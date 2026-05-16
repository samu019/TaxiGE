from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8")

functions = [
    "export_vehicles_csv",
    "export_drivers_csv",
    "export_payments_csv",
    "export_damages_csv",
    "export_vehicles_pdf",
    "export_drivers_pdf",
    "export_payments_pdf",
    "export_damages_pdf",
    "dashboard_export_excel",
    "dashboard_export_pdf",
]

for fn in functions:
    marker = f"def {fn}(request):"
    idx = text.find(marker)
    if idx == -1:
        continue

    start_body = text.find("\n", idx) + 1
    guard = """    if not user_has_any_export_permission(request.user):
        messages.error(request, 'No tienes permiso para exportar reportes.')
        return redirect('/panel/')

"""

    next_part = text[start_body:start_body + 300]
    if "No tienes permiso para exportar reportes" not in next_part:
        text = text[:start_body] + guard + text[start_body:]

p.write_text(text, encoding="utf-8")
print("Exportaciones protegidas por permiso")
