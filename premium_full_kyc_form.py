from pathlib import Path

p = Path("templates/accounts/register_owner_kyc.html")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

# Mejorar textos básicos
replacements = {
    "Enviar esta solicitud no activa el panel automáticamente. TaxiGE revisará tu identidad y documentos.":
    "🔐 Enviar esta solicitud no activa el panel automáticamente. TaxiGE revisará tu identidad, documentos, pago y datos del taxi antes de aprobar el acceso.",

    "1. Datos de cuenta": "👤 1. Datos de cuenta",
    "2. Identificación del propietario": "🛂 2. Identificación del propietario",
    "3. Empresa o flota": "🏢 3. Empresa o flota",
    "4. Taxi principal de verificación": "🚕 4. Taxi principal de verificación",
    "5. Mensaje adicional": "💬 5. Mensaje adicional",
}

for old, new in replacements.items():
    text = text.replace(old, new)

# Agregar ayudas desplegables minimalistas después de títulos si no existen
helpers = {
    "👤 1. Datos de cuenta": """
<details class="kyc-mini-guide">
    <summary>💡 Consejos para esta sección</summary>
    <p>Usa datos reales. El correo y el teléfono servirán para avisarte sobre la aprobación de tu cuenta.</p>
</details>
""",
    "🛂 2. Identificación del propietario": """
<details class="kyc-mini-guide">
    <summary>📘 Cómo subir tu identificación</summary>
    <p>Sube un documento legible y una selfie clara. Evita fotos borrosas, recortadas o con sombras.</p>
</details>
""",
    "🏢 3. Empresa o flota": """
<details class="kyc-mini-guide">
    <summary>🏷️ Cómo rellenar la empresa/flota</summary>
    <p>Si no tienes empresa formal, escribe tu nombre comercial o tu nombre como propietario de la flota.</p>
</details>
""",
    "🚕 4. Taxi principal de verificación": """
<details class="kyc-mini-guide">
    <summary>🚘 Documentos recomendados del taxi</summary>
    <p>Adjunta matrícula, licencia/permiso y prueba de propiedad. El taxi principal sirve para validar tu cuenta.</p>
</details>
""",
    "💬 5. Mensaje adicional": """
<details class="kyc-mini-guide">
    <summary>📝 Qué puedes escribir aquí</summary>
    <p>Puedes añadir observaciones sobre tu flota, ciudad, documentos pendientes o cualquier dato útil para administración.</p>
</details>
""",
}

for title, helper in helpers.items():
    if title in text and helper.strip() not in text:
        text = text.replace(title, title + "\n" + helper, 1)

premium_css = r'''
/* PREMIUM KYC FORM */
.kyc-alert,
.kyc-notice,
.alert,
.notice {
    border-radius: 22px !important;
    padding: 18px 20px !important;
    background: linear-gradient(135deg, rgba(37,99,235,.16), rgba(15,23,42,.92)) !important;
    border: 1px solid rgba(96,165,250,.28) !important;
    color: #f8fafc !important;
    box-shadow: 0 16px 45px rgba(15,23,42,.18);
}

form h2,
form h3,
.form-section-title,
.register-section-title {
    margin-top: 28px !important;
    margin-bottom: 14px !important;
    padding: 18px 20px !important;
    border-radius: 22px !important;
    background:
        radial-gradient(circle at top right, rgba(245,158,11,.18), transparent 35%),
        linear-gradient(135deg, rgba(15,23,42,.96), rgba(30,41,59,.92)) !important;
    border: 1px solid rgba(148,163,184,.24) !important;
    color: #f8fafc !important;
    font-size: 22px !important;
    font-weight: 900 !important;
    letter-spacing: -0.03em;
}

.kyc-mini-guide {
    margin: -4px 0 18px !important;
    padding: 14px 16px !important;
    border-radius: 18px !important;
    background: rgba(124,58,237,.12) !important;
    border: 1px solid rgba(167,139,250,.24) !important;
    color: #ddd6fe !important;
}

.kyc-mini-guide summary {
    cursor: pointer;
    font-weight: 900;
    color: #f5f3ff;
}

.kyc-mini-guide p {
    margin: 10px 0 0;
    line-height: 1.55;
    color: #ddd6fe;
}

.form-grid,
.owner-kyc-grid,
.kyc-grid {
    gap: 18px !important;
}

.form-field,
.field-wrapper,
.form-group {
    padding: 16px !important;
    border-radius: 20px !important;
    background: rgba(15,23,42,.82) !important;
    border: 1px solid rgba(148,163,184,.22) !important;
    box-shadow: 0 12px 28px rgba(15,23,42,.10);
}

.form-field label,
.field-wrapper label,
.form-group label {
    display: block;
    margin-bottom: 8px;
    color: #f8fafc !important;
    font-weight: 900 !important;
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
    width: 100%;
    border-radius: 15px !important;
    border: 1px solid rgba(148,163,184,.28) !important;
    background: rgba(255,255,255,.08) !important;
    color: #f8fafc !important;
    padding: 13px 14px !important;
    outline: none !important;
}

.form-field input:focus,
.form-field select:focus,
.form-field textarea:focus,
.field-wrapper input:focus,
.field-wrapper select:focus,
.field-wrapper textarea:focus,
.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
    border-color: rgba(96,165,250,.85) !important;
    box-shadow: 0 0 0 4px rgba(37,99,235,.18) !important;
}

input[type="file"] {
    background: rgba(15,23,42,.65) !important;
    border-style: dashed !important;
    cursor: pointer;
}

button[type="submit"],
.submit-btn,
.btn-submit {
    margin-top: 28px !important;
    width: 100% !important;
    border: 0 !important;
    border-radius: 20px !important;
    padding: 18px 22px !important;
    background: linear-gradient(135deg, #f59e0b, #facc15) !important;
    color: #020617 !important;
    font-weight: 950 !important;
    font-size: 18px !important;
    box-shadow: 0 18px 42px rgba(245,158,11,.28);
    cursor: pointer;
}

button[type="submit"]::before {
    content: "🚀 ";
}

@media (max-width: 760px) {
    form h2,
    form h3,
    .form-section-title,
    .register-section-title {
        font-size: 19px !important;
    }

    .form-field,
    .field-wrapper,
    .form-group {
        padding: 14px !important;
    }
}
'''

if "/* PREMIUM KYC FORM */" not in text:
    if "</style>" in text:
        text = text.replace("</style>", premium_css + "\n</style>", 1)
    else:
        text = "<style>\n" + premium_css + "\n</style>\n" + text

p.write_text(text, encoding="utf-8")
print("Formulario KYC general mejorado a estilo premium.")
