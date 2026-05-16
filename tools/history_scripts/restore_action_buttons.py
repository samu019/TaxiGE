from pathlib import Path
import re

configs = {
    "templates/dashboard/panel_vehicles.html": {
        "csv": "/panel/reports/vehicles.csv",
        "pdf": "/panel/reports/vehicles.pdf",
        "create": "/panel/vehicles/create/",
        "create_text": "Registrar taxi",
    },
    "templates/dashboard/panel_drivers.html": {
        "csv": "/panel/reports/drivers.csv",
        "pdf": "/panel/reports/drivers.pdf",
        "create": "/panel/drivers/create/",
        "create_text": "Registrar conductor",
    },
    "templates/dashboard/panel_payments.html": {
        "csv": "/panel/reports/payments.csv",
        "pdf": "/panel/reports/payments.pdf",
        "create": "/panel/payments/create/",
        "create_text": "Registrar pago",
    },
    "templates/dashboard/panel_damages.html": {
        "csv": "/panel/reports/damages.csv",
        "pdf": "/panel/reports/damages.pdf",
        "create": "/panel/damages/create/",
        "create_text": "Registrar daño",
    },
}

for file, cfg in configs.items():
    p = Path(file)
    text = p.read_text(encoding="utf-8")

    buttons = f'''
    <div class="page-actions">
        <a href="{cfg["csv"]}" class="btn btn-secondary">Exportar CSV</a>
        <a href="{cfg["pdf"]}" class="btn btn-secondary">Exportar PDF</a>
        <a href="{cfg["create"]}" class="btn">{cfg["create_text"]}</a>
    </div>
'''

    text = re.sub(
        r'<div class="page-actions">\s*</div>',
        buttons,
        text,
        count=1,
        flags=re.DOTALL
    )

    p.write_text(text, encoding="utf-8")
    print("OK:", file)

print("OK: botones CSV/PDF/Registrar restaurados")
