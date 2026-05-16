from pathlib import Path

base = Path("templates/dashboard/panel_base.html")
text = base.read_text(encoding="utf-8")

compact_css = r'''
/* =========================
   MOBILE COMPACT PREMIUM
========================= */

@media (max-width: 760px) {
    .topbar {
        padding: 10px 12px !important;
        min-height: auto !important;
    }

    .brand-wrap {
        gap: 8px !important;
    }

    .brand-logo {
        width: 34px !important;
        height: 34px !important;
        border-radius: 11px !important;
        font-size: 13px !important;
    }

    .brand {
        font-size: 15px !important;
    }

    .brand small {
        display: none !important;
    }

    .top-actions {
        gap: 6px !important;
    }

    .logout-btn {
        padding: 8px 9px !important;
        font-size: 12px !important;
    }

    .hamburger-btn {
        width: 34px !important;
        height: 34px !important;
        font-size: 18px !important;
        border-radius: 10px !important;
    }

    .mobile-drawer {
        top: 54px !important;
        padding: 8px 10px !important;
    }

    .mobile-drawer-card {
        border-radius: 18px !important;
        padding: 10px !important;
    }

    .mobile-drawer-card a {
        padding: 11px 12px !important;
        border-radius: 12px !important;
        font-size: 13px !important;
        margin-bottom: 7px !important;
    }

    .content {
        padding: 14px 10px 28px !important;
    }

    .content-shell {
        width: 100% !important;
    }

    .page-title {
        font-size: 23px !important;
        line-height: 1.1 !important;
        letter-spacing: -0.04em !important;
    }

    .page-subtitle {
        font-size: 13px !important;
        margin-top: 6px !important;
        margin-bottom: 14px !important;
    }

    .cards {
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 9px !important;
        margin-bottom: 12px !important;
    }

    .card {
        padding: 12px !important;
        border-radius: 15px !important;
        min-height: 86px !important;
    }

    .card h3 {
        font-size: 11px !important;
        margin-bottom: 6px !important;
        line-height: 1.25 !important;
    }

    .card strong {
        font-size: 19px !important;
        line-height: 1.15 !important;
        word-break: break-word !important;
    }

    .section {
        padding: 14px !important;
        border-radius: 16px !important;
        margin-bottom: 14px !important;
    }

    .section h2 {
        font-size: 17px !important;
        margin-bottom: 12px !important;
    }

    .chart-box {
        height: 190px !important;
    }

    .charts-grid {
        gap: 12px !important;
        margin-bottom: 14px !important;
    }

    .table-wrap {
        border-radius: 15px !important;
        overflow-x: auto !important;
        -webkit-overflow-scrolling: touch !important;
    }

    table {
        min-width: 680px !important;
        font-size: 12px !important;
    }

    th, td {
        padding: 10px 9px !important;
        font-size: 12px !important;
        white-space: nowrap !important;
    }

    .badge {
        font-size: 11px !important;
        padding: 5px 8px !important;
    }

    .btn {
        padding: 10px 12px !important;
        font-size: 12px !important;
        border-radius: 11px !important;
    }

    .btn-small {
        padding: 7px 9px !important;
        font-size: 11px !important;
        margin-bottom: 4px !important;
    }

    input, select, textarea {
        padding: 11px !important;
        border-radius: 11px !important;
        font-size: 14px !important;
    }

    .form-grid {
        gap: 12px !important;
    }

    .empty {
        padding: 14px !important;
        font-size: 13px !important;
        border-radius: 14px !important;
    }
}

@media (max-width: 430px) {
    .cards {
        grid-template-columns: 1fr 1fr !important;
    }

    .card strong {
        font-size: 17px !important;
    }

    .chart-box {
        height: 170px !important;
    }

    table {
        min-width: 620px !important;
    }
}
'''

if "MOBILE COMPACT PREMIUM" not in text:
    text = text.replace("</style>", compact_css + "\n</style>", 1)

base.write_text(text, encoding="utf-8")

home = Path("templates/dashboard/panel_home.html")
h = home.read_text(encoding="utf-8")

h = h.replace(
    "<h1 class=\"page-title\">Panel privado del dueño de taxi</h1>",
    "<h1 class=\"page-title\">Panel privado</h1>"
)

h = h.replace(
    "<p class=\"page-subtitle\">Control profesional de taxis, conductores, pagos, deudas y daños.</p>",
    "<p class=\"page-subtitle\">Resumen profesional de taxis, pagos, deudas y daños.</p>"
)

home.write_text(h, encoding="utf-8")

print("OK: panel compacto responsive móvil aplicado")
