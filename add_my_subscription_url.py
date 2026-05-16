from pathlib import Path

p = Path("dashboard/urls.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

route = "    path('subscription/', views.panel_my_subscription, name='panel_my_subscription'),"

if "panel_my_subscription" not in text:
    text = text.replace("urlpatterns = [", "urlpatterns = [\n" + route, 1)

p.write_text(text, encoding="utf-8")
print("URL Mi suscripción agregada.")
