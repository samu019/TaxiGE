from pathlib import Path

filters = {
    "templates/dashboard/panel_vehicles.html": '''
<form method="get" class="filter-bar">
    <input type="text" name="q" value="{{ request.GET.q }}" placeholder="Buscar matrícula, marca, modelo o color...">

    <select name="status">
        <option value="">Todos los estados</option>
        <option value="active" {% if request.GET.status == "active" %}selected{% endif %}>Activo</option>
        <option value="inactive" {% if request.GET.status == "inactive" %}selected{% endif %}>Inactivo</option>
        <option value="maintenance" {% if request.GET.status == "maintenance" %}selected{% endif %}>Mantenimiento</option>
    </select>

    <button type="submit" class="btn">Filtrar</button>
    <a href="/panel/vehicles/" class="btn btn-secondary">Limpiar</a>
</form>
''',
    "templates/dashboard/panel_drivers.html": '''
<form method="get" class="filter-bar">
    <input type="text" name="q" value="{{ request.GET.q }}" placeholder="Buscar conductor, teléfono, documento o taxi...">

    <select name="status">
        <option value="">Todos los estados</option>
        <option value="active" {% if request.GET.status == "active" %}selected{% endif %}>Activo</option>
        <option value="inactive" {% if request.GET.status == "inactive" %}selected{% endif %}>Inactivo</option>
        <option value="suspended" {% if request.GET.status == "suspended" %}selected{% endif %}>Suspendido</option>
    </select>

    <button type="submit" class="btn">Filtrar</button>
    <a href="/panel/drivers/" class="btn btn-secondary">Limpiar</a>
</form>
''',
    "templates/dashboard/panel_payments.html": '''
<form method="get" class="filter-bar">
    <input type="text" name="q" value="{{ request.GET.q }}" placeholder="Buscar conductor, taxi o nota...">

    <select name="status">
        <option value="">Todos los estados</option>
        <option value="paid" {% if request.GET.status == "paid" %}selected{% endif %}>Pagado</option>
        <option value="partial" {% if request.GET.status == "partial" %}selected{% endif %}>Pago parcial</option>
        <option value="pending" {% if request.GET.status == "pending" %}selected{% endif %}>Pendiente</option>
    </select>

    <button type="submit" class="btn">Filtrar</button>
    <a href="/panel/payments/" class="btn btn-secondary">Limpiar</a>
</form>
''',
    "templates/dashboard/panel_damages.html": '''
<form method="get" class="filter-bar">
    <input type="text" name="q" value="{{ request.GET.q }}" placeholder="Buscar taxi, conductor, daño o descripción...">

    <select name="status">
        <option value="">Todos los estados</option>
        <option value="pending" {% if request.GET.status == "pending" %}selected{% endif %}>Pendiente</option>
        <option value="in_progress" {% if request.GET.status == "in_progress" %}selected{% endif %}>En reparación</option>
        <option value="resolved" {% if request.GET.status == "resolved" %}selected{% endif %}>Resuelto</option>
    </select>

    <button type="submit" class="btn">Filtrar</button>
    <a href="/panel/damages/" class="btn btn-secondary">Limpiar</a>
</form>
''',
}

for file, filter_html in filters.items():
    p = Path(file)
    text = p.read_text(encoding="utf-8")

    if 'class="filter-bar"' not in text:
        text = text.replace('</div>\n\n<div class="table-wrap">', '</div>\n\n' + filter_html + '\n<div class="table-wrap">', 1)

    p.write_text(text, encoding="utf-8")
    print("OK:", file)

print("OK: filtros visuales agregados")
