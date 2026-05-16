from pathlib import Path

updates = {
    "templates/dashboard/panel_payments.html": (
        "<th>Estado</th>",
        "<th>Estado</th>\n            <th>Acción</th>",
        '<td><span class="badge">{{ payment.get_status_display }}</span></td>',
        '<td><span class="badge">{{ payment.get_status_display }}</span></td>\n                <td><a href="/panel/payments/{{ payment.id }}/edit/" class="btn btn-secondary btn-small">Editar</a></td>'
    ),
    "templates/dashboard/panel_damages.html": (
        "<th>Estado</th>",
        "<th>Estado</th>\n            <th>Acción</th>",
        '<td><span class="badge">{{ damage.get_status_display }}</span></td>',
        '<td><span class="badge">{{ damage.get_status_display }}</span></td>\n                <td><a href="/panel/damages/{{ damage.id }}/edit/" class="btn btn-secondary btn-small">Editar</a></td>'
    ),
}

for file, data in updates.items():
    p = Path(file)
    text = p.read_text(encoding="utf-8")
    th_old, th_new, td_old, td_new = data

    if "<th>Acción</th>" not in text:
        text = text.replace(th_old, th_new, 1)

    if "/edit/" not in text:
        text = text.replace(td_old, td_new)

    p.write_text(text, encoding="utf-8")
    print("OK:", file)

print("OK: botones de edición agregados")
