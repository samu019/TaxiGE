from pathlib import Path

p = Path("templates/dashboard/calendar.html")
text = p.read_text(encoding="utf-8")

notice = """
        {% if total_events_count > 8 %}
            <div style="margin-top:18px; padding:14px; border-radius:14px; background:rgba(59,130,246,.10); border:1px solid rgba(59,130,246,.25);">
                Mostrando los primeros 8 eventos de {{ total_events_count }}. 
                Usa los filtros o entra en Pagos/Daños para ver todos los registros.
            </div>
        {% endif %}
"""

if "Mostrando los primeros 8 eventos" not in text:
    text = text.replace("</div>\n    </section>\n</div>", "</div>\n" + notice + "\n    </section>\n</div>", 1)

p.write_text(text, encoding="utf-8")
print("Aviso de límite añadido al calendario")
