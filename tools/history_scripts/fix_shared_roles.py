from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8")

old = "'roles': CompanyMember.ROLE_CHOICES,"
new = "'roles': [(v, l) for v, l in CompanyMember.ROLE_CHOICES if v != CompanyMember.ROLE_OWNER],"

text = text.replace(old, new)

p.write_text(text, encoding="utf-8")
print("Rol propietario ocultado en invitaciones")
