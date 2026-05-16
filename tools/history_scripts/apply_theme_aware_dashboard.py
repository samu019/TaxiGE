from pathlib import Path
import re

p = Path("templates/dashboard/panel_home.html")
text = p.read_text(encoding="utf-8-sig").replace("\ufeff", "")

# Reemplazar fondos blancos por variables del tema actual
replacements = {
    "background: linear-gradient(180deg, rgba(255,255,255,.98), rgba(248,250,252,.96));":
        "background: var(--card-bg, rgba(15,23,42,.92));",

    "background: rgba(255,255,255,.92);":
        "background: var(--card-bg, rgba(15,23,42,.92));",

    "background: rgba(255,255,255,.96);":
        "background: var(--card-bg, rgba(15,23,42,.92));",

    "border: 1px solid rgba(148,163,184,.35);":
        "border: 1px solid var(--card-border, rgba(148,163,184,.20));",

    "color: #020617;":
        "color: var(--text-primary, #f8fafc);",

    "color: #475569;":
        "color: var(--text-secondary, #cbd5e1);",

    "color: #64748b;":
        "color: var(--text-muted, #94a3b8);",

    "background: #f1f5f9;":
        "background: var(--surface-soft, rgba(255,255,255,.08));",

    "color: #0f172a;":
        "color: var(--text-primary, #f8fafc);",

    "border: 1px solid #cbd5e1;":
        "border: 1px solid var(--card-border, rgba(148,163,184,.20));",

    "background: linear-gradient(135deg, #f59e0b, #facc15);":
        "background: linear-gradient(135deg, #f59e0b, #facc15); color: #111827;",
}

for old, new in replacements.items():
    text = text.replace(old, new)

# Ajustar tablas y textos vacíos para respetar el tema
if ".table-wrap {" in text and ".empty {" not in text:
    text = text.replace(
        ".table-wrap {\n    overflow-x: auto;\n}",
        """.table-wrap {
    overflow-x: auto;
}

.table-wrap table {
    width: 100%;
}

.empty {
    color: var(--text-muted, #94a3b8);
    font-weight: 700;
}"""
    )

p.write_text(text, encoding="utf-8")
print("OK: dashboard adaptado al tema oscuro/claro")
