from pathlib import Path
import re

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8")

if "from django.core.paginator import Paginator" not in text:
    text = "from django.core.paginator import Paginator\n" + text

patterns = {
    "vehicles": r"return render\(request, 'dashboard/panel_vehicles\.html', \{\s*'vehicles': vehicles,\s*\}\)",
    "drivers": r"return render\(request, 'dashboard/panel_drivers\.html', \{\s*'drivers': drivers,\s*\}\)",
    "payments": r"return render\(request, 'dashboard/panel_payments\.html', \{\s*'payments': payments,\s*\}\)",
    "damages": r"return render\(request, 'dashboard/panel_damages\.html', \{\s*'damages': damages,\s*\}\)",
}

for name, pattern in patterns.items():
    replacement = f"""paginator = Paginator({name}, 10)
    page_number = request.GET.get('page')
    {name}_page = paginator.get_page(page_number)

    return render_panel(request, 'dashboard/panel_{name}.html', {{
        '{name}': {name}_page,
    }})"""
    text = re.sub(pattern, replacement, text, count=1, flags=re.DOTALL)

p.write_text(text, encoding="utf-8")
print("Paginación aplicada a taxis, conductores, pagos y daños")
