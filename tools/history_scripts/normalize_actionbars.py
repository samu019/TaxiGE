from pathlib import Path
import re

configs = {
    "templates/dashboard/panel_vehicles.html": {
        "title": "Mis taxis",
        "subtitle": "Lista de vehículos registrados en tu empresa.",
        "csv": "/panel/reports/vehicles.csv",
        "pdf": "/panel/reports/vehicles.pdf",
        "create": "/panel/vehicles/create/",
        "create_text": "Registrar taxi",
    },
    "templates/dashboard/panel_drivers.html": {
        "title": "Mis conductores",
        "subtitle": "Conductores asignados a tu empresa.",
        "csv": "/panel/reports/drivers.csv",
        "pdf": "/panel/reports/drivers.pdf",
        "create": "/panel/drivers/create/",
        "create_text": "Registrar conductor",
    },
    "templates/dashboard/panel_payments.html": {
        "title": "Pagos",
        "subtitle": "Historial de pagos de tus conductores.",
        "csv": "/panel/reports/payments.csv",
        "pdf": "/panel/reports/payments.pdf",
        "create": "/panel/payments/create/",
        "create_text": "Registrar pago",
    },
    "templates/dashboard/panel_damages.html": {
        "title": "Daños",
        "subtitle": "Daños registrados en tus taxis.",
        "csv": "/panel/reports/damages.csv",
        "pdf": "/panel/reports/damages.pdf",
        "create": "/panel/damages/create/",
        "create_text": "Registrar daño",
    },
}

for file, cfg in configs.items():
    p = Path(file)
    text = p.read_text(encoding="utf-8")

    actionbar = f'''
<div class="page-head">
    <div class="page-head-text">
        <h1 class="page-title">{cfg["title"]}</h1>
        <p class="page-subtitle">{cfg["subtitle"]}</p>
    </div>

    <div class="page-actions">
        <a href="{cfg["csv"]}" class="btn btn-secondary">Exportar CSV</a>
        <a href="{cfg["pdf"]}" class="btn btn-secondary">Exportar PDF</a>
        <a href="{cfg["create"]}" class="btn">{cfg["create_text"]}</a>
    </div>
</div>
'''

    # Reemplaza desde el primer h1 hasta antes de la primera table-wrap o section.
    text = re.sub(
        r'<h1 class="page-title">.*?</h1>\s*<p class="page-subtitle">.*?</p>\s*(?:<a[^>]*>.*?</a>\s*)*',
        actionbar + "\n",
        text,
        count=1,
        flags=re.DOTALL
    )

    # Elimina duplicados de botones sueltos si quedaron
    text = re.sub(r'\s*<a href="/panel/reports/[^"]+" class="btn btn-secondary">Exportar (?:CSV|PDF)</a>', '', text)
    text = re.sub(r'\s*<a href="/panel/[^"]+/create/" class="btn[^"]*">Registrar [^<]+</a>', '', text)

    # Asegura que actionbar quede una sola vez: si eliminó botones dentro del actionbar por regex, reconstruimos al principio
    if 'class="page-actions"' not in text:
        text = re.sub(r'{% block content %}', '{% block content %}\n' + actionbar, text, count=1)

    p.write_text(text, encoding="utf-8")
    print("OK:", file)

print("OK: action bars profesionales aplicadas")
