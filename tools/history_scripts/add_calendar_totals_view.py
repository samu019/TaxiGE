from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8")

old = """    pending_payments = payments.filter(status__in=['pending', 'partial', 'late'])
    pending_damages = damages.filter(status__in=['pending', 'in_repair'])

    events = []"""

new = """    pending_payments = payments.filter(status__in=['pending', 'partial', 'late'])
    pending_damages = damages.filter(status__in=['pending', 'in_repair'])

    total_pending_debt = sum([p.debt_amount for p in pending_payments])
    total_active_damage_cost = sum([d.estimated_cost for d in pending_damages])
    total_operational_risk = total_pending_debt + total_active_damage_cost

    events = []"""

text = text.replace(old, new)

old2 = """        'late_payments_count': pending_payments.filter(payment_date__lt=today).count(),
    })"""

new2 = """        'late_payments_count': pending_payments.filter(payment_date__lt=today).count(),
        'total_pending_debt': total_pending_debt,
        'total_active_damage_cost': total_active_damage_cost,
        'total_operational_risk': total_operational_risk,
    })"""

text = text.replace(old2, new2)

p.write_text(text, encoding="utf-8")
print("Totales financieros añadidos al calendario")
