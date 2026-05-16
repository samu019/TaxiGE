from pathlib import Path

p = Path("templates/dashboard/panel_base.html")
text = p.read_text(encoding="utf-8")

keywords = [
    "topbar",
    "hamburger-btn",
    "mobile-drawer",
    "mobile-nav",
    "sidebar",
    "MOBILE COMPACT PREMIUM",
    "HAMBURGER MOBILE MENU",
    "DOMContentLoaded",
]

print("\n===== REVISION PANEL_BASE.HTML =====\n")

for key in keywords:
    print(f"\n--- BUSCANDO: {key} ---")
    lines = text.splitlines()
    found = False

    for i, line in enumerate(lines, start=1):
        if key in line:
            found = True
            start = max(1, i - 5)
            end = min(len(lines), i + 12)

            print(f"\nLINEA {i}:")
            for n in range(start, end + 1):
                print(f"{n}: {lines[n-1]}")
            print("-" * 60)

    if not found:
        print("NO ENCONTRADO")

print("\n===== FIN REVISION =====")
