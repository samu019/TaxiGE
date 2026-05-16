from pathlib import Path
import re

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8-sig").replace("\ufeff", "")

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

    total_expected = payments.aggregate(total=Sum('expected_amount'))['total'] or Decimal('0')
    total_paid = payments.aggregate(total=Sum('paid_amount'))['total'] or Decimal('0')
    total_debt = total_expected - total_paid

    damages_cost = damages.aggregate(total=Sum('estimated_cost'))['total'] or Decimal('0')
    net_profit = total_paid - damages_cost

    if total_expected > 0:
        collection_rate = round((total_paid / total_expected) * 100, 2)
    else:
        collection_rate = Decimal('0')

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
print("OK: panel_home limpiado y reconstruido correctamente")
