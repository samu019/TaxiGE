from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8")

old = """        audit_event(
            request,
            AuditLog.ACTION_CREATE,
            'sharing',
            'TaxiShareInvite',
            invite.id,
            invite.company.name,
            f'Invitación creada para empresa {invite.company.name} con rol {invite.role}'
        )

        messages.success(request, 'Enlace compartido creado correctamente.')"""

new = """        audit_event(
            request,
            AuditLog.ACTION_CREATE,
            'sharing',
            'TaxiShareInvite',
            invite.id,
            invite.company.name,
            f'Invitación creada para empresa {invite.company.name} con rol {invite.role}'
        )

        create_notification(
            request.user,
            'Invitación compartida creada',
            f'Se creó un enlace de acceso para {invite.company.name} con rol {invite.get_role_display()}.',
            'success',
            '/panel/shared-access/'
        )

        messages.success(request, 'Enlace compartido creado correctamente.')"""

text = text.replace(old, new)

p.write_text(text, encoding="utf-8")
print("Notificación al crear invitación añadida")
