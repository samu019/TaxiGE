from pathlib import Path

p = Path('templates/dashboard/panel_home.html')
text = p.read_text(encoding='utf-8-sig').replace('\ufeff','')

insert_after = '<p class="page-subtitle">Resumen financiero, mensual y operativo de tu empresa de taxis.</p>'

filters_html = '''<div class="section" style="margin-bottom:18px;">
<form method="get" class="filter-bar">
<select name="filter">
<option value="month" {% if active_filter == 'month' %}selected{% endif %}>Este mes</option>
<option value="today" {% if active_filter == 'today' %}selected{% endif %}>Hoy</option>
<option value="week" {% if active_filter == 'week' %}selected{% endif %}>Últimos 7 días</option>
<option value="custom" {% if active_filter == 'custom' %}selected{% endif %}>Personalizado</option>
</select>
<input type="date" name="start_date" value="{{ start_date }}">
<input type="date" name="end_date" value="{{ end_date }}">
<button type="submit" class="btn-primary">Aplicar filtro</button>
</form>
</div>'''

if filters_html not in text:
    text = text.replace(insert_after,insert_after + filters_html)

p.write_text(text,encoding='utf-8')
print("OK: filtros frontend agregados")
