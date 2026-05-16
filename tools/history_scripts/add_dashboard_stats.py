from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8")

text = text.replace(
"""from django.http import HttpResponseForbidden""",
"""from django.http import HttpResponseForbidden, JsonResponse"""
)

text = text.replace(
"""from .forms import VehicleForm, DriverForm, DriverPaymentForm, VehicleDamageForm""",
"""from .forms import VehicleForm, DriverForm, DriverPaymentForm, VehicleDamageForm
from django.db.models import Sum"""
)

old = """    context = {
        'companies_count': companies.count(),
        'vehicles_count': vehicles.count(),
        'drivers_count': drivers.count(),
        'payments_count': payments.count(),
        'damages_count': damages.count(),
        'recent_payments': payments.order_by('-payment_date', '-created_at')[:5],
        'recent_damages': damages.order_by('-damage_date', '-created_at')[:5],
    }"""

new = """    total_expected = payments.aggregate(total=Sum('expected_amount'))['total'] or 0
    total_paid = payments.aggregate(total=Sum('paid_amount'))['total'] or 0
    total_debt = total_expected - total_paid

    damages_pending = damages.filter(status='pending').count()
    damages_cost = damages.aggregate(total=Sum('estimated_cost'))['total'] or 0

    active_vehicles = vehicles.filter(status='active').count()
    active_drivers = drivers.filter(status='active').count()

    context = {
        'companies_count': companies.count(),
        'vehicles_count': vehicles.count(),
        'drivers_count': drivers.count(),
        'payments_count': payments.count(),
        'damages_count': damages.count(),

        'total_expected': total_expected,
        'total_paid': total_paid,
        'total_debt': total_debt,
        'damages_pending': damages_pending,
        'damages_cost': damages_cost,
        'active_vehicles': active_vehicles,
        'active_drivers': active_drivers,

        'recent_payments': payments.order_by('-payment_date', '-created_at')[:5],
        'recent_damages': damages.order_by('-damage_date', '-created_at')[:5],
    }"""

if old not in text:
    print("AVISO: no encontré bloque context exacto. Puede que ya esté cambiado.")
else:
    text = text.replace(old, new, 1)

p.write_text(text, encoding="utf-8")
print("OK: estadísticas avanzadas agregadas a panel_home")
