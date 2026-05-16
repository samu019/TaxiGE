from pathlib import Path

p = Path("templates/dashboard/notifications.html")
text = p.read_text(encoding="utf-8")

pagination = """
        {% if notifications.has_other_pages %}
            <div style="display:flex; gap:10px; justify-content:center; align-items:center; flex-wrap:wrap; margin-top:22px;">
                {% if notifications.has_previous %}
                    <a href="?filter={{ active_filter }}&page={{ notifications.previous_page_number }}" style="padding:9px 13px; border-radius:12px; background:rgba(255,255,255,.08); text-decoration:none; color:inherit;">Anterior</a>
                {% endif %}

                <span style="opacity:.8;">Página {{ notifications.number }} de {{ notifications.paginator.num_pages }}</span>

                {% if notifications.has_next %}
                    <a href="?filter={{ active_filter }}&page={{ notifications.next_page_number }}" style="padding:9px 13px; border-radius:12px; background:rgba(255,255,255,.08); text-decoration:none; color:inherit;">Siguiente</a>
                {% endif %}
            </div>
        {% endif %}
"""

if "notifications.has_other_pages" not in text:
    text = text.replace("{% endfor %}", "{% endfor %}\n" + pagination, 1)

p.write_text(text, encoding="utf-8")
print("Controles de paginación añadidos")
