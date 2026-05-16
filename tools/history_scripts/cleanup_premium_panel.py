from pathlib import Path
import re

# 1. Mejorar botones editar
files = [
    "templates/dashboard/panel_vehicles.html",
    "templates/dashboard/panel_drivers.html",
]

for file in files:
    p = Path(file)
    text = p.read_text(encoding="utf-8")

    text = re.sub(
        r'<a href="([^"]+/edit/)" style="font-weight:bold; color:#111827;">\s*Editar\s*</a>',
        r'<a href="\1" class="btn btn-secondary btn-small">Editar</a>',
        text
    )

    p.write_text(text, encoding="utf-8")
    print("OK:", file)

# 2. Envolver tablas en table-wrap si todavía no lo están
table_files = [
    "templates/dashboard/panel_vehicles.html",
    "templates/dashboard/panel_drivers.html",
    "templates/dashboard/panel_payments.html",
    "templates/dashboard/panel_damages.html",
    "templates/dashboard/panel_home.html",
]

for file in table_files:
    p = Path(file)
    text = p.read_text(encoding="utf-8")

    if '<div class="table-wrap">' not in text:
        text = text.replace("<table>", '<div class="table-wrap">\n<table>')
        text = text.replace("</table>", "</table>\n</div>")

    p.write_text(text, encoding="utf-8")
    print("OK responsive table:", file)

print("OK: limpieza premium aplicada")
