from pathlib import Path

p = Path("templates/dashboard/notifications.html")
text = p.read_text(encoding="utf-8")

text = text.replace("{{ notifications|length }}", "{{ total_count }}")

text = text.replace(
"""        <div class="notification-stat">
            <span>No leídas</span>
            <strong>{{ unread_count }}</strong>
        </div>

        <div class="notification-stat">
            <span>Estado</span>
            <strong>{% if unread_count > 0 %}Pendiente{% else %}Al día{% endif %}</strong>
        </div>""",
"""        <div class="notification-stat">
            <span>No leídas</span>
            <strong>{{ unread_count }}</strong>
        </div>

        <div class="notification-stat">
            <span>Leídas</span>
            <strong>{{ read_count }}</strong>
        </div>"""
)

filter_block = """
        <div style="display:flex; gap:10px; flex-wrap:wrap; margin-bottom:18px;">
            <a href="/panel/notifications/" style="padding:9px 13px; border-radius:12px; text-decoration:none; background:{% if active_filter == 'all' %}rgba(59,130,246,.35){% else %}rgba(255,255,255,.08){% endif %}; color:inherit;">Todas</a>

            <a href="/panel/notifications/?filter=unread" style="padding:9px 13px; border-radius:12px; text-decoration:none; background:{% if active_filter == 'unread' %}rgba(59,130,246,.35){% else %}rgba(255,255,255,.08){% endif %}; color:inherit;">No leídas</a>

            <a href="/panel/notifications/?filter=read" style="padding:9px 13px; border-radius:12px; text-decoration:none; background:{% if active_filter == 'read' %}rgba(59,130,246,.35){% else %}rgba(255,255,255,.08){% endif %}; color:inherit;">Leídas</a>
        </div>
"""

if "filter=unread" not in text:
    text = text.replace("{% for n in notifications %}", filter_block + "\n        {% for n in notifications %}", 1)

p.write_text(text, encoding="utf-8")
print("Filtros visuales añadidos")
