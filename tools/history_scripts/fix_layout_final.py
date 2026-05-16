from pathlib import Path

p = Path("templates/dashboard/panel_base.html")
text = p.read_text(encoding="utf-8")

css = r'''
/* =========================
   FINAL LAYOUT FIX TAXIGE
========================= */

html, body {
    width: 100%;
    max-width: 100%;
    overflow-x: hidden !important;
}

body {
    min-width: 0 !important;
}

.topbar {
    width: 100%;
}

.layout {
    width: 100%;
    max-width: 100%;
    overflow-x: hidden;
}

.content {
    min-width: 0 !important;
    width: 100% !important;
    overflow-x: hidden !important;
}

.content-shell {
    max-width: 1180px !important;
    width: 100% !important;
    margin: 0 auto !important;
    min-width: 0 !important;
}

.cards {
    width: 100%;
    min-width: 0;
}

.card,
.section,
.table-wrap,
.charts-grid,
.chart-box {
    min-width: 0 !important;
    max-width: 100% !important;
}

.charts-grid {
    display: grid !important;
    grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
    gap: 20px !important;
    width: 100% !important;
}

.chart-box {
    height: 230px !important;
    overflow: hidden !important;
}

.chart-box canvas {
    max-width: 100% !important;
    max-height: 100% !important;
}

.table-wrap {
    width: 100%;
    overflow-x: auto !important;
}

table {
    width: 100%;
}

@media (min-width: 1051px) {
    .layout {
        grid-template-columns: 300px minmax(0, 1fr) !important;
    }

    .sidebar {
        width: 300px !important;
    }

    .content {
        padding: 28px 28px 50px !important;
    }

    .cards {
        grid-template-columns: repeat(5, minmax(0, 1fr)) !important;
    }
}

@media (max-width: 1280px) {
    .cards {
        grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
    }

    .charts-grid {
        grid-template-columns: 1fr !important;
    }
}

@media (max-width: 900px) {
    .layout {
        grid-template-columns: 1fr !important;
    }

    .content {
        padding: 16px 12px 34px !important;
    }

    .cards {
        grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
    }

    .chart-box {
        height: 190px !important;
    }
}

@media (max-width: 430px) {
    .cards {
        grid-template-columns: 1fr !important;
    }

    .chart-box {
        height: 165px !important;
    }
}
'''

if "FINAL LAYOUT FIX TAXIGE" not in text:
    text = text.replace("</style>", css + "\n</style>", 1)

p.write_text(text, encoding="utf-8")
print("OK: layout final corregido")
