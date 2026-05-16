from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8-sig").replace("\ufeff", "")

if "from decimal import Decimal" not in text:
    text = "from decimal import Decimal\n" + text

# Insertar cálculo seguro si no existe
if "collection_rate" not in text:
    text = text.replace(
        "total_debt = total_expected - total_paid",
        """total_debt = total_expected - total_paid
    damages_cost = damages.aggregate(total=Sum('estimated_cost'))['total'] or Decimal('0')
    net_profit = total_paid - damages_cost

    if total_expected > 0:
        collection_rate = round((total_paid / total_expected) * 100, 2)
    else:
        collection_rate = Decimal('0')"""
    )

# Añadir variables al context si faltan
text = text.replace(
    "'total_debt': total_debt,",
    """'total_debt': total_debt,
        'damages_cost': damages_cost,
        'net_profit': net_profit,
        'collection_rate': collection_rate,"""
)

p.write_text(text, encoding="utf-8")
print("OK: métricas financieras agregadas")
