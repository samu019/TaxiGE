from pathlib import Path

files = [
    "templates/dashboard/panel_base.html",
    "templates/dashboard/panel_home.html",
]

keywords = [
    ".topbar",
    ".layout",
    ".sidebar",
    ".content",
    ".content-shell",
    ".page-title",
    ".page-subtitle",
    ".cards",
    ".card",
    ".section",
    ".charts-grid",
    ".chart-box",
    "@media",
    "ULTRA WIDE",
    "MOBILE",
    "RESPONSIVE",
]

for file in files:
    p = Path(file)
    text = p.read_text(encoding="utf-8-sig").replace("\ufeff", "")
    lines = text.splitlines()

    print("\n" + "="*90)
    print("ARCHIVO:", file)
    print("LINEAS:", len(lines))
    print("="*90)

    for key in keywords:
        found = False
        for i, line in enumerate(lines, start=1):
            if key in line:
                found = True
                start = max(1, i - 5)
                end = min(len(lines), i + 14)

                print(f"\n--- {key} línea {i} ---")
                for n in range(start, end + 1):
                    print(f"{n}: {lines[n-1]}")
                print("-" * 70)

        if not found:
            pass
