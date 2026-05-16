from pathlib import Path
import re

p = Path("templates/dashboard/panel_base.html")
text = p.read_text(encoding="utf-8")

# 1. Eliminar el nav móvil horizontal antiguo completo
text = re.sub(
    r'\n<nav class="mobile-nav">.*?</nav>\n',
    '\n',
    text,
    flags=re.DOTALL
)

# 2. Reglas finales responsive limpias
final_css = r'''
/* =========================
   RESPONSIVE FINAL TAXIGE
========================= */

/* PC grande: sidebar visible, sin hamburguesa */
@media (min-width: 1051px) {
    .hamburger-btn {
        display: none !important;
    }

    .mobile-drawer {
        display: none !important;
    }

    .layout {
        grid-template-columns: 280px 1fr !important;
    }

    .sidebar {
        display: block !important;
    }
}

/* Tablet y móvil: sidebar oculto, hamburguesa visible */
@media (max-width: 1050px) {
    .hamburger-btn {
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
    }

    .sidebar {
        display: none !important;
    }

    .layout {
        grid-template-columns: 1fr !important;
    }

    .mobile-drawer {
        display: none !important;
    }

    .mobile-drawer.open {
        display: block !important;
    }
}

/* Móvil compacto */
@media (max-width: 760px) {
    .topbar {
        padding: 10px 12px !important;
    }

    .content {
        padding: 14px 10px 28px !important;
    }

    .cards {
        grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
        gap: 9px !important;
    }

    .card {
        padding: 12px !important;
        border-radius: 15px !important;
    }

    .card strong {
        font-size: 18px !important;
    }

    .chart-box {
        height: 175px !important;
    }
}

/* Teléfonos muy pequeños */
@media (max-width: 390px) {
    .cards {
        grid-template-columns: 1fr !important;
    }

    .top-actions {
        gap: 4px !important;
    }

    .logout-btn {
        padding: 7px 8px !important;
    }
}
'''

if "RESPONSIVE FINAL TAXIGE" not in text:
    text = text.replace("</style>", final_css + "\n</style>", 1)

p.write_text(text, encoding="utf-8")
print("OK: responsive final aplicado. Menú mobile-nav eliminado y hamburguesa limpia.")
