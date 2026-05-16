from pathlib import Path

buttons = {
    "templates/dashboard/panel_vehicles.html": ('href="/panel/vehicles/create/"', '<a href="/panel/reports/vehicles.csv" class="btn btn-secondary">Exportar CSV</a>'),
    "templates/dashboard/panel_drivers.html": ('href="/panel/drivers/create/"', '<a href="/panel/reports/drivers.csv" class="btn btn-secondary">Exportar CSV</a>'),
    "templates/dashboard/panel_payments.html": ('href="/panel/payments/create/"', '<a href="/panel/reports/payments.csv" class="btn btn-secondary">Exportar CSV</a>'),
    "templates/dashboard/panel_damages.html": ('href="/panel/damages/create/"', '<a href="/panel/reports/damages.csv" class="btn btn-secondary">Exportar CSV</a>'),
}

for file, (marker, button) in buttons.items():
    p = Path(file)
    text = p.read_text(encoding="utf-8")

    if button not in text and marker in text:
        text = text.replace(marker, button + "\n        <a " + marker, 1)

    p.write_text(text, encoding="utf-8")
    print("OK:", file)

print("OK: botones CSV agregados")
