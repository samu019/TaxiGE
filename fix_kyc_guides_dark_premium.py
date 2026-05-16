from pathlib import Path
import re

p = Path("templates/accounts/register_owner_kyc.html")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

# Forzar estilo premium oscuro para las guías desplegables del KYC general
css = r'''
/* FIX PREMIUM KYC GUIDES */
.kyc-mini-guide {
    margin: 14px 0 28px !important;
    padding: 0 !important;
    border-radius: 20px !important;
    overflow: hidden !important;
    background:
        radial-gradient(circle at top right, rgba(37,99,235,.18), transparent 35%),
        linear-gradient(135deg, rgba(15,23,42,.96), rgba(30,41,59,.94)) !important;
    border: 1px solid rgba(96,165,250,.28) !important;
    box-shadow: 0 14px 34px rgba(15,23,42,.16) !important;
    color: #f8fafc !important;
}

.kyc-mini-guide summary {
    min-height: 54px !important;
    padding: 16px 18px !important;
    cursor: pointer !important;
    font-weight: 900 !important;
    color: #f8fafc !important;
    background: rgba(15,23,42,.38) !important;
    list-style: none !important;
    display: flex !important;
    align-items: center !important;
    gap: 10px !important;
}

.kyc-mini-guide summary::-webkit-details-marker {
    display: none !important;
}

.kyc-mini-guide summary::after {
    content: "abrir" !important;
    margin-left: auto !important;
    font-size: 12px !important;
    color: #93c5fd !important;
    padding: 6px 10px !important;
    border-radius: 999px !important;
    background: rgba(37,99,235,.16) !important;
    border: 1px solid rgba(96,165,250,.25) !important;
}

.kyc-mini-guide[open] summary::after {
    content: "cerrar" !important;
}

.kyc-mini-guide p {
    margin: 0 !important;
    padding: 16px 18px 18px !important;
    line-height: 1.65 !important;
    color: #cbd5e1 !important;
    background: rgba(15,23,42,.25) !important;
}

/* Separación profesional entre títulos, guías y campos */
form h2,
form h3,
.form-section-title,
.register-section-title {
    margin-top: 34px !important;
    margin-bottom: 12px !important;
    color: #f8fafc !important;
}

/* Evitar que las guías se peguen visualmente a los campos */
.kyc-mini-guide + .form-grid,
.kyc-mini-guide + .owner-kyc-grid,
.kyc-mini-guide + .kyc-grid,
.kyc-mini-guide + .form-field,
.kyc-mini-guide + .form-group {
    margin-top: 22px !important;
}

/* Mejor contraste para contenedores claros heredados */
.form-field,
.field-wrapper,
.form-group {
    background:
        linear-gradient(135deg, rgba(15,23,42,.92), rgba(30,41,59,.88)) !important;
    border: 1px solid rgba(148,163,184,.24) !important;
    color: #f8fafc !important;
}

.form-field label,
.field-wrapper label,
.form-group label {
    color: #f8fafc !important;
}

.form-field input,
.form-field select,
.form-field textarea,
.field-wrapper input,
.field-wrapper select,
.field-wrapper textarea,
.form-group input,
.form-group select,
.form-group textarea {
    background: rgba(15,23,42,.72) !important;
    color: #f8fafc !important;
    border: 1px solid rgba(148,163,184,.30) !important;
}

.form-field input::placeholder,
.form-field textarea::placeholder {
    color: #94a3b8 !important;
}
'''

# Eliminar bloque anterior problemático de guías si existe parcialmente
text = re.sub(
    r"/\* FIX PREMIUM KYC GUIDES \*/.*?(?=</style>)",
    "",
    text,
    flags=re.DOTALL
)

if "</style>" in text:
    text = text.replace("</style>", css + "\n</style>", 1)
else:
    text = "<style>\n" + css + "\n</style>\n" + text

p.write_text(text, encoding="utf-8")
print("Guías KYC ajustadas al estilo premium oscuro/azul.")
