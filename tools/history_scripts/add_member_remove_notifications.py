from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8")

old = """    audit_event(
        request,
        AuditLog.ACTION_UPDATE,
        'sharing',
        'CompanyMember',
        member.id,
        member.company.name,
        f'Acceso retirado al usuario {member.user} en empresa {member.company.name}'
    )

    messages.success(request, 'Acceso del socio desactivado correctamente.')"""

new = """    audit_event(
        request,
        AuditLog.ACTION_UPDATE,
        'sharing',
        'CompanyMember',
        member.id,
        member.company.name,
        f'Acceso retirado al usuario {member.user} en empresa {member.company.name}'
    )

    create_notification(
        request.user,
        'Acceso retirado',
        f'Se retiró el acceso de {member.user} a {member.company.name}.',
        'warning',
        '/panel/shared-access/'
    )

    create_notification(
        member.user,
        'Acceso desactivado',
        f'Tu acceso a {member.company.name} fue desactivado.',
        'warning',
        '/panel/'
    )

    messages.success(request, 'Acceso del socio desactivado correctamente.')"""

text = text.replace(old, new)

p.write_text(text, encoding="utf-8")
print("Notificaciones al retirar acceso añadidas")
