from pathlib import Path

p = Path("templates/accounts/request_admin.html")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

# Reemplazar el CSS del mapa por una versión más grande y premium
import re

pattern = r"\.real-map-box\s*\{.*?\}\s*\.taxige-map\s*\{.*?\}\s*\.map-overlay\s*\{.*?\}\s*\.map-overlay strong\s*\{.*?\}\s*\.map-overlay span\s*\{.*?\}"
replacement = """
.real-map-box {
    position: relative !important;
    min-height: 560px !important;
    padding: 0 !important;
    overflow: hidden !important;
    border-radius: 28px !important;
    border: 1px solid rgba(96,165,250,.22) !important;
    box-shadow: 0 30px 70px rgba(0,0,0,.35) !important;
}

.taxige-map {
    width: 100%;
    height: 560px;
    border: 0;
    display: block;
    filter: saturate(1.08) contrast(1.04);
}

.map-overlay {
    position: absolute;
    left: 24px;
    right: 24px;
    bottom: 24px;
    padding: 18px 22px;
    border-radius: 22px;
    background: rgba(15,23,42,.90);
    border: 1px solid rgba(96,165,250,.28);
    backdrop-filter: blur(12px);
    box-shadow: 0 18px 40px rgba(0,0,0,.30);
}

.map-overlay strong {
    display: block;
    font-size: 24px;
    font-weight: 900;
    color: #ffffff;
    margin-bottom: 6px;
}

.map-overlay span {
    display: block;
    color: #cbd5e1;
    font-weight: 700;
    line-height: 1.6;
}
"""

text = re.sub(pattern, replacement, text, flags=re.DOTALL)

# Ajustar media query móvil
text = text.replace(
    ".taxige-map {\n        height: 360px;\n    }",
    ".taxige-map {\n        height: 380px;\n    }"
)

p.write_text(text, encoding="utf-8")
print("Mapa ampliado y mejorado con diseño premium.")
