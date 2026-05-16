from pathlib import Path

files = [
    "templates/dashboard/panel_vehicles.html",
    "templates/dashboard/panel_drivers.html",
    "templates/dashboard/panel_payments.html",
    "templates/dashboard/panel_damages.html",
    "dashboard/urls.py",
    "dashboard/views.py",
]

for file in files:
    p = Path(file)
    print("\n" + "="*80)
    print("ARCHIVO:", file)
    print("="*80)

    text = p.read_text(encoding="utf-8-sig").replace("\ufeff", "")
    lines = text.splitlines()

    keywords = [
        "page-head",
        "page-actions",
        "Exportar CSV",
        "Exportar PDF",
        "reports/",
        "export_vehicles_pdf",
        "export_drivers_pdf",
        "export_payments_pdf",
        "export_damages_pdf",
        "export_vehicles_csv",
        "export_drivers_csv",
        "export_payments_csv",
        "export_damages_csv",
    ]

    for key in keywords:
        found = False
        for i, line in enumerate(lines, start=1):
            if key in line:
                found = True
                start = max(1, i - 3)
                end = min(len(lines), i + 5)
                print(f"\n--- {key} línea {i} ---")
                for n in range(start, end + 1):
                    print(f"{n}: {lines[n-1]}")
        if not found:
            pass
