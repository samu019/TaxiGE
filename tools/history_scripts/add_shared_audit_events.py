from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8")

text = text.replace(
"""        messages.success(request, 'Enlace compartido creado correctamente.')
        return redirect('/panel/shared-access/')""",
"""        audit_event(
            request,
            AuditLog.ACTION_CREATE,
            'sharing',
            'TaxiShareInvite',
            invite.id,
            invite.company.name,
            f'Invitación creada para empresa {invite.company.name} con rol {invite.role}'
        )

        messages.success(request, 'Enlace compartido creado correctamente.')
        return redirect('/panel/shared-access/')"""
)

text = text.replace(
"""    messages.success(request, 'Acceso compartido activado correctamente.')
    return redirect('/panel/')""",
"""    audit_event(
        request,
        AuditLog.ACTION_UPDATE,
        'sharing',
        'CompanyMember',
        invite.company.id,
        invite.company.name,
        f'Usuario aceptó invitación compartida para {invite.company.name} con rol {invite.role}'
    )

    messages.success(request, 'Acceso compartido activado correctamente.')
    return redirect('/panel/')"""
)

text = text.replace(
"""    messages.success(request, 'Invitación desactivada correctamente.')
    return redirect('/panel/shared-access/')""",
"""    audit_event(
        request,
        AuditLog.ACTION_UPDATE,
        'sharing',
        'TaxiShareInvite',
        invite.id,
        invite.company.name,
        f'Invitación desactivada para empresa {invite.company.name}'
    )

    messages.success(request, 'Invitación desactivada correctamente.')
    return redirect('/panel/shared-access/')"""
)

text = text.replace(
"""    messages.success(request, 'Acceso del socio desactivado correctamente.')
    return redirect('/panel/shared-access/')""",
"""    audit_event(
        request,
        AuditLog.ACTION_UPDATE,
        'sharing',
        'CompanyMember',
        member.id,
        member.company.name,
        f'Acceso retirado al usuario {member.user} en empresa {member.company.name}'
    )

    messages.success(request, 'Acceso del socio desactivado correctamente.')
    return redirect('/panel/shared-access/')"""
)

p.write_text(text, encoding="utf-8")
print("Auditoría de acceso compartido aplicada")
