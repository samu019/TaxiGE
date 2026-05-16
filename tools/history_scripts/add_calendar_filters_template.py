from pathlib import Path

p = Path("templates/dashboard/calendar.html")
text = p.read_text(encoding="utf-8")

filter_block = """
        <div style="display:flex; gap:10px; flex-wrap:wrap; margin-bottom:18px;">
            <a href="/panel/calendar/" style="padding:8px 12px; border-radius:12px; text-decoration:none; color:inherit; background:{% if active_filter == 'all' %}rgba(59,130,246,.35){% else %}rgba(255,255,255,.08){% endif %};">Todos</a>

            <a href="/panel/calendar/?filter=payments" style="padding:8px 12px; border-radius:12px; text-decoration:none; color:inherit; background:{% if active_filter == 'payments' %}rgba(59,130,246,.35){% else %}rgba(255,255,255,.08){% endif %};">Pagos</a>

            <a href="/panel/calendar/?filter=damages" style="padding:8px 12px; border-radius:12px; text-decoration:none; color:inherit; background:{% if active_filter == 'damages' %}rgba(59,130,246,.35){% else %}rgba(255,255,255,.08){% endif %};">Daños</a>

            <a href="/panel/calendar/?filter=late" style="padding:8px 12px; border-radius:12px; text-decoration:none; color:inherit; background:{% if active_filter == 'late' %}rgba(239,68,68,.35){% else %}rgba(255,255,255,.08){% endif %};">Atrasados</a>
        </div>
"""

if "filter=payments" not in text:
    text = text.replace('<div class="timeline">', filter_block + '\n        <div class="timeline">', 1)

p.write_text(text, encoding="utf-8")
print("Filtros visuales añadidos al calendario")
