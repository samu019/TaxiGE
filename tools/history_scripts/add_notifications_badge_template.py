from pathlib import Path

p = Path("templates/dashboard/panel_base.html")
text = p.read_text(encoding="utf-8")

old = '''<span>Notificaciones</span>'''
new = '''<span>Notificaciones</span>
                    {% if global_unread_notifications %}
                        <span style="margin-left:8px; padding:2px 7px; border-radius:999px; background:#ef4444; color:white; font-size:12px;">{{ global_unread_notifications }}</span>
                    {% endif %}'''

text = text.replace(old, new)

p.write_text(text, encoding="utf-8")
print("Badge de notificaciones añadido")
