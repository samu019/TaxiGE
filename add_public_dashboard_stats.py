from pathlib import Path

p = Path("templates/accounts/request_admin.html")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

stats_block = '''
        <section class="card">
            <h2>📊 Estadísticas públicas TaxiGE</h2>
            <p>
                Vista informativa del ecosistema TaxiGE para usuarios normales. Los datos empresariales privados
                solo están disponibles para propietarios aprobados.
            </p>

            <div class="feature-grid">
                <div class="feature">
                    <strong>🚕 Gestión de flotas</strong>
                    <span>Módulo preparado para taxis, matrículas y estados operativos.</span>
                </div>
                <div class="feature">
                    <strong>👥 Conductores</strong>
                    <span>Control de conductores, licencias y asignaciones.</span>
                </div>
                <div class="feature">
                    <strong>💳 Finanzas</strong>
                    <span>Seguimiento de pagos, deudas y reportes internos.</span>
                </div>
                <div class="feature">
                    <strong>🛠️ Incidencias</strong>
                    <span>Registro de daños, reparaciones y responsabilidades.</span>
                </div>
            </div>

            <div class="notice">
                🔒 Esta sección es pública e informativa. Para acceder a estadísticas reales de una flota,
                debes completar la verificación KYC como propietario.
            </div>
        </section>
'''

if "📊 Estadísticas públicas TaxiGE" not in text:
    text = text.replace(
        "<section class=\"section-grid\">",
        stats_block + "\n\n        <section class=\"section-grid\">",
        1
    )

# Enlace a términos
text = text.replace(
    "Si solo quieres mantener tu cuenta normal, no necesitas hacer nada más.",
    'Si solo quieres mantener tu cuenta normal, no necesitas hacer nada más. Consulta también nuestros <a href="/terms/" style="color:#facc15;font-weight:900;">Términos y Condiciones</a>.'
)

p.write_text(text, encoding="utf-8")
print("Dashboard público con estadísticas agregado.")
