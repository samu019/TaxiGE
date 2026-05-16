from pathlib import Path

files = [
    "dashboard/views.py",
    "templates/dashboard/panel_home.html",
]

for file in files:
    p = Path(file)
    text = p.read_text(encoding="utf-8-sig").replace("\ufeff", "")
    lines = text.splitlines()

    print("\n" + "="*80)
    print("ARCHIVO:", file)
    print("="*80)

    keywords = [
        "def panel_home",
        "total_expected",
        "total_paid",
        "total_debt",
        "damages_cost",
        "net_profit",
        "collection_rate",
        "recent_payments",
        "recent_damages",
        "Dashboard ejecutivo",
        "cards",
        "financeChart",
        "operationChart",
        "Chart",
    ]

    for key in keywords:
        for i, line in enumerate(lines, start=1):
            if key in line:
                start = max(1, i - 4)
                end = min(len(lines), i + 8)
                print(f"\n--- {key} línea {i} ---")
                for n in range(start, end + 1):
                    print(f"{n}: {lines[n-1]}")
                print("-"*60)
