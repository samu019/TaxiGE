from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

old = """    payment_settings = None
    try:
        from accounts.models import SaaSPaymentSettings
        payment_settings = SaaSPaymentSettings.get_active()
"""

new = """    from accounts.models import SaaSSubscription, SaaSPaymentHistory, SaaSPaymentSettings

    payment_settings = None
    try:
        payment_settings = SaaSPaymentSettings.get_active()
"""

if old not in text:
    raise SystemExit("No se encontró el bloque de import local de SaaSPaymentSettings.")

text = text.replace(old, new, 1)

p.write_text(text, encoding="utf-8")
print("Imports locales de renovación corregidos.")
