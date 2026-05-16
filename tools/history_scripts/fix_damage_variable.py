from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8-sig").replace("\ufeff", "")

text = text.replace("total_damage_estimated", "damages_cost")

p.write_text(text, encoding="utf-8")
print("OK: total_damage_estimated reemplazado por damages_cost")
