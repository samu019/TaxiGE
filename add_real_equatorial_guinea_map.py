from pathlib import Path
import re

p = Path("templates/accounts/request_admin.html")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

new_map = r'''
<div class="map-box real-map-box">
    <iframe
        class="taxige-map"
        src="https://www.openstreetmap.org/export/embed.html?bbox=5.2%2C-2.2%2C12.5%2C3.9&amp;layer=mapnik&amp;marker=1.5186%2C10.3405"
        loading="lazy">
    </iframe>

    <div class="map-overlay">
        <strong>🇬🇶 Guinea Ecuatorial</strong>
        <span>Malabo · Bata · Ebibeyín · Mongomo · Evinayong</span>
    </div>
</div>
'''

text = re.sub(
    r'<div class="map-box">.*?</div>\s*</div>\s*</div>',
    new_map,
    text,
    count=1,
    flags=re.DOTALL
)

css = r'''
.real-map-box {
    position: relative !important;
    min-height: 380px !important;
    padding: 0 !important;
    overflow: hidden !important;
}

.taxige-map {
    width: 100%;
    height: 420px;
    border: 0;
    filter: saturate(1.05) contrast(1.05);
}

.map-overlay {
    position: absolute;
    left: 18px;
    bottom: 18px;
    right: 18px;
    padding: 16px;
    border-radius: 18px;
    background: rgba(15,23,42,.88);
    border: 1px solid rgba(96,165,250,.28);
    backdrop-filter: blur(12px);
}

.map-overlay strong {
    display: block;
    font-size: 20px;
    margin-bottom: 5px;
}

.map-overlay span {
    color: #cbd5e1;
    font-weight: 700;
}

@media (max-width: 768px) {
    .taxige-map {
        height: 360px;
    }

    .map-overlay {
        left: 12px;
        right: 12px;
        bottom: 12px;
    }
}
'''

if "real-map-box" not in text:
    text = text.replace("</style>", css + "\n</style>", 1)
else:
    if "taxige-map" not in text:
        text = text.replace("</style>", css + "\n</style>", 1)

p.write_text(text, encoding="utf-8")
print("Mapa real interactivo de Guinea Ecuatorial agregado.")
