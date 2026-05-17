from pathlib import Path

p = Path("templates/accounts/request_admin.html")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

# Forzar iframe grande con estilo inline
text = text.replace(
    '<iframe\n        class="taxige-map"',
    '<iframe\n        class="taxige-map"\n        style="width:100% !important; height:520px !important; display:block !important; border:0 !important;"',
)

# CSS final que gana a todos los estilos anteriores
force_css = r'''
/* FORCE REAL MAP FULL SIZE */
.map-box.real-map-box,
.real-map-box {
    display: block !important;
    width: 100% !important;
    min-height: 520px !important;
    height: auto !important;
    padding: 0 !important;
    overflow: hidden !important;
    border-radius: 28px !important;
}

.map-box.real-map-box iframe,
.real-map-box iframe,
.taxige-map {
    width: 100% !important;
    min-width: 100% !important;
    height: 520px !important;
    min-height: 520px !important;
    display: block !important;
    border: 0 !important;
}

@media (max-width: 768px) {
    .map-box.real-map-box,
    .real-map-box {
        min-height: 420px !important;
    }

    .map-box.real-map-box iframe,
    .real-map-box iframe,
    .taxige-map {
        height: 420px !important;
        min-height: 420px !important;
    }
}
'''

if "FORCE REAL MAP FULL SIZE" not in text:
    text = text.replace("</style>", force_css + "\n</style>", 1)

p.write_text(text, encoding="utf-8")
print("Mapa forzado a tamaño completo.")
