from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8")

helper = r'''

def user_is_company_owner(user, company):
    return company.owner_id == user.id


def get_company_membership(user, company):
    return CompanyMember.objects.filter(
        user=user,
        company=company,
        is_active=True
    ).first()


def user_can_add_payments(user, company):
    if user_is_company_owner(user, company):
        return True
    member = get_company_membership(user, company)
    return bool(member and member.can_add_payments)


def user_can_add_damages(user, company):
    if user_is_company_owner(user, company):
        return True
    member = get_company_membership(user, company)
    return bool(member and member.can_add_damages)


def user_can_edit_data(user, company):
    if user_is_company_owner(user, company):
        return True
    member = get_company_membership(user, company)
    return bool(member and member.can_edit_data)


def user_can_export_reports(user, company):
    if user_is_company_owner(user, company):
        return True
    member = get_company_membership(user, company)
    return bool(member and member.can_export_reports)

'''

if "def user_can_add_payments(user, company):" not in text:
    text = text.replace("def user_company_access_q(user):", helper + "\ndef user_company_access_q(user):", 1)

p.write_text(text, encoding="utf-8")
print("Helpers de permisos por acción añadidos")
