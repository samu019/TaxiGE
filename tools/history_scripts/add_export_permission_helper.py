from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8")

helper = r'''

def user_has_any_export_permission(user):
    companies = Company.objects.filter(user_company_direct_access_q(user)).distinct()
    for company in companies:
        if user_can_export_reports(user, company):
            return True
    return False

'''

if "def user_has_any_export_permission(user):" not in text:
    text = text.replace("def user_can_export_reports(user, company):", helper + "\ndef user_can_export_reports(user, company):", 1)

p.write_text(text, encoding="utf-8")
print("Helper global de exportación añadido")
