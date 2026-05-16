from pathlib import Path

p = Path("templates/dashboard/panel_base.html")
text = p.read_text(encoding="utf-8")

css = r'''
/* =========================
   PROFESSIONAL ACTION BAR
========================= */

.page-head {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 18px;
    margin-bottom: 22px;
    width: 100%;
}

.page-head-text {
    min-width: 0;
}

.page-actions {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    gap: 10px;
    flex-wrap: wrap;
}

.page-actions .btn {
    min-height: 46px;
}

@media (max-width: 760px) {
    .page-head {
        flex-direction: column;
        gap: 12px;
    }

    .page-actions {
        width: 100%;
        justify-content: flex-start;
        display: grid;
        grid-template-columns: 1fr;
        gap: 8px;
    }

    .page-actions .btn {
        width: 100%;
    }
}
'''

if "PROFESSIONAL ACTION BAR" not in text:
    text = text.replace("</style>", css + "\n</style>", 1)

p.write_text(text, encoding="utf-8")
print("OK: CSS action bar agregado")
