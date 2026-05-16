from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8-sig").replace("\ufeff", "")

old = """        'end_date': end_date or '',
"""

new = """        'end_date': end_date or '',

        'chart_paid': float(total_paid),
        'chart_debt': float(total_debt),
        'chart_damages': float(damages_cost),
        'chart_net': float(net_profit),
        'chart_active_vehicles': active_vehicles,
        'chart_active_drivers': active_drivers,
        'chart_damages_pending': damages_pending,
        'chart_payments_paid': payments.filter(status='paid').count(),
        'chart_payments_partial': payments.filter(status='partial').count(),
        'chart_payments_pending': payments.filter(status='pending').count(),
"""

if "'chart_payments_paid'" not in text:
    text = text.replace(old, new, 1)

p.write_text(text, encoding="utf-8")
print("OK: contexto para gráficos avanzados agregado")
