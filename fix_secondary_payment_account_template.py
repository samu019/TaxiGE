from pathlib import Path

p = Path("templates/accounts/register_owner_kyc.html")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

if "payment_settings.secondary_account_number" not in text:
    marker = """        <div>
            <span>Número de cuenta</span>
            <strong>{{ payment_settings.primary_account_number }}</strong>
        </div>"""

    insert = marker + """

        <div>
            <span>Número de cuenta ECOBANK</span>
            <strong>{{ payment_settings.secondary_account_number }}</strong>
        </div>"""

    text = text.replace(marker, insert, 1)

p.write_text(text, encoding="utf-8")
print("Número de cuenta ECOBANK agregado dinámicamente.")
