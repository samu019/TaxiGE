from pathlib import Path

p = Path("templates/dashboard/panel_base.html")
text = p.read_text(encoding="utf-8")

css = r'''
/* =========================================================
   TAXIGE ULTRA WIDE DESKTOP LAYOUT
   Aprovecha todo el ancho del monitor profesionalmente
========================================================= */

.content-shell {
    max-width: 100% !important;
    width: 100% !important;
    margin: 0 !important;
    padding: 0 !important;
}

@media (min-width: 1051px) {
    .layout {
        grid-template-columns: 300px minmax(0, 1fr) !important;
        gap: 24px !important;
    }

    .content {
        width: 100% !important;
        max-width: 100% !important;
        padding: 24px 32px 48px !important;
        overflow-x: hidden !important;
    }

    .content-shell {
        max-width: 100% !important;
        width: 100% !important;
    }

    .page-head,
    .cards,
    .charts-grid,
    .section,
    .table-wrap {
        width: 100% !important;
        max-width: 100% !important;
    }

    .cards {
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)) !important;
        gap: 18px !important;
    }

    .charts-grid {
        grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
        gap: 24px !important;
    }

    .chart-box {
        height: 320px !important;
    }

    .page-head {
        display: flex !important;
        justify-content: space-between !important;
        align-items: flex-start !important;
        gap: 20px !important;
        flex-wrap: wrap !important;
    }

    .page-actions,
    .actions,
    .header-actions {
        display: flex !important;
        flex-wrap: wrap !important;
        justify-content: flex-end !important;
        gap: 12px !important;
    }

    .btn,
    .btn-primary,
    .btn-secondary {
        white-space: nowrap !important;
    }

    .table-wrap {
        overflow-x: auto !important;
    }

    table {
        width: 100% !important;
    }
}
'''

if "TAXIGE ULTRA WIDE DESKTOP LAYOUT" not in text:
    text = text.replace("</style>", css + "\n</style>", 1)

p.write_text(text, encoding="utf-8")
print("OK: layout ultra wide aplicado")
