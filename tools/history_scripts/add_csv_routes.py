from pathlib import Path

p = Path("dashboard/urls.py")
text = p.read_text(encoding="utf-8")

routes = """
    path('reports/vehicles.csv', views.export_vehicles_csv, name='export_vehicles_csv'),
    path('reports/drivers.csv', views.export_drivers_csv, name='export_drivers_csv'),
    path('reports/payments.csv', views.export_payments_csv, name='export_payments_csv'),
    path('reports/damages.csv', views.export_damages_csv, name='export_damages_csv'),
"""

if "reports/vehicles.csv" not in text:
    text = text.replace("]\n", routes + "]\n")

p.write_text(text, encoding="utf-8")
print("OK: rutas CSV agregadas")
