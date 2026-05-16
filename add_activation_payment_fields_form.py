from pathlib import Path

p = Path("accounts/forms.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

old = """            'message',
        ]"""

new = """            'message',

            'payment_reference',
            'payment_receipt',
        ]"""

if "'payment_reference'" not in text:
    text = text.replace(old, new, 1)

# Mejorar labels si existe el bloque labels
if "payment_reference" in text and "'payment_reference':" not in text:
    marker = "        labels = {"
    if marker in text:
        text = text.replace(
            marker,
            marker + "\n            'payment_reference': 'Referencia de pago',\n            'payment_receipt': 'Comprobante de pago',",
            1
        )

p.write_text(text, encoding="utf-8")
print("Formulario KYC actualizado con campos de pago")
