from pathlib import Path
import re

p = Path("templates/dashboard/panel_home.html")
text = p.read_text(encoding="utf-8-sig").replace("\ufeff", "")

# Corregir textos dañados
text = text.replace("da�os", "daños")
text = text.replace("Da�os", "Daños")
text = text.replace("Costo da±os", "Costo daños")
text = text.replace("Costo daÃ±os", "Costo daños")

# Eliminar todos los bloques duplicados de filtros
pattern = re.compile(
    r'\s*<div class="section" style="margin-bottom:18px;">\s*'
    r'<form method="get" class="filter-bar">.*?'
    r'</form>\s*</div>\s*',
    re.DOTALL
)

text = re.sub(pattern, "\n", text)

# Insertar un solo filtro después del subtítulo
subtitle = '<p class="page-subtitle">Resumen financiero, mensual y operativo de tu empresa de taxis.</p>'

filter_block = '''
<div class="section" style="margin-bottom:18px;">
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
</div>
'''

if subtitle in text:
    text = text.replace(subtitle, subtitle + "\n" + filter_block, 1)

p.write_text(text, encoding="utf-8")
print("OK: filtros duplicados eliminados y textos corregidos")
