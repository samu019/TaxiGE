from pathlib import Path

p = Path("templates/dashboard/subscription_renew.html")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

old = """        <div class="actions">
            <a class="btn btn-primary" href="/panel/subscription/renew/">Subir comprobante de renovación</a>
            <a class="btn btn-muted" href="/accounts/logout/">Cerrar sesión</a>
        </div>
"""

new = """        <form method="post" enctype="multipart/form-data" style="margin-top: 26px;">
            {% csrf_token %}

            <div class="bank-grid">
                <div class="box">
                    <small>Referencia de pago</small>
                    <input type="text"
                           name="payment_reference"
                           placeholder="Ejemplo: TRX-2026-0001"
                           required
                           style="width:100%; margin-top:8px; padding:14px; border-radius:14px; border:1px solid rgba(255,255,255,.18); background:rgba(255,255,255,.08); color:white;">
                </div>

                <div class="box">
                    <small>Comprobante de pago</small>
                    <input type="file"
                           name="payment_receipt"
                           accept=".pdf,.jpg,.jpeg,.png"
                           required
                           style="width:100%; margin-top:8px; padding:14px; border-radius:14px; border:1px solid rgba(255,255,255,.18); background:rgba(255,255,255,.08); color:white;">
                </div>
            </div>

            <div class="actions">
                <button type="submit" class="btn btn-primary" style="border:0; cursor:pointer;">
                    Enviar comprobante
                </button>

                <a class="btn btn-muted" href="/accounts/logout/">Cerrar sesión</a>
            </div>
        </form>
"""

if old in text:
    text = text.replace(old, new, 1)
else:
    raise SystemExit("No se encontró el bloque del botón anterior.")

p.write_text(text, encoding="utf-8")
print("Formulario de subida de comprobante agregado.")
