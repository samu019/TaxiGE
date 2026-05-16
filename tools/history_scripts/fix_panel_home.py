# =========================================================
# Script para corregir filter_type y filtros en panel_home
# =========================================================
from django.shortcuts import render
from django.utils import timezone
from decimal import Decimal
from datetime import timedelta
from django.db.models import Sum
from companies.models import Company
from vehicles.models import Vehicle
from drivers.models import Driver
from payments.models import DriverPayment
from damages.models import VehicleDamage

def panel_home(request):
    user = request.user

    companies = Company.objects.filter(owner=user)
    vehicles = Vehicle.objects.filter(company__owner=user)
    drivers = Driver.objects.filter(company__owner=user)

    payments = DriverPayment.objects.filter(company__owner=user)
    damages = VehicleDamage.objects.filter(company__owner=user)

    # ===========================
    # Definir filtro y fechas
    # ===========================
    today = timezone.localdate()
    filter_type = request.GET.get('filter', 'month')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    # ===========================
    # Aplicar filtros
    # ===========================
    if filter_type == 'today':
        payments = payments.filter(payment_date=today)
        damages = damages.filter(damage_date=today)
    elif filter_type == 'week':
        week_start = today - timedelta(days=7)
        payments = payments.filter(payment_date__gte=week_start)
        damages = damages.filter(damage_date__gte=week_start)
    elif filter_type == 'custom' and start_date and end_date:
        payments = payments.filter(payment_date__range=[start_date, end_date])
        damages = damages.filter(damage_date__range=[start_date, end_date])
    else:
        payments = payments.filter(payment_date__year=today.year,
                                   payment_date__month=today.month)
        damages = damages.filter(damage_date__year=today.year,
                                 damage_date__month=today.month)

    # ===========================
    # Totales
    # ===========================
    total_expected = payments.aggregate(total=Sum('expected_amount'))['total'] or Decimal('0')
    total_paid = payments.aggregate(total=Sum('paid_amount'))['total'] or Decimal('0')
    total_debt = total_expected - total_paid
    damages_cost = damages.aggregate(total=Sum('estimated_cost'))['total'] or Decimal('0')
    net_profit = total_paid - damages_cost
    collection_rate = round((total_paid / total_expected) * 100, 2) if total_expected > 0 else Decimal('0')

    context = {
        'companies': companies,
        'vehicles': vehicles,
        'drivers': drivers,
        'payments': payments,
        'damages': damages,
        'total_expected': total_expected,
        'total_paid': total_paid,
        'total_debt': total_debt,
        'damages_cost': damages_cost,
        'net_profit': net_profit,
        'collection_rate': collection_rate,
        'recent_payments': payments.order_by('-payment_date', '-created_at')[:5],
        'recent_damages': damages.order_by('-damage_date', '-created_at')[:5],
        'active_filter': filter_type,
        'start_date': start_date or '',
        'end_date': end_date or '',
    }

    return render(request, 'dashboard/panel_home.html', context)

print("OK: panel_home corregido con filter_type y filtros aplicados")
