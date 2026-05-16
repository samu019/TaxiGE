from pathlib import Path

p = Path("dashboard/urls.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

route = "    path('subscription/renew/', views.panel_subscription_renew, name='panel_subscription_renew'),"

if "panel_subscription_renew" not in text:
    text = text.replace("urlpatterns = [", "urlpatterns = [\n" + route, 1)

p.write_text(text, encoding="utf-8")
print("URL de renovación agregada.")
