from pathlib import Path

p = Path("templates/dashboard/panel_base.html")
text = p.read_text(encoding="utf-8")

# Botón hamburguesa junto al logo
text = text.replace(
    '<div class="brand-wrap">',
    '<div class="brand-wrap">\n        <button class="hamburger-btn" id="hamburgerBtn" type="button">☰</button>',
    1
)

# Menú móvil desplegable
mobile_menu = r'''
<div class="mobile-drawer" id="mobileDrawer">
    <div class="mobile-drawer-card">
        <a href="/panel/" class="{% if request.path == '/panel/' %}active{% endif %}">Panel principal</a>
        <a href="/panel/vehicles/" class="{% if '/panel/vehicles/' in request.path %}active{% endif %}">Mis taxis</a>
        <a href="/panel/drivers/" class="{% if '/panel/drivers/' in request.path %}active{% endif %}">Mis conductores</a>
        <a href="/panel/payments/" class="{% if '/panel/payments/' in request.path %}active{% endif %}">Pagos</a>
        <a href="/panel/damages/" class="{% if '/panel/damages/' in request.path %}active{% endif %}">Daños</a>
        <a href="/accounts/logout/">Cerrar sesión</a>
    </div>
</div>
'''

if 'mobile-drawer' not in text:
    text = text.replace('</div>\n\n<nav class="mobile-nav">', '</div>\n' + mobile_menu + '\n<nav class="mobile-nav">', 1)

# CSS
css = r'''
/* =========================
   HAMBURGER MOBILE MENU
========================= */

.hamburger-btn {
    display: none;
    width: 42px;
    height: 42px;
    border: 0;
    border-radius: 14px;
    background: rgba(255,255,255,0.10);
    color: white;
    font-size: 22px;
    font-weight: 900;
    cursor: pointer;
}

.mobile-drawer {
    display: none;
}

.mobile-drawer-card a {
    display: block;
    color: #111827;
    text-decoration: none;
    background: white;
    border: 1px solid #e5e7eb;
    padding: 14px 16px;
    border-radius: 14px;
    font-weight: 900;
    margin-bottom: 10px;
}

.mobile-drawer-card a.active {
    background: #111827;
    color: white;
    border-color: #111827;
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

@media (max-width: 1050px) {
    .hamburger-btn {
        display: inline-flex;
        align-items: center;
        justify-content: center;
    }

    .mobile-nav {
        display: none !important;
    }

    .mobile-drawer {
        display: none;
        padding: 12px 14px;
        background: rgba(255,255,255,0.86);
        border-bottom: 1px solid #e5e7eb;
        position: sticky;
        top: 74px;
        z-index: 16;
    }

    .mobile-drawer.open {
        display: block;
    }

    .mobile-drawer-card {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 22px;
        padding: 14px;
        box-shadow: 0 18px 45px rgba(15, 23, 42, 0.12);
    }
}

@media (max-width: 640px) {
    .hamburger-btn {
        width: 38px;
        height: 38px;
        border-radius: 12px;
        font-size: 20px;
    }
}
'''

if 'HAMBURGER MOBILE MENU' not in text:
    text = text.replace('</style>', css + '\n</style>', 1)

# JS
js = r'''
<script>
document.addEventListener('DOMContentLoaded', function () {
    const hamburgerBtn = document.getElementById('hamburgerBtn');
    const mobileDrawer = document.getElementById('mobileDrawer');

    if (hamburgerBtn && mobileDrawer) {
        hamburgerBtn.addEventListener('click', function () {
            mobileDrawer.classList.toggle('open');
            hamburgerBtn.innerHTML = mobileDrawer.classList.contains('open') ? '×' : '☰';
        });
    }
});
</script>
'''

if 'hamburgerBtn' in text and 'mobileDrawer.classList.toggle' not in text:
    text = text.replace('</body>', js + '\n</body>', 1)

p.write_text(text, encoding="utf-8")
print("OK: menú hamburguesa agregado")
