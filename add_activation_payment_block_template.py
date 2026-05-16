from pathlib import Path

p = Path("templates/accounts/register_owner_kyc.html")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

payment_block = r'''
<details class="kyc-payment-box" open>
    <summary>
        Pago de activación de cuenta
    </summary>

    <div class="payment-info-grid">
        <div>
            <span>Importe de activación</span>
            <strong>50.000 XAF</strong>
        </div>

        <div>
            <span>Banco</span>
            <strong>BANGE</strong>
        </div>

        <div>
            <span>Beneficiario</span>
            <strong>TaxiGE Platform</strong>
        </div>

        <div>
            <span>Número de cuenta</span>
            <strong>100200300400</strong>
        </div>
    </div>

    <p class="payment-note">
        Realiza el pago de activación y sube el comprobante. Tu solicitud será revisada por el administrador antes de activar tu cuenta de propietario.
    </p>

    <div class="form-grid">
        <div class="form-field">
            <label for="{{ form.payment_reference.id_for_label }}">Referencia de pago</label>
            {{ form.payment_reference }}
            {% if form.payment_reference.errors %}
                <div class="field-error">{{ form.payment_reference.errors }}</div>
            {% endif %}
        </div>

        <div class="form-field">
            <label for="{{ form.payment_receipt.id_for_label }}">Comprobante de pago</label>
            {{ form.payment_receipt }}
            {% if form.payment_receipt.errors %}
                <div class="field-error">{{ form.payment_receipt.errors }}</div>
            {% endif %}
        </div>
    </div>
</details>
'''

css = r'''
<style>
.kyc-payment-box {
    margin: 22px 0;
    padding: 18px;
    border-radius: 18px;
    border: 1px solid rgba(59,130,246,.28);
    background: rgba(59,130,246,.08);
}

.kyc-payment-box summary {
    cursor: pointer;
    font-weight: 800;
    font-size: 18px;
    list-style: none;
}

.kyc-payment-box summary::-webkit-details-marker {
    display: none;
}

.kyc-payment-box summary::after {
    content: " desplegar";
    font-size: 12px;
    opacity: .65;
    margin-left: 8px;
}

.kyc-payment-box[open] summary::after {
    content: " cerrar";
}

.payment-info-grid {
    margin-top: 16px;
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 12px;
}

.payment-info-grid div {
    padding: 13px;
    border-radius: 14px;
    background: rgba(255,255,255,.07);
    border: 1px solid rgba(255,255,255,.10);
}

.payment-info-grid span {
    display: block;
    font-size: 13px;
    opacity: .75;
    margin-bottom: 4px;
}

.payment-info-grid strong {
    font-size: 16px;
}

.payment-note {
    margin: 16px 0;
    opacity: .85;
    line-height: 1.5;
}

@media (max-width: 720px) {
    .payment-info-grid {
        grid-template-columns: 1fr;
    }
}
</style>
'''

if "kyc-payment-box" not in text:
    if "</style>" in text:
        text = text.replace("</style>", css.replace("<style>", "").replace("</style>", "") + "\n</style>", 1)
    else:
        text = css + "\n" + text

    markers = [
        '<button type="submit"',
        '<button',
        '</form>',
    ]

    inserted = False
    for marker in markers:
        pos = text.find(marker)
        if pos != -1:
            text = text[:pos] + payment_block + "\n" + text[pos:]
            inserted = True
            break

    if not inserted:
        raise SystemExit("No se encontró punto seguro para insertar el bloque de pago.")

p.write_text(text, encoding="utf-8")
print("Bloque desplegable de pago agregado al formulario KYC.")
