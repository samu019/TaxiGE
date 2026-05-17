from pathlib import Path

p = Path("accounts/views.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

if "def terms_page(request):" not in text:
    text += """

def terms_page(request):
    return render(request, 'accounts/terms.html')
"""

p.write_text(text, encoding="utf-8")
print("Vista de términos agregada.")
