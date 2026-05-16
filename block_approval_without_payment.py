from pathlib import Path

p = Path("accounts/admin.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

# Importar ValidationError
if "from django.core.exceptions import ValidationError" not in text:
    text = "from django.core.exceptions import ValidationError\n" + text

# Insertar validación en AdminRequestAdmin.save_model
if "No se puede aprobar la solicitud porque el pago aún no ha sido verificado." not in text:
    marker = "def save_model(self, request, obj, form, change):"

    if marker in text:
        replacement = marker + """
        if obj.status == 'approved' and not obj.payment_verified:
            raise ValidationError(
                'No se puede aprobar la solicitud porque el pago aún no ha sido verificado.'
            )
"""
        text = text.replace(marker, replacement, 1)

p.write_text(text, encoding="utf-8")
print("Bloqueo de aprobación sin pago verificado agregado.")
