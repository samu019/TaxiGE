from pathlib import Path

p = Path("templates/dashboard/panel_base.html")
text = p.read_text(encoding="utf-8")

old = '<a class="logout-btn" href="/accounts/logout/">Salir</a>'
new = '''
<button id="themeToggle" class="logout-btn" type="button" style="background:#334155;color:white;">
    🌙
</button>

<a class="logout-btn" href="/accounts/logout/">Salir</a>
'''

if old not in text:
    print("AVISO: no se encontró el botón Salir exacto, puede que ya esté cambiado.")
else:
    text = text.replace(old, new, 1)

dark_css = r'''
/* =========================
   DARK MODE PREMIUM
========================= */

body.dark-mode {
    background:
        radial-gradient(circle at top left, rgba(245, 158, 11, 0.10), transparent 28%),
        linear-gradient(180deg, #020617 0%, #0f172a 45%, #111827 100%) !important;
    color: #f8fafc !important;
}

body.dark-mode .topbar {
    background: rgba(2, 6, 23, 0.98) !important;
    border-bottom: 1px solid #1e293b;
}

body.dark-mode .sidebar-inner,
body.dark-mode .card,
body.dark-mode .section,
body.dark-mode .table-wrap,
body.dark-mode table,
body.dark-mode .mobile-nav,
body.dark-mode .mobile-nav a {
    background: rgba(15, 23, 42, 0.96) !important;
    color: #f8fafc !important;
    border-color: #334155 !important;
}

body.dark-mode th {
    background: #020617 !important;
    color: #cbd5e1 !important;
}

body.dark-mode td {
    color: #f8fafc !important;
    border-color: #334155 !important;
}

body.dark-mode tr:hover td {
    background: #1e293b !important;
}

body.dark-mode .page-title,
body.dark-mode .section h2,
body.dark-mode h1,
body.dark-mode h2,
body.dark-mode h3,
body.dark-mode strong,
body.dark-mode label {
    color: #ffffff !important;
}

body.dark-mode .page-subtitle,
body.dark-mode .nav-label {
    color: #94a3b8 !important;
}

body.dark-mode .sidebar a,
body.dark-mode .mobile-nav a {
    color: #f8fafc !important;
}

body.dark-mode .sidebar a:hover {
    background: #1e293b !important;
}

body.dark-mode .sidebar a.active,
body.dark-mode .mobile-nav a.active {
    background: linear-gradient(135deg, #f59e0b, #facc15) !important;
    color: #111827 !important;
}

body.dark-mode input,
body.dark-mode select,
body.dark-mode textarea {
    background: #020617 !important;
    color: #ffffff !important;
    border-color: #334155 !important;
}

body.dark-mode .badge {
    background: #334155 !important;
    color: #ffffff !important;
}

body.dark-mode .empty {
    background: #0f172a !important;
    color: #cbd5e1 !important;
    border-color: #475569 !important;
}

body.dark-mode .user-pill {
    background: #111827 !important;
    border-color: #334155 !important;
}

body.dark-mode .btn-secondary {
    background: #334155 !important;
    color: #ffffff !important;
}
'''

if "DARK MODE PREMIUM" not in text:
    text = text.replace("</style>", dark_css + "\n</style>")
else:
    print("AVISO: CSS dark mode ya existe.")

dark_js = r'''
<script>
document.addEventListener('DOMContentLoaded', function () {
    const body = document.body;
    const toggle = document.getElementById('themeToggle');

    const savedTheme = localStorage.getItem('taxige-theme');

    if (savedTheme === 'dark') {
        body.classList.add('dark-mode');
        if (toggle) toggle.innerHTML = '☀️';
    }

    if (toggle) {
        toggle.addEventListener('click', function () {
            body.classList.toggle('dark-mode');

            if (body.classList.contains('dark-mode')) {
                localStorage.setItem('taxige-theme', 'dark');
                toggle.innerHTML = '☀️';
            } else {
                localStorage.setItem('taxige-theme', 'light');
                toggle.innerHTML = '🌙';
            }
        });
    }
});
</script>
'''

if "taxige-theme" not in text:
    text = text.replace("</body>", dark_js + "\n</body>")
else:
    print("AVISO: JS dark mode ya existe.")

p.write_text(text, encoding="utf-8")
print("OK: modo oscuro premium agregado a panel_base.html")
