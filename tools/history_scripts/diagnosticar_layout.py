from pathlib import Path
import re

files = [
    "templates/dashboard/panel_base.html",
    "templates/dashboard/panel_home.html",
]

for file in files:
    p = Path(file)
    text = p.read_text(encoding="utf-8")
    lines = text.splitlines()

    print("\n" + "="*80)
    print("ARCHIVO:", file)
    print("LINEAS:", len(lines))
    print("="*80)

    checks = [
        "layout",
        "content-shell",
        "cards",
        "charts-grid",
        "chart-box",
        "canvas",
        "overflow-x",
        "grid-template-columns",
        "min-width",
        "max-width",
        "FINAL LAYOUT FIX",
        "RESPONSIVE FINAL",
        "MOBILE COMPACT",
        "HAMBURGER",
    ]

    for key in checks:
        print(f"\n--- {key} ---")
        found = False

        for i, line in enumerate(lines, start=1):
            if key in line:
                found = True
                start = max(1, i - 3)
                end = min(len(lines), i + 8)

                print(f"\nLínea {i}:")
                for n in range(start, end + 1):
                    print(f"{n}: {lines[n-1]}")
                print("-"*60)

        if not found:
            print("NO ENCONTRADO")

print("\nDIAGNOSTICO FINALIZADO")
