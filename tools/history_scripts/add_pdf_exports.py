from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8-sig").replace("\ufeff", "")

imports = """
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
"""

if "from reportlab.lib import colors" not in text:
    text = imports + "\n" + text

if "HttpResponse" not in text:
    text = text.replace(
        "from django.http import HttpResponseForbidden, JsonResponse",
        "from django.http import HttpResponseForbidden, JsonResponse, HttpResponse"
    )

code = r'''

def make_pdf_response(filename, title, headers, rows):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    doc = SimpleDocTemplate(
        response,
        pagesize=landscape(A4),
        rightMargin=24,
        leftMargin=24,
        topMargin=24,
        bottomMargin=24,
    )

    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph('TaxiGE Platform', styles['Title']))
    elements.append(Paragraph(title, styles['Heading2']))
    elements.append(Spacer(1, 12))

    data = [headers] + rows

    table = Table(data, repeatRows=1)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#111827')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('GRID', (0, 0), (-1, -1), 0.25, colors.HexColor('#CBD5E1')),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#F8FAFC')),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F8FAFC')]),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ]))

    elements.append(table)
    doc.build(elements)

    return response


@login_required
def export_vehicles_pdf(request):
    guard_response = panel_guard(request)
    if guard_response:
        return guard_response

    vehicles = Vehicle.objects.filter(company__owner=request.user).select_related('company').order_by('-created_at')

    rows = [[
        str(v.id),
        v.company.name,
        v.plate_number,
        v.brand,
        v.model,
        v.color,
        str(v.daily_target_amount),
        v.get_status_display(),
    ] for v in vehicles]

    return make_pdf_response(
        'taxige_taxis.pdf',
        'Reporte de taxis',
        ['ID', 'Empresa', 'Matrícula', 'Marca', 'Modelo', 'Color', 'Objetivo diario', 'Estado'],
        rows
    )


@login_required
def export_drivers_pdf(request):
    guard_response = panel_guard(request)
    if guard_response:
        return guard_response

    drivers = Driver.objects.filter(company__owner=request.user).select_related('company', 'assigned_vehicle').order_by('-created_at')

    rows = [[
        str(d.id),
        d.company.name,
        d.full_name,
        d.phone,
        d.assigned_vehicle.plate_number if d.assigned_vehicle else '',
        str(d.daily_payment_amount),
        d.payment_day,
        d.get_status_display(),
    ] for d in drivers]

    return make_pdf_response(
        'taxige_conductores.pdf',
        'Reporte de conductores',
        ['ID', 'Empresa', 'Conductor', 'Teléfono', 'Taxi', 'Pago diario', 'Día pago', 'Estado'],
        rows
    )


@login_required
def export_payments_pdf(request):
    guard_response = panel_guard(request)
    if guard_response:
        return guard_response

    payments = DriverPayment.objects.filter(company__owner=request.user).select_related('company', 'driver', 'vehicle').order_by('-payment_date', '-created_at')

    rows = [[
        str(p.id),
        p.driver.full_name,
        p.vehicle.plate_number if p.vehicle else '',
        str(p.payment_date),
        str(p.expected_amount),
        str(p.paid_amount),
        str(p.debt_amount),
        p.get_status_display(),
    ] for p in payments]

    return make_pdf_response(
        'taxige_pagos.pdf',
        'Reporte de pagos',
        ['ID', 'Conductor', 'Taxi', 'Fecha', 'Esperado', 'Pagado', 'Deuda', 'Estado'],
        rows
    )


@login_required
def export_damages_pdf(request):
    guard_response = panel_guard(request)
    if guard_response:
        return guard_response

    damages = VehicleDamage.objects.filter(company__owner=request.user).select_related('company', 'driver', 'vehicle').order_by('-damage_date', '-created_at')

    rows = [[
        str(d.id),
        d.vehicle.plate_number if d.vehicle else '',
        d.driver.full_name if d.driver else '',
        d.title,
        str(d.damage_date),
        str(d.estimated_cost),
        str(d.final_cost),
        d.get_status_display(),
    ] for d in damages]

    return make_pdf_response(
        'taxige_danos.pdf',
        'Reporte de daños',
        ['ID', 'Taxi', 'Conductor', 'Daño', 'Fecha', 'Estimado', 'Final', 'Estado'],
        rows
    )
'''

if "def export_vehicles_pdf" not in text:
    text += code

p.write_text(text, encoding="utf-8")
print("OK: exportaciones PDF agregadas")
