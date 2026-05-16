from pathlib import Path

p = Path("templates/accounts/register_owner_kyc.html")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

replacements = {
    "<strong>50.000 XAF</strong>": "<strong>{{ payment_settings.activation_fee }} XAF</strong>",
    "<strong>BANGE</strong>": "<strong>{{ payment_settings.primary_bank_name }}</strong>",
    "<strong>TaxiGE Platform</strong>": "<strong>{{ payment_settings.primary_account_holder }}</strong>",
    "<strong>100200300400</strong>": "<strong>{{ payment_settings.primary_account_number }}</strong>",
    "<strong>ECOBANK</strong>": "<strong>{{ payment_settings.secondary_bank_name }}</strong>",
    "<strong>Pendiente de configurar</strong>": "<strong>{{ payment_settings.secondary_account_number }}</strong>",
}

for old, new in replacements.items():
    text = text.replace(old, new)

old_note = "Realiza el pago de activación en BANGE o ECOBANK y sube el comprobante. Tu solicitud será revisada por el administrador antes de activar tu cuenta de propietario."
new_note = "{{ payment_settings.payment_instructions }}"
text = text.replace(old_note, new_note)

p.write_text(text, encoding="utf-8")
print("Template KYC conectado dinámicamente con configuración de pagos.")
