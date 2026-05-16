from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

# Cambiar redirección del guard
text = text.replace(
    'return redirect("/accounts/login/")',
    'return redirect("/panel/subscription/renew/")',
    1
)

view = r'''

@login_required
def panel_subscription_renew(request):
    subscription = None

    try:
        subscription = request.user.saas_subscription
    except Exception:
        subscription = None

    payment_settings = None
    try:
        from accounts.models import SaaSPaymentSettings
        payment_settings = SaaSPaymentSettings.get_active()
    except Exception:
        payment_settings = None

    return render(request, 'dashboard/subscription_renew.html', {
        'subscription': subscription,
        'payment_settings': payment_settings,
    })

'''

if "def panel_subscription_renew(request):" not in text:
    text += view

p.write_text(text, encoding="utf-8")
print("Vista de renovación de suscripción agregada.")
