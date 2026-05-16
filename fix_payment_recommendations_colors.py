from pathlib import Path
import re

p = Path("templates/accounts/register_owner_kyc.html")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

css = r'''
/* FIX PAYMENT RECOMMENDATIONS CONTRAST */
.mini-help-box {
    background:
        radial-gradient(circle at top right, rgba(37,99,235,.18), transparent 35%),
        linear-gradient(135deg, rgba(15,23,42,.96), rgba(30,41,59,.94)) !important;
    border: 1px solid rgba(96,165,250,.30) !important;
    color: #f8fafc !important;
}

.mini-help-box summary {
    color: #f8fafc !important;
    font-weight: 950 !important;
}

.mini-help-box ol,
.mini-help-box ul,
.mini-help-box li {
    color: #dbeafe !important;
}

.mini-help-box li::marker {
    color: #facc15 !important;
}

.premium-note {
    background: rgba(34,197,94,.13) !important;
    border: 1px solid rgba(34,197,94,.30) !important;
    color: #dcfce7 !important;
}

/* FIX EMPTY PAYMENT VALUES VISIBILITY */
.premium-info-card strong:empty::after {
    content: "No configurado";
    color: #f8fafc;
}
'''

text = re.sub(
    r"/\* FIX PAYMENT RECOMMENDATIONS CONTRAST \*/.*?(?=</style>)",
    "",
    text,
    flags=re.DOTALL
)

if "</style>" in text:
    text = text.replace("</style>", css + "\n</style>", 1)
else:
    text = "<style>\n" + css + "\n</style>\n" + text

p.write_text(text, encoding="utf-8")
print("Colores de recomendaciones importantes corregidos.")
