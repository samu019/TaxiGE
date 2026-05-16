from pathlib import Path

p = Path("accounts/admin.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

old = """        for admin_request in queryset.filter(status=AdminRequest.STATUS_PENDING):
            user = admin_request.user
"""

new = """        blocked_count = 0

        for admin_request in queryset.filter(status=AdminRequest.STATUS_PENDING):
            if not admin_request.payment_verified:
                blocked_count += 1
                continue

            user = admin_request.user
"""

if "blocked_count = 0" not in text:
    text = text.replace(old, new, 1)

old_msg = """        self.message_user(
            request,
            f'{approved_count} solicitud(es) KYC aprobada(s). Empresa y taxi inicial creados automáticamente.'
        )
"""

new_msg = """        if blocked_count:
            self.message_user(
                request,
                f'{blocked_count} solicitud(es) no fueron aprobadas porque el pago no está verificado.',
                level='error'
            )

        self.message_user(
            request,
            f'{approved_count} solicitud(es) KYC aprobada(s). Empresa y taxi inicial creados automáticamente.'
        )
"""

if "no fueron aprobadas porque el pago no está verificado" not in text:
    text = text.replace(old_msg, new_msg, 1)

p.write_text(text, encoding="utf-8")
print("Acción masiva KYC protegida contra pagos no verificados.")
