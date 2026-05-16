from pathlib import Path

p = Path("accounts/admin.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

old = """        self.message_user(
            request,
            f'{approved_count} solicitud(es) KYC aprobada(s). Empresa y taxi inicial creados automáticamente.'
        )
"""

new = """        if approved_count > 0:
            self.message_user(
                request,
                f'{approved_count} solicitud(es) KYC aprobada(s). Empresa y taxi inicial creados automáticamente.'
            )
        else:
            self.message_user(
                request,
                'No había solicitudes pendientes para aprobar.',
                level='warning'
            )
"""

if "No había solicitudes pendientes para aprobar." not in text:
    text = text.replace(old, new, 1)

p.write_text(text, encoding="utf-8")
print("Mensajes de aprobación masiva mejorados.")
