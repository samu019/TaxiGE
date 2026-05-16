from pathlib import Path

p = Path("accounts/models.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

if "activation_fee = models.DecimalField" in text:
    print("Los campos de pago ya existen.")
    raise SystemExit(0)

marker = "    message = models.TextField(blank=True, null=True)"

new_fields = """
    activation_fee = models.DecimalField(max_digits=12, decimal_places=2, default=50000)
    payment_reference = models.CharField(max_length=100, blank=True, null=True)
    payment_receipt = models.FileField(upload_to='kyc/payment_receipts/', blank=True, null=True)
    payment_verified = models.BooleanField(default=False)
    payment_verified_at = models.DateTimeField(blank=True, null=True)
    payment_note = models.TextField(blank=True, null=True)

    message = models.TextField(blank=True, null=True)
"""

if marker not in text:
    raise SystemExit("No se encontró el campo message.")

text = text.replace(marker, new_fields, 1)

p.write_text(text, encoding="utf-8")
print("Campos de pago agregados correctamente.")
