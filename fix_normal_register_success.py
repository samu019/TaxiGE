from pathlib import Path

p = Path("accounts/views.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

text = text.replace(
    "return render(request, 'accounts/request_admin_success.html')",
    "return render(request, 'accounts/normal_register_success.html')",
    1
)

p.write_text(text, encoding="utf-8")
print("Registro normal ahora usa normal_register_success.html")
