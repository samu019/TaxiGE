from pathlib import Path
import re

p = Path("templates/accounts/register_owner_kyc.html")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

start = text.find('<details class="kyc-payment-box')
end = text.find('</details>', start)

if start == -1 or end == -1:
    raise SystemExit("No se encontró el bloque de pago.")

end += len('</details>')

block = r'''
<details class="kyc-payment-box premium-payment-box" open>
    <summary>💳 Pago seguro de activación</summary>

    <div class="payment-alert">
        <div>
            <strong>🔐 Importante</strong>
            <p>
                Enviar esta solicitud no activa el panel automáticamente. TaxiGE revisará tu identidad,
                documentos y comprobante antes de aprobar tu cuenta.
            </p>
        </div>
        <div class="payment-secure-badge">🛡️ Transacción segura</div>
    </div>

    <div class="payment-info-grid premium-bank-grid">
        <div class="premium-info-card highlight">
            <span>💰 Importe de activación</span>
            <strong>{{ payment_settings.activation_fee|floatformat:0 }} XAF</strong>
        </div>

        <div class="premium-info-card">
            <span>🏦 Banco principal</span>
            <strong>{{ payment_settings.primary_bank_name|default:"No configurado" }}</strong>
        </div>

        <div class="premium-info-card">
            <span>👤 Beneficiario</span>
            <strong>{{ payment_settings.primary_account_holder|default:"No configurado" }}</strong>
        </div>

        <div class="premium-info-card">
            <span>🔢 Número de cuenta principal</span>
            <strong>{{ payment_settings.primary_account_number|default:"No configurado" }}</strong>
        </div>

        {% if payment_settings.secondary_bank_name or payment_settings.secondary_account_holder or payment_settings.secondary_account_number %}
            <div class="premium-info-card">
                <span>🏦 Banco alternativo</span>
                <strong>{{ payment_settings.secondary_bank_name|default:"No configurado" }}</strong>
            </div>

            <div class="premium-info-card">
                <span>🔢 Número de cuenta alternativa</span>
                <strong>{{ payment_settings.secondary_account_number|default:"No configurado" }}</strong>
            </div>
        {% endif %}
    </div>

    <details class="mini-help-box">
        <summary>📘 ¿Cómo realizar el pago?</summary>
        <ol>
            <li>Realiza la transferencia al banco indicado.</li>
            <li>Guarda el comprobante del pago.</li>
            <li>Escribe la referencia del pago.</li>
            <li>Sube el comprobante en JPG, PNG o PDF.</li>
            <li>Envía la solicitud KYC.</li>
        </ol>
    </details>

    <details class="mini-help-box">
        <summary>⚠️ Recomendaciones importantes</summary>
        <ul>
            <li>El comprobante debe verse claro y completo.</li>
            <li>El importe debe coincidir con la cuota indicada.</li>
            <li>No uses capturas borrosas o recortadas.</li>
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
        </div>

        <div class="form-field premium-field">
            <label for="{{ form.payment_receipt.id_for_label }}">📎 Comprobante de pago</label>
            {{ form.payment_receipt }}
            <small>Formatos aceptados: JPG, PNG o PDF.</small>
        </div>
    </div>

    <div class="final-security-note">
        🔒 Al enviar este formulario confirmas que los datos proporcionados son correctos.
        Nuestro equipo verificará la solicitud antes de activar el panel.
    </div>
</details>
'''

text = text[:start] + block + text[end:]

p.write_text(text, encoding="utf-8")
print("Valores dinámicos del bloque de pago corregidos.")
