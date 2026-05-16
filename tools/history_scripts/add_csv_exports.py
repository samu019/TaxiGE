from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8")

if "import csv" not in text:
    text = "import csv\n" + text

if "HttpResponse" not in text:
    text = text.replace(
        "from django.http import HttpResponseForbidden, JsonResponse",
        "from django.http import HttpResponseForbidden, JsonResponse, HttpResponse"
    )
elif "HttpResponseForbidden, JsonResponse" in text and "HttpResponse" not in text.split("from django.http")[1].split("\n")[0]:
    text = text.replace(
        "from django.http import HttpResponseForbidden, JsonResponse",
        "from django.http import HttpResponseForbidden, JsonResponse, HttpResponse"
    )

code = r'''

def make_csv_response(filename, headers, rows):
    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    response.write('\ufeff')

    writer = csv.writer(response)
    writer.writerow(headers)

    for row in rows:
        writer.writerow(row)

    return response


@login_required
def export_vehicles_csv(request):
    guard_response = panel_guard(request)
    if guard_response:
        return guard_response

    vehicles = Vehicle.objects.filter(company__owner=request.user).select_related('company').order_by('-created_at')

    rows = []
    for v in vehicles:
        rows.append([
            v.id,
            v.company.name,
            v.plate_number,
            v.internal_code,
            v.brand,
            v.model,
            v.color,
            v.year,
            v.daily_target_amount,
            v.get_status_display(),
            v.created_at,
        ])

    return make_csv_response(
        'taxige_taxis.csv',
        ['ID', 'Empresa', 'Matrícula', 'Código interno', 'Marca', 'Modelo', 'Color', 'Año', 'Objetivo diario', 'Estado', 'Creado'],
        rows
    )


@login_required
def export_drivers_csv(request):
    guard_response = panel_guard(request)
    if guard_response:
        return guard_response

    drivers = Driver.objects.filter(company__owner=request.user).select_related('company', 'assigned_vehicle').order_by('-created_at')

    rows = []
    for d in drivers:
        rows.append([
            d.id,
            d.company.name,
            d.full_name,
            d.phone,
            d.identity_number,
            d.license_number,
            d.assigned_vehicle.plate_number if d.assigned_vehicle else '',
            d.daily_payment_amount,
            d.payment_day,
            d.get_status_display(),
            d.created_at,
        ])

    return make_csv_response(
        'taxige_conductores.csv',
        ['ID', 'Empresa', 'Conductor', 'Teléfono', 'Documento', 'Licencia', 'Taxi asignado', 'Pago diario', 'Día de pago', 'Estado', 'Creado'],
        rows
    )


@login_required
def export_payments_csv(request):
    guard_response = panel_guard(request)
    if guard_response:
        return guard_response

    payments = DriverPayment.objects.filter(company__owner=request.user).select_related('company', 'driver', 'vehicle').order_by('-payment_date', '-created_at')

    rows = []
    for p in payments:
        rows.append([
            p.id,
            p.company.name,
            p.driver.full_name,
            p.vehicle.plate_number if p.vehicle else '',
            p.payment_date,
            p.expected_amount,
            p.paid_amount,
            p.debt_amount,
            p.get_status_display(),
            p.notes,
            p.created_at,
        ])

    return make_csv_response(
        'taxige_pagos.csv',
        ['ID', 'Empresa', 'Conductor', 'Taxi', 'Fecha', 'Esperado', 'Pagado', 'Deuda', 'Estado', 'Notas', 'Creado'],
        rows
    )


@login_required
def export_damages_csv(request):
    guard_response = panel_guard(request)
    if guard_response:
        return guard_response

    damages = VehicleDamage.objects.filter(company__owner=request.user).select_related('company', 'driver', 'vehicle').order_by('-damage_date', '-created_at')

    rows = []
    for d in damages:
        rows.append([
            d.id,
            d.company.name,
            d.vehicle.plate_number if d.vehicle else '',
            d.driver.full_name if d.driver else '',
            d.title,
            d.damage_date,
            d.estimated_cost,
            d.final_cost,
            d.get_status_display(),
            d.description,
            d.created_at,
        ])

    return make_csv_response(
        'taxige_danos.csv',
        ['ID', 'Empresa', 'Taxi', 'Conductor', 'Daño', 'Fecha', 'Costo estimado', 'Costo final', 'Estado', 'Descripción', 'Creado'],
        rows
    )
'''

if "def export_vehicles_csv" not in text:
    text += code

p.write_text(text, encoding="utf-8")
print("OK: exportaciones CSV agregadas")
