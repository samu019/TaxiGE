from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

if "SaaSSubscription" not in text:
    text = text.replace(
        "from accounts.models import",
        "from accounts.models import SaaSSubscription,",
        1
    )

guard = r'''

def subscription_guard(request):
    if not request.user.is_authenticated:
        return None

    if request.user.is_superuser or getattr(request.user, "is_platform_owner", False):
        return None

    try:
        if request.user.saas_subscription.is_valid():
            return None
    except Exception:
        pass

    messages.error(
        request,
        "Tu suscripción SaaS no está activa. Renueva tu suscripción para acceder al panel."
    )
    return redirect("/accounts/login/")

'''

if "def subscription_guard(request):" not in text:
    text = text.replace(
        "def panel_guard(request):",
        guard + "\ndef panel_guard(request):",
        1
    )

old = """    guard_response = panel_guard(request)
    if guard_response:
        return guard_response
"""

new = """    guard_response = panel_guard(request)
    if guard_response:
        return guard_response

    subscription_response = subscription_guard(request)
    if subscription_response:
        return subscription_response
"""

if "subscription_response = subscription_guard(request)" not in text:
    text = text.replace(old, new)

p.write_text(text, encoding="utf-8")
print("Bloqueo por suscripción agregado al panel.")
