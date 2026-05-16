from pathlib import Path

p = Path("templates/dashboard/panel_base.html")
text = p.read_text(encoding="utf-8-sig").replace("\ufeff", "")

css = r'''
/* =========================================================
   TAXIGE PRODUCTION RESPONSIVE COMPACT FINAL
   Corrige tamaño excesivo en PC, tablet y móvil
========================================================= */

@media (min-width: 1051px) {
    .layout {
        grid-template-columns: 260px minmax(0, 1fr) !important;
        gap: 14px !important;
    }

    .sidebar {
        padding: 18px !important;
    }

    .sidebar-inner {
        border-radius: 20px !important;
        padding: 14px !important;
    }

    .sidebar a {
        min-height: 42px !important;
        padding: 10px 12px !important;
        font-size: 15px !important;
    }

    .content {
        padding: 22px 24px 42px !important;
    }

    .content-shell {
        max-width: 1320px !important;
        margin: 0 auto !important;
        width: 100% !important;
    }

    .page-title {
        font-size: 30px !important;
        line-height: 1.1 !important;
    }

    .page-subtitle {
        font-size: 15px !important;
        margin-bottom: 18px !important;
    }

    .cards {
        grid-template-columns: repeat(auto-fit, minmax(190px, 1fr)) !important;
        gap: 12px !important;
        margin-bottom: 16px !important;
    }

    .card {
        padding: 15px 16px !important;
        border-radius: 18px !important;
    }

    .card h3 {
        font-size: 13px !important;
        margin-bottom: 8px !important;
    }

    .card strong {
        font-size: 24px !important;
        line-height: 1.05 !important;
    }

    .section {
        padding: 18px !important;
        border-radius: 20px !important;
        margin-bottom: 18px !important;
    }

    .section h2 {
        font-size: 20px !important;
        margin-bottom: 14px !important;
    }

    .charts-grid {
        grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
        gap: 16px !important;
        margin-bottom: 18px !important;
    }

    .chart-box {
        height: 230px !important;
    }
}

@media (max-width: 1050px) {
    .layout {
        grid-template-columns: 1fr !important;
    }

    .content {
        padding: 18px 14px 36px !important;
    }

    .content-shell {
        max-width: 100% !important;
        margin: 0 auto !important;
    }

    .cards {
        grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
        gap: 10px !important;
    }

    .card strong {
        font-size: 22px !important;
    }

    .charts-grid {
        grid-template-columns: 1fr !important;
    }

    .chart-box {
        height: 210px !important;
    }
}

@media (max-width: 560px) {
    .topbar {
        min-height: 56px !important;
        padding: 8px !important;
    }

    .brand {
        font-size: 15px !important;
    }

    .brand small {
        display: none !important;
    }

    .user-pill {
        display: none !important;
    }

    .content {
        padding: 14px 10px 28px !important;
    }

    .page-title {
        font-size: 24px !important;
    }

    .page-subtitle {
        font-size: 13px !important;
    }

    .cards {
        grid-template-columns: 1fr !important;
        gap: 9px !important;
    }

    .card {
        padding: 13px !important;
        border-radius: 16px !important;
    }

    .card h3 {
        font-size: 12px !important;
    }

    .card strong {
        font-size: 21px !important;
    }

    .section {
        padding: 14px !important;
        border-radius: 16px !important;
    }

    .section h2 {
        font-size: 18px !important;
    }

    .chart-box {
        height: 180px !important;
    }

    table {
        min-width: 620px !important;
    }
}
'''

if "TAXIGE PRODUCTION RESPONSIVE COMPACT FINAL" not in text:
    text = text.replace("</style>", css + "\n</style>", 1)

p.write_text(text, encoding="utf-8")
print("OK: responsive compacto final aplicado")
