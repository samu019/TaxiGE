from pathlib import Path

# 1. Corregir enlaces del template: usar rutas directas
tpl = Path("templates/dashboard/panel_home.html")
text = tpl.read_text(encoding="utf-8-sig").replace("\ufeff", "")

text = text.replace('{% url \'dashboard_export_pdf\' %}', '/panel/export/pdf/')
text = text.replace('{% url "dashboard_export_pdf" %}', '/panel/export/pdf/')
text = text.replace('{% url \'dashboard_export_excel\' %}', '/panel/export/excel/')
text = text.replace('{% url "dashboard_export_excel" %}', '/panel/export/excel/')

tpl.write_text(text, encoding="utf-8")
print("OK: enlaces PDF/Excel convertidos a rutas directas")


# 2. Asegurar URLs en dashboard/urls.py
urls = Path("dashboard/urls.py")
u = urls.read_text(encoding="utf-8-sig").replace("\ufeff", "")

if "export/pdf/" not in u:
    u = u.replace(
        "urlpatterns = [",
        """urlpatterns = [
    path('export/pdf/', views.dashboard_export_pdf, name='dashboard_export_pdf'),
    path('export/excel/', views.dashboard_export_excel, name='dashboard_export_excel'),"""
    )

urls.write_text(u, encoding="utf-8")
print("OK: urls.py revisado")
