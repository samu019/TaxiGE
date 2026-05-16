from pathlib import Path
import re

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8-sig").replace("\ufeff", "")

if "from django.utils import timezone" not in text:
    text = text.replace(
        "from django.shortcuts import render, redirect, get_object_or_404",
        "from django.shortcuts import render, redirect, get_object_or_404\nfrom django.utils import timezone"
    )

new_panel_home = r'''@login_required
def panel_home(request):
    guard_response = panel_guard(request)
    if guard_response:
        return guard_response

    user = request.user

    companies = Company.objects.filter(owner=user)
    vehicles = Vehicle.objects.filter(company__owner=user)
    drivers = Driver.objects.filter(company__owner=user)
    payments = DriverPayment.objects.filter(company__owner=user)
    damages = VehicleDamage.objects.filter(company__owner=user)

    today = timezone.localdate()
    month_start = today.replace(day=1)
    last_7_start = today - timezone.timedelta(days=7)

    total_expected = payments.aggregate(total=Sum('expected_amount'))['total'] or Decimal('0')
    total_paid = payments.aggregate(total=Sum('paid_amount'))['total'] or Decimal('0')
    total_debt = total_expected - total_paid

    damages_cost = damages.aggregate(total=Sum('estimated_cost'))['total'] or Decimal('0')
    net_profit = total_paid - damages_cost

    collection_rate = round((total_paid / total_expected) * 100, 2) if total_expected > 0 else Decimal('0')

    month_payments = payments.filter(payment_date__gte=month_start, payment_date__lte=today)
    today_payments = payments.filter(payment_date=today)
    last_7_payments = payments.filter(payment_date__gte=last_7_start, payment_date__lte=today)
    month_damages = damages.filter(damage_date__gte=month_start, damage_date__lte=today)

    month_expected = month_payments.aggregate(total=Sum('expected_amount'))['total'] or Decimal('0')
    month_paid = month_payments.aggregate(total=Sum('paid_amount'))['total'] or Decimal('0')
    month_debt = month_expected - month_paid
    month_damages_cost = month_damages.aggregate(total=Sum('estimated_cost'))['total'] or Decimal('0')
    month_net_profit = month_paid - month_damages_cost

    today_paid = today_payments.aggregate(total=Sum('paid_amount'))['total'] or Decimal('0')
    last_7_paid = last_7_payments.aggregate(total=Sum('paid_amount'))['total'] or Decimal('0')

    active_vehicles = vehicles.filter(status='active').count()
    active_drivers = drivers.filter(status='active').count()
    damages_pending = damages.filter(status='pending').count()

    context = {
        'companies_count': companies.count(),
        'vehicles_count': vehicles.count(),
        'drivers_count': drivers.count(),
        'payments_count': payments.count(),
        'damages_count': damages.count(),

        'active_vehicles': active_vehicles,
        'active_drivers': active_drivers,
        'damages_pending': damages_pending,

        'total_expected': total_expected,
        'total_paid': total_paid,
        'total_debt': total_debt,
        'damages_cost': damages_cost,
        'net_profit': net_profit,
        'collection_rate': collection_rate,

        'month_label': today.strftime('%m/%Y'),
        'month_expected': month_expected,
        'month_paid': month_paid,
        'month_debt': month_debt,
        'month_damages_cost': month_damages_cost,
        'month_net_profit': month_net_profit,
        'today_paid': today_paid,
        'last_7_paid': last_7_paid,

        'recent_payments': payments.order_by('-payment_date', '-created_at')[:5],
        'recent_damages': damages.order_by('-damage_date', '-created_at')[:5],
    }

    return render(request, 'dashboard/panel_home.html', context)


'''

text = re.sub(
    r'@login_required\s+def panel_home\(request\):.*?(?=\n@login_required\s+def panel_vehicles)',
    new_panel_home,
    text,
    count=1,
    flags=re.DOTALL
)

p.write_text(text, encoding="utf-8")
print("OK: panel_home limpio, único y mensual")
