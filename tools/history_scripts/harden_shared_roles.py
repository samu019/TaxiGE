from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8")

old = """        role = request.POST.get('role', CompanyMember.ROLE_VIEWER)
        max_uses = request.POST.get('max_uses', '1')"""

new = """        role = request.POST.get('role', CompanyMember.ROLE_VIEWER)

        allowed_roles = [
            CompanyMember.ROLE_PARTNER,
            CompanyMember.ROLE_MANAGER,
            CompanyMember.ROLE_VIEWER,
            CompanyMember.ROLE_ACCOUNTANT,
        ]

        if role not in allowed_roles:
            role = CompanyMember.ROLE_VIEWER

        max_uses = request.POST.get('max_uses', '1')"""

text = text.replace(old, new)

p.write_text(text, encoding="utf-8")
print("Rol propietario bloqueado desde backend")
