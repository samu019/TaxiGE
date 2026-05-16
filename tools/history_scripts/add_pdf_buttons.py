from pathlib import Path

replacements = {
    "templates/dashboard/panel_vehicles.html": (
        '<a href="/panel/reports/vehicles.csv" class="btn btn-secondary">Exportar CSV</a>',
        '<a href="/panel/reports/vehicles.csv" class="btn btn-secondary">Exportar CSV</a>\n        <a href="/panel/reports/vehicles.pdf" class="btn btn-secondary">Exportar PDF</a>'
    ),
    "templates/dashboard/panel_drivers.html": (
        '<a href="/panel/reports/drivers.csv" class="btn btn-secondary">Exportar CSV</a>',
        '<a href="/panel/reports/drivers.csv" class="btn btn-secondary">Exportar CSV</a>\n        <a href="/panel/reports/drivers.pdf" class="btn btn-secondary">Exportar PDF</a>'
    ),
    "templates/dashboard/panel_payments.html": (
        '<a href="/panel/reports/payments.csv" class="btn btn-secondary">Exportar CSV</a>',
        '<a href="/panel/reports/payments.csv" class="btn btn-secondary">Exportar CSV</a>\n        <a href="/panel/reports/payments.pdf" class="btn btn-secondary">Exportar PDF</a>'
    ),
    "templates/dashboard/panel_damages.html": (
        '<a href="/panel/reports/damages.csv" class="btn btn-secondary">Exportar CSV</a>',
        '<a href="/panel/reports/damages.csv" class="btn btn-secondary">Exportar CSV</a>\n        <a href="/panel/reports/damages.pdf" class="btn btn-secondary">Exportar PDF</a>'
    ),
}

for file, (old, new) in replacements.items():
    p = Path(file)
    text = p.read_text(encoding="utf-8")

    if "Exportar PDF" not in text and old in text:
        text = text.replace(old, new, 1)

    p.write_text(text, encoding="utf-8")
    print("OK:", file)

print("OK: botones PDF agregados")
