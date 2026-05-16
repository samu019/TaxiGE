from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8")

old = "members = CompanyMember.objects.filter(company__owner=request.user).select_related('company', 'user').order_by('-created_at')"
new = "members = CompanyMember.objects.filter(company__owner=request.user, is_active=True).select_related('company', 'user').order_by('-created_at')"

text = text.replace(old, new)

p.write_text(text, encoding="utf-8")
print("Ahora se muestran solo socios activos")
