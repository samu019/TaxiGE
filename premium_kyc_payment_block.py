from pathlib import Path

p = Path("templates/accounts/register_owner_kyc.html")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

# 1. Mejorar título del bloque
text = text.replace(
    "Pago de activación de cuenta",
    "💳 Pago seguro de activación"
)

# 2. Reemplazar el bloque visual de pago por una versión premium si existe kyc-payment-box
start = text.find('<details class="kyc-payment-box"')
end = text.find('</details>', start)

if start == -1 or end == -1:
    raise SystemExit("No se encontró el bloque details kyc-payment-box.")

end = end + len('</details>')

premium_block = r'''
<details class="kyc-payment-box premium-payment-box" open>
    <summary>
        💳 Pago seguro de activación
    </summary>

    <div class="payment-alert">
        <div>
            <strong>🔐 Importante</strong>
            <p>
                Enviar esta solicitud no activa el panel automáticamente. TaxiGE revisará tu identidad,
                documentos y comprobante antes de aprobar tu cuenta.
            </p>
        </div>
        <div class="payment-secure-badge">
            🛡️ Transacción segura
        </div>
    </div>

    <div class="payment-info-grid premium-bank-grid">
        <div class="premium-info-card highlight">
            <span>💰 Importe de activación</span>
            <strong>{{ payment_settings.activation_fee }} XAF</strong>
        </div>

        <div class="premium-info-card">
            <span>🏦 Banco principal</span>
            <strong>{{ payment_settings.primary_bank_name }}</strong>
        </div>

        <div class="premium-info-card">
            <span>🏦 Banco alternativo</span>
            <strong>{{ payment_settings.secondary_bank_name }}</strong>
        </div>

        <div class="premium-info-card">
            <span>👤 Beneficiario</span>
            <strong>{{ payment_settings.primary_account_holder }}</strong>
        </div>

        <div class="premium-info-card">
            <span>🔢 Número de cuenta principal</span>
            <strong>{{ payment_settings.primary_account_number }}</strong>
        </div>

        <div class="premium-info-card">
            <span>🔢 Número de cuenta ECOBANK</span>
            <strong>{{ payment_settings.secondary_account_number }}</strong>
        </div>
    </div>

    <details class="mini-help-box">
        <summary>📘 ¿Cómo realizar el pago?</summary>
        <ol>
            <li>Realiza la transferencia al banco indicado.</li>
            <li>Guarda el comprobante del pago.</li>
            <li>Escribe correctamente la referencia.</li>
            <li>Sube el comprobante en JPG, PNG o PDF.</li>
            <li>Envía la solicitud KYC.</li>
        </ol>
    </details>

    <details class="mini-help-box">
        <summary>⚠️ Recomendaciones importantes</summary>
        <ul>
            <li>El comprobante debe ser legible y completo.</li>
            <li>El importe debe coincidir con la cuota indicada.</li>
            <li>No uses documentos borrosos o recortados.</li>
            <li>La revisión puede tardar entre 1 y 24 horas hábiles.</li>
        </ul>
    </details>

    <p class="payment-note premium-note">
        {{ payment_settings.payment_instructions }}
    </p>

    <div class="form-grid">
        <div class="form-field premium-field">
            <label for="{{ form.payment_reference.id_for_label }}">🧾 Referencia de pago</label>
            {{ form.payment_reference }}
            <small>Ejemplo: ACT-2026-001 o número de referencia de tu transferencia.</small>
            {% if form.payment_reference.errors %}
                <div class="field-error">{{ form.payment_reference.errors }}</div>
            {% endif %}
        </div>

        <div class="form-field premium-field">
            <label for="{{ form.payment_receipt.id_for_label }}">📎 Comprobante de pago</label>
            {{ form.payment_receipt }}
            <small>Formatos aceptados: JPG, PNG o PDF.</small>
            {% if form.payment_receipt.errors %}
                <div class="field-error">{{ form.payment_receipt.errors }}</div>
            {% endif %}
        </div>
    </div>

    <div class="final-security-note">
        🔒 Al enviar este formulario confirmas que los datos proporcionados son correctos.
        Nuestro equipo verificará la solicitud antes de activar el panel.
    </div>
</details>
'''

text = text[:start] + premium_block + text[end:]

