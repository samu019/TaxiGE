from pathlib import Path

p = Path("dashboard/urls.py")
text = p.read_text(encoding="utf-8")

route = "    path('calendar/', views.panel_calendar, name='panel_calendar'),"

if route not in text:
    text = text.replace("urlpatterns = [", "urlpatterns = [\n" + route, 1)

p.write_text(text, encoding="utf-8")
print("Ruta /panel/calendar/ añadida")
