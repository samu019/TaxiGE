from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

# Buscar cualquier import desde accounts.models y asegurar los 2 modelos necesarios
if "from accounts.models import" in text:
    lines = text.splitlines()
    new_lines = []
    fixed = False

    for line in lines:
        if line.startswith("from accounts.models import") and not fixed:
            needed = ["SaaSSubscription", "SaaSPaymentHistory"]
            for item in needed:
                if item not in line:
                    line = line.rstrip() + f", {item}"
            fixed = True
        new_lines.append(line)

    text = "\n".join(new_lines) + "\n"
else:
    text = "from accounts.models import SaaSSubscription, SaaSPaymentHistory\n" + text

p.write_text(text, encoding="utf-8")
print("Imports SaaS corregidos en dashboard/views.py")
