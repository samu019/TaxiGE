from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8")

block = r'''

@login_required
def deactivate_taxi_invite(request, invite_id):
    guard_response = panel_guard(request)
    if guard_response:
        return guard_response

    if request.method != 'POST':
        return redirect('/panel/shared-access/')

    invite = get_object_or_404(
        TaxiShareInvite,
        id=invite_id,
        company__owner=request.user
    )

    invite.is_active = False
    invite.save(update_fields=['is_active'])

    messages.success(request, 'Invitación desactivada correctamente.')
    return redirect('/panel/shared-access/')


@login_required
def remove_company_member(request, member_id):
    guard_response = panel_guard(request)
    if guard_response:
        return guard_response

    if request.method != 'POST':
        return redirect('/panel/shared-access/')

    member = get_object_or_404(
        CompanyMember,
        id=member_id,
        company__owner=request.user
    )

    member.is_active = False
    member.save(update_fields=['is_active'])

    messages.success(request, 'Acceso del socio desactivado correctamente.')
    return redirect('/panel/shared-access/')
'''

if 'def deactivate_taxi_invite(request, invite_id):' not in text:
    text += block

p.write_text(text, encoding="utf-8")
print("Vistas para desactivar invitaciones y socios añadidas")
