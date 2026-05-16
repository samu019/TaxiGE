from pathlib import Path

files = {
    "templates/dashboard/panel_vehicles.html": (
        '<a href="/panel/vehicles/{{ vehicle.id }}/edit/" class="btn btn-secondary btn-small">Editar</a>',
        '<a href="/panel/vehicles/{{ vehicle.id }}/edit/" class="btn btn-secondary btn-small">Editar</a> <a href="/panel/vehicles/{{ vehicle.id }}/delete/" class="btn btn-small" style="background:#dc2626;">Eliminar</a>'
    ),
    "templates/dashboard/panel_drivers.html": (
        '<a href="/panel/drivers/{{ driver.id }}/edit/" class="btn btn-secondary btn-small">Editar</a>',
        '<a href="/panel/drivers/{{ driver.id }}/edit/" class="btn btn-secondary btn-small">Editar</a> <a href="/panel/drivers/{{ driver.id }}/delete/" class="btn btn-small" style="background:#dc2626;">Eliminar</a>'
    ),
    "templates/dashboard/panel_payments.html": (
        '<a href="/panel/payments/{{ payment.id }}/edit/" class="btn btn-secondary btn-small">Editar</a>',
        '<a href="/panel/payments/{{ payment.id }}/edit/" class="btn btn-secondary btn-small">Editar</a> <a href="/panel/payments/{{ payment.id }}/delete/" class="btn btn-small" style="background:#dc2626;">Eliminar</a>'
    ),
    "templates/dashboard/panel_damages.html": (
        '<a href="/panel/damages/{{ damage.id }}/edit/" class="btn btn-secondary btn-small">Editar</a>',
        '<a href="/panel/damages/{{ damage.id }}/edit/" class="btn btn-secondary btn-small">Editar</a> <a href="/panel/damages/{{ damage.id }}/delete/" class="btn btn-small" style="background:#dc2626;">Eliminar</a>'
    ),
}

for file, (old, new) in files.items():
    p = Path(file)
    text = p.read_text(encoding="utf-8")

    if old in text and "delete/" not in text:
        text = text.replace(old, new)

    p.write_text(text, encoding="utf-8")
    print("OK:", file)

print("OK: botones eliminar agregados")
