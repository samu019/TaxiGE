from pathlib import Path

p = Path("dashboard/urls.py")
text = p.read_text(encoding="utf-8")

routes = """
    path('reports/vehicles.pdf', views.export_vehicles_pdf, name='export_vehicles_pdf'),
    path('reports/drivers.pdf', views.export_drivers_pdf, name='export_drivers_pdf'),
    path('reports/payments.pdf', views.export_payments_pdf, name='export_payments_pdf'),
    path('reports/damages.pdf', views.export_damages_pdf, name='export_damages_pdf'),
"""

if "reports/vehicles.pdf" not in text:
    text = text.replace("]\n", routes + "]\n")

p.write_text(text, encoding="utf-8")
print("OK: rutas PDF agregadas")
