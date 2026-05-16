from pathlib import Path

p = Path("templates/dashboard/panel_base.html")
text = p.read_text(encoding="utf-8")

# Añadir overlay si no existe
if 'drawerOverlay' not in text:
    text = text.replace(
        '<div class="mobile-drawer" id="mobileDrawer">',
        '<div class="drawer-overlay" id="drawerOverlay"></div>\n\n<div class="mobile-drawer" id="mobileDrawer">',
        1
    )

css = r'''
/* =========================
   PROFESSIONAL DRAWER MENU
========================= */

.drawer-overlay {
    display: none;
    position: fixed;
    inset: 0;
    background: rgba(2, 6, 23, .42);
    backdrop-filter: blur(2px);
    z-index: 9998;
}

.drawer-overlay.open {
    display: block;
}

.mobile-drawer {
    animation: drawerIn .18s ease-out;
}

@keyframes drawerIn {
    from {
        opacity: 0;
        transform: translateY(-8px) scale(.98);
    }
    to {
        opacity: 1;
        transform: translateY(0) scale(1);
    }
}

.mobile-drawer-card::before {
    content: "Navegación rápida";
    display: block;
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: .08em;
    color: #64748b;
    font-weight: 900;
    padding: 6px 8px 12px;
}

body.dark-mode .mobile-drawer-card::before {
    color: #94a3b8;
}

.hamburger-btn {
    transition: transform .16s ease, background .16s ease;
}

.hamburger-btn:hover {
    transform: translateY(-1px);
    background: rgba(255,255,255,.18) !important;
}

.hamburger-btn:active {
    transform: scale(.96);
}

@media (min-width: 1051px) {
    .mobile-drawer {
        left: 24px !important;
        top: 78px !important;
    }
}
'''

if "PROFESSIONAL DRAWER MENU" not in text:
    text = text.replace("</style>", css + "\n</style>", 1)

old_js = """    const hamburgerBtn = document.getElementById('hamburgerBtn');
    const mobileDrawer = document.getElementById('mobileDrawer');

    if (hamburgerBtn && mobileDrawer) {
        hamburgerBtn.addEventListener('click', function () {
            mobileDrawer.classList.toggle('open');
            hamburgerBtn.innerHTML = mobileDrawer.classList.contains('open') ? '×' : '☰';
        });

        mobileDrawer.querySelectorAll('a').forEach(function (link) {
            link.addEventListener('click', function () {
                mobileDrawer.classList.remove('open');
                hamburgerBtn.innerHTML = '☰';
            });
        });
    }"""

new_js = """    const hamburgerBtn = document.getElementById('hamburgerBtn');
    const mobileDrawer = document.getElementById('mobileDrawer');
    const drawerOverlay = document.getElementById('drawerOverlay');

    function openDrawer() {
        if (!mobileDrawer) return;
        mobileDrawer.classList.add('open');
        if (drawerOverlay) drawerOverlay.classList.add('open');
        if (hamburgerBtn) hamburgerBtn.innerHTML = '×';
    }

    function closeDrawer() {
        if (!mobileDrawer) return;
        mobileDrawer.classList.remove('open');
        if (drawerOverlay) drawerOverlay.classList.remove('open');
        if (hamburgerBtn) hamburgerBtn.innerHTML = '☰';
    }

    if (hamburgerBtn && mobileDrawer) {
        hamburgerBtn.addEventListener('click', function () {
            if (mobileDrawer.classList.contains('open')) {
                closeDrawer();
            } else {
                openDrawer();
            }
        });

        if (drawerOverlay) {
            drawerOverlay.addEventListener('click', closeDrawer);
        }

        document.addEventListener('keydown', function (event) {
            if (event.key === 'Escape') {
                closeDrawer();
            }
        });

        mobileDrawer.querySelectorAll('a').forEach(function (link) {
            link.addEventListener('click', closeDrawer);
        });
    }"""

if old_js in text:
    text = text.replace(old_js, new_js, 1)
else:
    print("AVISO: no encontré el JS exacto. Si el menú abre igual, no pasa nada.")

p.write_text(text, encoding="utf-8")
print("OK: menú hamburguesa profesional final aplicado")
