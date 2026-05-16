from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8")

helper = r'''

def shared_permissions_for_role(role):
    permissions = {
        CompanyMember.ROLE_PARTNER: {
            'can_view_payments': True,
            'can_view_damages': True,
            'can_add_payments': False,
            'can_add_damages': False,
            'can_edit_data': False,
            'can_invite_members': False,
            'can_export_reports': True,
        },
        CompanyMember.ROLE_MANAGER: {
            'can_view_payments': True,
            'can_view_damages': True,
            'can_add_payments': True,
            'can_add_damages': True,
            'can_edit_data': True,
            'can_invite_members': False,
            'can_export_reports': False,
        },
        CompanyMember.ROLE_VIEWER: {
            'can_view_payments': True,
            'can_view_damages': True,
            'can_add_payments': False,
            'can_add_damages': False,
            'can_edit_data': False,
            'can_invite_members': False,
            'can_export_reports': False,
        },
        CompanyMember.ROLE_ACCOUNTANT: {
            'can_view_payments': True,
            'can_view_damages': False,
            'can_add_payments': False,
            'can_add_damages': False,
            'can_edit_data': False,
            'can_invite_members': False,
            'can_export_reports': True,
        },
    }
    return permissions.get(role, permissions[CompanyMember.ROLE_VIEWER])

'''

if "def shared_permissions_for_role(role):" not in text:
    text = text.replace("def user_company_access_q(user):", helper + "\ndef user_company_access_q(user):", 1)

old = """    CompanyMember.objects.get_or_create(
        company=invite.company,
        user=request.user,
        defaults={
            'role': invite.role,
            'is_active': True,
            'can_view_payments': True,
            'can_view_damages': True,
            'can_export_reports': True,
        }
    )"""

new = """    permissions = shared_permissions_for_role(invite.role)

    member, created = CompanyMember.objects.get_or_create(
        company=invite.company,
        user=request.user,
        defaults={
            'role': invite.role,
            'is_active': True,
            **permissions,
        }
    )

    if not created:
        member.role = invite.role
        member.is_active = True
        for key, value in permissions.items():
            setattr(member, key, value)
        member.save()"""

text = text.replace(old, new)

p.write_text(text, encoding="utf-8")
print("Permisos por rol aplicados")
