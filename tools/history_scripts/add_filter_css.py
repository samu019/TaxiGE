from pathlib import Path

p = Path("templates/dashboard/panel_base.html")
text = p.read_text(encoding="utf-8")

css = r'''
/* =========================
   PROFESSIONAL FILTER BAR
========================= */

.filter-bar {
    display: grid;
    grid-template-columns: 1fr 220px auto auto;
    gap: 10px;
    align-items: center;
    margin-bottom: 18px;
    background: rgba(255,255,255,.86);
    border: 1px solid var(--border);
    border-radius: 18px;
    padding: 12px;
    box-shadow: var(--shadow);
}

.filter-bar input,
.filter-bar select {
    height: 46px;
}

body.dark-mode .filter-bar {
    background: rgba(15,23,42,.96);
    border-color: #334155;
}

@media(max-width: 760px) {
    .filter-bar {
        grid-template-columns: 1fr;
        padding: 10px;
    }

    .filter-bar .btn {
        width: 100%;
    }
}
'''

if "PROFESSIONAL FILTER BAR" not in text:
    text = text.replace("</style>", css + "\n</style>", 1)

p.write_text(text, encoding="utf-8")
print("OK: CSS filtros agregado")
