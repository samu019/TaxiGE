from pathlib import Path

p = Path("templates/dashboard/panel_base.html")
text = p.read_text(encoding="utf-8")

css = r'''
/* =========================
   FORCE HAMBURGER ALL SCREENS
========================= */

.hamburger-btn {
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    flex: 0 0 auto !important;
    width: 42px !important;
    height: 42px !important;
    border-radius: 14px !important;
    background: rgba(255,255,255,.12) !important;
    color: #ffffff !important;
    border: 1px solid rgba(255,255,255,.16) !important;
    font-size: 22px !important;
    font-weight: 900 !important;
    cursor: pointer !important;
}

.mobile-drawer {
    display: none !important;
    position: fixed !important;
    top: 72px !important;
    left: 18px !important;
    width: min(330px, calc(100vw - 36px)) !important;
    max-width: calc(100vw - 36px) !important;
    height: auto !important;
    max-height: calc(100vh - 92px) !important;
    overflow-y: auto !important;
    z-index: 9999 !important;
    padding: 0 !important;
    background: transparent !important;
    border: 0 !important;
}

.mobile-drawer.open {
    display: block !important;
}

.mobile-drawer-card {
    background: #ffffff !important;
    border: 1px solid #e2e8f0 !important;
    border-radius: 22px !important;
    padding: 12px !important;
    box-shadow: 0 24px 70px rgba(2,6,23,.28) !important;
}

.mobile-drawer-card a {
    display: block !important;
    padding: 13px 14px !important;
    margin-bottom: 8px !important;
    border-radius: 14px !important;
    color: #0f172a !important;
    font-weight: 900 !important;
    background: #f8fafc !important;
    border: 1px solid #e2e8f0 !important;
}

.mobile-drawer-card a.active {
    background: linear-gradient(135deg, #f59e0b, #facc15) !important;
    color: #111827 !important;
    border-color: transparent !important;
}

body.dark-mode .mobile-drawer-card {
    background: #0f172a !important;
    border-color: #334155 !important;
}

body.dark-mode .mobile-drawer-card a {
    background: #1e293b !important;
    color: #f8fafc !important;
    border-color: #334155 !important;
}

body.dark-mode .mobile-drawer-card a.active {
    background: linear-gradient(135deg, #f59e0b, #facc15) !important;
    color: #111827 !important;
}

@media (max-width: 760px) {
    .hamburger-btn {
        width: 34px !important;
        height: 34px !important;
        font-size: 18px !important;
        border-radius: 11px !important;
    }

    .mobile-drawer {
        top: 58px !important;
        left: 10px !important;
        width: calc(100vw - 20px) !important;
        max-width: calc(100vw - 20px) !important;
    }
}
'''

if "FORCE HAMBURGER ALL SCREENS" not in text:
    text = text.replace("</style>", css + "\n</style>", 1)

p.write_text(text, encoding="utf-8")
print("OK: hamburguesa forzada en todas las pantallas")
