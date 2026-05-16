from pathlib import Path

p = Path("templates/dashboard/calendar.html")
text = p.read_text(encoding="utf-8")

finance_block = """
    <section class="calendar-stats">
        <div class="calendar-stat">
            <span>Deuda pendiente total</span>
            <strong>{{ total_pending_debt }} XAF</strong>
        </div>

        <div class="calendar-stat">
            <span>Coste daños activos</span>
            <strong>{{ total_active_damage_cost }} XAF</strong>
        </div>

        <div class="calendar-stat">
            <span>Riesgo operativo</span>
            <strong>{{ total_operational_risk }} XAF</strong>
        </div>
    </section>
"""

if "Deuda pendiente total" not in text:
    text = text.replace('</section>\n\n    <section class="card"', '</section>\n\n' + finance_block + '\n    <section class="card"', 1)

p.write_text(text, encoding="utf-8")
print("Totales financieros mostrados en calendario")
