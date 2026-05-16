from pathlib import Path

p = Path("templates/dashboard/panel_base.html")
text = p.read_text(encoding="utf-8")

css = r'''
/* =========================
   TOPBAR OVERFLOW FIX
========================= */

.topbar {
    max-width: 100vw !important;
    overflow: hidden !important;
}

.brand-wrap {
    min-width: 0 !important;
    flex: 1 1 auto !important;
    overflow: hidden !important;
}

.brand {
    min-width: 0 !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
}

.top-actions {
    flex: 0 0 auto !important;
    min-width: 0 !important;
}

@media (max-width: 760px) {
    .topbar {
        gap: 6px !important;
        padding: 8px 8px !important;
    }

    .brand-logo {
        width: 32px !important;
        height: 32px !important;
        border-radius: 10px !important;
        font-size: 12px !important;
    }

    .hamburger-btn {
        width: 32px !important;
        height: 32px !important;
        font-size: 18px !important;
        border-radius: 10px !important;
        flex: 0 0 auto !important;
    }

    .brand {
        font-size: 14px !important;
        max-width: 145px !important;
        white-space: nowrap !important;
    }

    .top-actions {
        gap: 5px !important;
    }

    .logout-btn {
        padding: 7px 8px !important;
        font-size: 11px !important;
        border-radius: 999px !important;
    }

    #themeToggle {
        width: 32px !important;
        height: 32px !important;
        padding: 0 !important;
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
}

@media (max-width: 390px) {
    .brand {
        max-width: 105px !important;
    }

    .logout-main {
        padding: 7px 7px !important;
    }
}
'''

if "TOPBAR OVERFLOW FIX" not in text:
    text = text.replace("</style>", css + "\n</style>", 1)

p.write_text(text, encoding="utf-8")
print("OK: topbar corregida para no salirse de pantalla")
