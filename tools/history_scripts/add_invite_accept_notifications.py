from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8")

old = """    audit_event(
        request,
        AuditLog.ACTION_UPDATE,
        'sharing',
        'CompanyMember',
        invite.company.id,
        invite.company.name,
        f'Usuario aceptó invitación compartida para {invite.company.name} con rol {invite.role}'
    )

    messages.success(request, 'Acceso compartido activado correctamente.')"""

new = """    audit_event(
        request,
        AuditLog.ACTION_UPDATE,
        'sharing',
        'CompanyMember',
        invite.company.id,
        invite.company.name,
        f'Usuario aceptó invitación compartida para {invite.company.name} con rol {invite.role}'
    )

    create_notification(
        invite.company.owner,
        'Nuevo socio conectado',
        f'{request.user} aceptó la invitación para acceder a {invite.company.name} como {invite.get_role_display()}.',
        'success',
        '/panel/shared-access/'
    )

    create_notification(
        request.user,
        'Acceso compartido activado',
        f'Ya puedes ver la empresa {invite.company.name} desde tu panel.',
        'success',
        '/panel/'
    )

    messages.success(request, 'Acceso compartido activado correctamente.')"""

text = text.replace(old, new)

p.write_text(text, encoding="utf-8")
print("Notificaciones al aceptar invitación añadidas")
