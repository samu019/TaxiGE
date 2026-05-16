from pathlib import Path

p = Path("templates/accounts/register_owner_kyc.html")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

old = """        <div>
            <span>Banco</span>
            <strong>BANGE</strong>
        </div>"""

new = """        <div>
            <span>Banco principal</span>
            <strong>BANGE</strong>
        </div>

        <div>
            <span>Banco alternativo</span>
            <strong>ECOBANK</strong>
        </div>"""

if "ECOBANK" not in text:
    text = text.replace(old, new, 1)

old_note = """Realiza el pago de activación y sube el comprobante. Tu solicitud será revisada por el administrador antes de activar tu cuenta de propietario."""

new_note = """Realiza el pago de activación en BANGE o ECOBANK y sube el comprobante. Tu solicitud será revisada por el administrador antes de activar tu cuenta de propietario."""

text = text.replace(old_note, new_note, 1)

p.write_text(text, encoding="utf-8")
print("ECOBANK agregado al bloque de pago.")
