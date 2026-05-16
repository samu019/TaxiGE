from pathlib import Path

p = Path("dashboard/urls.py")
text = p.read_text(encoding="utf-8-sig").replace("\ufeff", "")

if "dashboard_export_pdf" not in text:
    text = text.replace(
        "urlpatterns = [",
        """urlpatterns = [
    path('export/pdf/', views.dashboard_export_pdf, name='dashboard_export_pdf'),
    path('export/excel/', views.dashboard_export_excel, name='dashboard_export_excel'),"""
    )

p.write_text(text, encoding="utf-8")
print("OK: URLs PDF/Excel registradas")
