from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8")

old = "invites = TaxiShareInvite.objects.filter(invited_by=request.user).select_related('company').order_by('-created_at')"
new = "invites = TaxiShareInvite.objects.filter(invited_by=request.user, is_active=True).select_related('company').order_by('-created_at')"

text = text.replace(old, new)

p.write_text(text, encoding="utf-8")
print("Ahora se muestran solo invitaciones activas")
