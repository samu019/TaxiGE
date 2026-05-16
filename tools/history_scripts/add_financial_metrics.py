from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8-sig").replace("\ufeff", "")

old = """    total_paid = payments.aggregate(total=Sum('paid_amount'))['total'] or 0
    total_expected = payments.aggregate(total=Sum('expected_amount'))['total'] or 0
"""

new = """    total_paid = payments.aggregate(total=Sum('paid_amount'))['total'] or 0
    total_expected = payments.aggregate(total=Sum('expected_amount'))['total'] or 0

    total_damage_estimated = damages.aggregate(total=Sum('estimated_cost'))['total'] or 0
    total_damage_final = damages.aggregate(total=Sum('final_cost'))['total'] or 0

    outstanding_debt = max(total_expected - total_paid, 0)
    net_profit = total_paid - total_damage_final

    collection_ratio = 0
    if total_expected > 0:
        collection_ratio = round((total_paid / total_expected) * 100, 2)

    pending_damages = damages.exclude(status='resolved').count()
"""

if old in text and "net_profit" not in text:
    text = text.replace(old, new, 1)

context_old = """        'total_expected': total_expected,
        'total_paid': total_paid,
"""

context_new = """        'total_expected': total_expected,
        'total_paid': total_paid,
        'total_damage_estimated': total_damage_estimated,
        'total_damage_final': total_damage_final,
        'outstanding_debt': outstanding_debt,
        'net_profit': net_profit,
        'collection_ratio': collection_ratio,
        'pending_damages': pending_damages,
"""

text = text.replace(context_old, context_new, 1)

p.write_text(text, encoding="utf-8")
print("OK: métricas financieras agregadas")
