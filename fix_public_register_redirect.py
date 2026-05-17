from pathlib import Path

p = Path("accounts/views.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

old = """            user = form.save()
            login(request, user)
            return redirect('/request-admin/')"""

new = """            user = form.save()
            login(request, user)
            return render(request, 'accounts/request_admin_success.html')"""

if old not in text:
    raise SystemExit("No se encontró el bloque exacto en public_register().")

text = text.replace(old, new, 1)
p.write_text(text, encoding="utf-8")
print("public_register corregido.")
