from pathlib import Path

p = Path("templates/accounts/register_owner_kyc.html")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

if "{% load payment_settings_tags %}" not in text:
    text = "{% load payment_settings_tags %}\n{% active_payment_settings as payment_settings %}\n" + text

p.write_text(text, encoding="utf-8")
print("Template tag de pagos cargado en register_owner_kyc.html")
