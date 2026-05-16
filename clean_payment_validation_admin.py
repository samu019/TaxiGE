from pathlib import Path

p = Path("accounts/admin.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

# Quitar import ValidationError si existe
text = text.replace("from django.core.exceptions import ValidationError\n", "")

old = """        if obj.status == 'approved' and not obj.payment_verified:
            raise ValidationError(
                'No se puede aprobar la solicitud porque el pago aún no ha sido verificado.'
            )
"""

new = """        if obj.status == 'approved' and not obj.payment_verified:
            self.message_user(
                request,
                'No se puede aprobar la solicitud porque el pago aún no ha sido verificado.',
                level='error'
            )
            obj.status = AdminRequest.STATUS_PENDING
"""

text = text.replace(old, new, 1)

p.write_text(text, encoding="utf-8")
print("Validación convertida a mensaje limpio en admin.")
