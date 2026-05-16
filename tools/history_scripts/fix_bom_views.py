from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8-sig")

# Eliminar cualquier BOM invisible dentro del archivo
text = text.replace("\ufeff", "")

# Asegurar import csv arriba
if "import csv" not in text:
    text = "import csv\n" + text

# Asegurar HttpResponse
text = text.replace(
    "from django.http import HttpResponseForbidden, JsonResponse",
    "from django.http import HttpResponseForbidden, JsonResponse, HttpResponse"
)

p.write_text(text, encoding="utf-8")
print("OK: dashboard/views.py limpiado sin caracteres invisibles")
