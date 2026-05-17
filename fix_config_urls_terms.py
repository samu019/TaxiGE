from pathlib import Path
import re

p = Path("config/urls.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

# Corregir cualquier import roto
text = re.sub(
    r'from accounts\.views import\s*\(',
    'from accounts.views import (',
    text
)

# Eliminar inserciones incorrectas como "home_page,\n    terms_page,"
text = text.replace("home_page,\n    terms_page,", "home_page,")

# Si terms_page no está importado, añadirlo antes del cierre del import
if "terms_page" not in text:
    text = text.replace(
        "home_page,",
        "home_page,\n    terms_page,",
        1
    )

# Añadir URL /terms/ si no existe
if "path('terms/'" not in text:
    text = text.replace(
        "path('', home_page, name='home'),",
        "path('', home_page, name='home'),\n    path('terms/', terms_page, name='terms'),",
        1
    )

p.write_text(text, encoding="utf-8")
print("config/urls.py corregido correctamente.")
