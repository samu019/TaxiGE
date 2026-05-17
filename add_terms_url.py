from pathlib import Path

p = Path("config/urls.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

if "terms_page" not in text:
    text = text.replace(
        "home_page,",
        "home_page,\n    terms_page,"
    )

if "path('terms/'" not in text:
    text = text.replace(
        "path('', home_page, name='home'),",
        "path('', home_page, name='home'),\n    path('terms/', terms_page, name='terms'),"
    )

p.write_text(text, encoding="utf-8")
print("URL /terms/ agregada.")
