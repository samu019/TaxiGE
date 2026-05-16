from pathlib import Path

p = Path("dashboard/urls.py")
text = p.read_text(encoding="utf-8")

if "shared-access/" not in text:
    text = text.replace(
        "urlpatterns = [",
        "urlpatterns = [\n    path('shared-access/', views.panel_shared_access, name='panel_shared_access'),"
    )

p.write_text(text, encoding="utf-8")
print("Ruta /panel/shared-access/ añadida")
