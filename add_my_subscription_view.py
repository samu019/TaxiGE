from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

view = r'''

@login_required
def panel_my_subscription(request):
    guard_response = panel_guard(request)
    if guard_response:
        return guard_response

    subscription = None
    payments = []

    try:
        subscription = request.user.saas_subscription
        payments = subscription.payment_history.all().order_by('-created_at')[:20]
    except Exception:
        subscription = None
        payments = []

    return render(request, 'dashboard/my_subscription.html', {
        'subscription': subscription,
        'payments': payments,
    })

'''

if "def panel_my_subscription(request):" not in text:
    text += view

p.write_text(text, encoding="utf-8")
print("Vista Mi suscripción agregada.")