# 3. Agregar CSS premium antes del cierre de style si existe
premium_css = r'''
.premium-payment-box {
    margin: 30px 0;
    padding: 24px;
    border-radius: 28px;
    background:
        radial-gradient(circle at top right, rgba(37,99,235,.28), transparent 38%),
        linear-gradient(135deg, rgba(15,23,42,.96), rgba(30,41,59,.96));
    border: 1px solid rgba(96,165,250,.35);
    box-shadow: 0 26px 70px rgba(15,23,42,.32);
    color: #f8fafc;
}

.premium-payment-box summary {
    cursor: pointer;
    font-size: 26px;
    font-weight: 900;
    letter-spacing: -0.03em;
    list-style: none;
    display: flex;
    align-items: center;
    gap: 10px;
}

.premium-payment-box summary::-webkit-details-marker {
    display: none;
}

.premium-payment-box summary::after {
    content: " cerrar";
    margin-left: 10px;
    font-size: 13px;
    font-weight: 800;
    color: #cbd5e1;
    padding: 7px 12px;
    border-radius: 999px;
    background: rgba(255,255,255,.08);
    border: 1px solid rgba(255,255,255,.12);
}

.premium-payment-box:not([open]) summary::after {
    content: " abrir";
}

.payment-alert {
    margin-top: 20px;
    padding: 18px;
    border-radius: 20px;
    display: flex;
    justify-content: space-between;
    gap: 16px;
    align-items: center;
    background: rgba(37,99,235,.14);
    border: 1px solid rgba(96,165,250,.28);
}

.payment-alert p {
    margin: 6px 0 0;
    color: #cbd5e1;
    line-height: 1.5;
}

.payment-secure-badge {
    white-space: nowrap;
    padding: 12px 16px;
    border-radius: 16px;
    background: rgba(15,23,42,.50);
    border: 1px solid rgba(255,255,255,.12);
    font-weight: 900;
}

.premium-bank-grid {
    margin-top: 20px;
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 14px;
}

.premium-info-card {
    padding: 18px;
    border-radius: 20px;
    background: rgba(255,255,255,.07);
    border: 1px solid rgba(255,255,255,.12);
}

.premium-info-card.highlight {
    background: linear-gradient(135deg, rgba(245,158,11,.20), rgba(37,99,235,.12));
    border-color: rgba(245,158,11,.35);
}

.premium-info-card span {
    display: block;
    color: #cbd5e1;
    margin-bottom: 8px;
    font-size: 14px;
}

.premium-info-card strong {
    display: block;
    font-size: 20px;
    color: #ffffff;
}

.mini-help-box {
    margin-top: 16px;
    padding: 16px 18px;
    border-radius: 18px;
    background: rgba(124,58,237,.13);
    border: 1px solid rgba(167,139,250,.28);
}

.mini-help-box summary {
    font-size: 16px;
    font-weight: 900;
}

.mini-help-box ol,
.mini-help-box ul {
    margin: 14px 0 0 20px;
    color: #ddd6fe;
    line-height: 1.7;
}

.premium-note {
    margin: 18px 0;
    padding: 16px;
    border-radius: 18px;
    background: rgba(34,197,94,.10);
    border: 1px solid rgba(34,197,94,.22);
    color: #dcfce7;
}

.premium-field label {
    color: #ffffff;
    font-weight: 900;
}

.premium-field small {
    display: block;
    margin-top: 7px;
    color: #cbd5e1;
}

.premium-field input,
.premium-field select,
.premium-field textarea {
    background: rgba(15,23,42,.75) !important;
    color: #f8fafc !important;
    border: 1px solid rgba(148,163,184,.30) !important;
    border-radius: 16px !important;
    padding: 14px !important;
}

.final-security-note {
    margin-top: 20px;
    padding: 18px;
    border-radius: 18px;
    background: rgba(15,23,42,.70);
    border: 1px solid rgba(148,163,184,.22);
    color: #cbd5e1;
    font-weight: 700;
}

@media (max-width: 760px) {
    .premium-bank-grid,
    .payment-alert {
        grid-template-columns: 1fr;
        flex-direction: column;
        align-items: stretch;
    }

    .premium-payment-box {
        padding: 18px;
    }

    .premium-payment-box summary {
        font-size: 21px;
    }
}
'''

if premium_css not in text:
    if "</style>" in text:
        text = text.replace("</style>", premium_css + "\n</style>", 1)
    else:
        text = "<style>\n" + premium_css + "\n</style>\n" + text

p.write_text(text, encoding="utf-8")
print("Bloque de pago KYC convertido a diseño premium.")
