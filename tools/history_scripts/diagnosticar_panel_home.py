from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8-sig").replace("\ufeff", "")
lines = text.splitlines()

keywords = [
    "def panel_home",
    "total_expected",
    "total_paid",
    "total_debt",
    "damages_cost",
    "total_damage_final",
    "total_damage_estimated",
    "net_profit",
    "collection_rate",
    "context =",
    "return render",
]

print("\n===== DIAGNÓSTICO dashboard/views.py =====\n")

for key in keywords:
    print(f"\n--- BUSCANDO: {key} ---")
    found = False

    for i, line in enumerate(lines, start=1):
        if key in line:
            found = True
            start = max(1, i - 8)
            end = min(len(lines), i + 12)

            print(f"\nLÍNEA {i}:")
            for n in range(start, end + 1):
                print(f"{n}: {lines[n-1]}")
            print("-" * 70)

    if not found:
        print("NO ENCONTRADO")

print("\n===== FIN DIAGNÓSTICO =====")
