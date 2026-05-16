from pathlib import Path
import re

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8-sig").replace("\ufeff", "")

old_start = text.find("def make_pdf_response(")
old_end = text.find("@login_required\ndef export_vehicles_pdf", old_start)

if old_start == -1 or old_end == -1:
    raise SystemExit("No encontré make_pdf_response correctamente")

new_function = r'''
def make_pdf_response(filename, title, headers, rows):
    from reportlab.lib.units import mm
    from reportlab.platypus import PageBreak
    from django.utils import timezone

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    doc = SimpleDocTemplate(
        response,
        pagesize=landscape(A4),
        rightMargin=16 * mm,
        leftMargin=16 * mm,
        topMargin=14 * mm,
        bottomMargin=14 * mm,
    )

    styles = getSampleStyleSheet()
    elements = []

    generated_at = timezone.localtime().strftime('%d/%m/%Y %H:%M')

    header_data = [
        [
            Paragraph('<b>TaxiGE Platform</b><br/><font size="8">Sistema profesional de gestión de taxis</font>', styles['Normal']),
            Paragraph(f'<b>{title}</b><br/><font size="8">Generado: {generated_at}</font>', styles['Normal']),
        ]
    ]

    header_table = Table(header_data, colWidths=[130 * mm, 130 * mm])
    header_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#111827')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.white),
        ('BOX', (0, 0), (-1, -1), 0.8, colors.HexColor('#111827')),
        ('INNERGRID', (0, 0), (-1, -1), 0.3, colors.HexColor('#334155')),
        ('LEFTPADDING', (0, 0), (-1, -1), 12),
        ('RIGHTPADDING', (0, 0), (-1, -1), 12),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
    ]))

    elements.append(header_table)
    elements.append(Spacer(1, 14))

    summary_data = [
        ['Total de registros', str(len(rows)), 'Formato', 'PDF corporativo'],
    ]

    summary_table = Table(summary_data, colWidths=[45 * mm, 35 * mm, 35 * mm, 55 * mm])
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F8FAFC')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#0F172A')),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0, 0), (-1, -1), 0.3, colors.HexColor('#CBD5E1')),
        ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Bold'),
        ('FONTNAME', (2, 0), (2, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 7),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
    ]))

    elements.append(summary_table)
    elements.append(Spacer(1, 14))

    safe_rows = rows if rows else [['Sin datos'] + ['' for _ in headers[1:]]]
    data = [headers] + safe_rows

    available_width = landscape(A4)[0] - (32 * mm)
    col_count = len(headers)
    col_widths = [available_width / col_count for _ in headers]

    table = Table(data, repeatRows=1, colWidths=col_widths)

    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#111827')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 8),
        ('FONTSIZE', (0, 1), (-1, -1), 7),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('GRID', (0, 0), (-1, -1), 0.25, colors.HexColor('#CBD5E1')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F8FAFC')]),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ]))

    elements.append(table)
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(
        '<font size="8" color="#64748B">Documento generado automáticamente por TaxiGE Platform. Uso interno y administrativo.</font>',
        styles['Normal']
    ))

    def footer(canvas, doc):
        canvas.saveState()
        canvas.setFont('Helvetica', 8)
        canvas.setFillColor(colors.HexColor('#64748B'))
        canvas.drawString(16 * mm, 10 * mm, 'TaxiGE Platform')
        canvas.drawRightString(281 * mm, 10 * mm, f'Página {doc.page}')
        canvas.restoreState()

    doc.build(elements, onFirstPage=footer, onLaterPages=footer)

    return response


'''

text = text[:old_start] + new_function + text[old_end:]

p.write_text(text, encoding="utf-8")
print("OK: PDF premium corporativo aplicado")
