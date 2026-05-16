from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8")

block = r'''

@login_required
def panel_calendar(request):
    guard_response = panel_guard(request)
    if guard_response:
        return guard_response

    today = timezone.localdate()

    payments = DriverPayment.objects.filter(
        user_company_access_q(request.user)
    ).select_related('company', 'driver', 'vehicle').order_by('payment_date')

    damages = VehicleDamage.objects.filter(
        user_company_access_q(request.user)
    ).select_related('company', 'driver', 'vehicle').order_by('damage_date')

    pending_payments = payments.filter(status__in=['pending', 'partial', 'late'])
    pending_damages = damages.filter(status__in=['pending', 'in_repair'])

    events = []

    for payment in pending_payments[:80]:
        is_late = payment.payment_date < today or payment.status == 'late'
        events.append({
            'type': 'payment',
            'title': f'Pago pendiente - {payment.driver}',
            'date': payment.payment_date,
            'status': 'Atrasado' if is_late else payment.get_status_display(),
            'amount': payment.debt_amount,
            'vehicle': payment.vehicle,
            'link': '/panel/payments/',
            'level': 'danger' if is_late else 'warning',
        })

    for damage in pending_damages[:80]:
        events.append({
            'type': 'damage',
            'title': f'Daño - {damage.title}',
            'date': damage.damage_date,
            'status': damage.get_status_display(),
            'amount': damage.estimated_cost,
            'vehicle': damage.vehicle,
            'link': '/panel/damages/',
            'level': 'danger' if damage.status == 'pending' else 'warning',
        })

    events = sorted(events, key=lambda x: x['date'])

    return render_panel(request, 'dashboard/calendar.html', {
        'today': today,
        'events': events,
        'pending_payments_count': pending_payments.count(),
        'pending_damages_count': pending_damages.count(),
        'late_payments_count': pending_payments.filter(payment_date__lt=today).count(),
    })
'''

if "def panel_calendar(request):" not in text:
    text += block

p.write_text(text, encoding="utf-8")
print("Vista calendario añadida")
