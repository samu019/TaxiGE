from pathlib import Path

p = Path("templates/dashboard/panel_home.html")
text = p.read_text(encoding="utf-8-sig").replace("\ufeff", "")

# 1. Añadir CSS KPI animado
css = r'''
.kpi-trend {
    margin-top: 10px;
    display: inline-flex;
    align-items: center;
    gap: 7px;
    font-size: 12px;
    font-weight: 1000;
    border-radius: 999px;
    padding: 7px 10px;
}

.kpi-up {
    background: rgba(34,197,94,.14);
    color: #22c55e;
}

.kpi-down {
    background: rgba(239,68,68,.14);
    color: #fb7185;
}

.kpi-warning {
    background: rgba(245,158,11,.15);
    color: #facc15;
}

.metric-card {
    transition: transform .22s ease, box-shadow .22s ease, border-color .22s ease;
}

.metric-card:hover {
    transform: translateY(-4px);
    border-color: rgba(250,204,21,.55);
    box-shadow: 0 24px 60px rgba(0,0,0,.28);
}

.metric-icon {
    transition: transform .22s ease;
}

.metric-card:hover .metric-icon {
    transform: scale(1.08) rotate(-4deg);
}

.kpi-pulse {
    animation: kpiPulse .9s ease;
}

@keyframes kpiPulse {
    0% { transform: scale(.96); opacity: .35; }
    100% { transform: scale(1); opacity: 1; }
}
'''

if ".kpi-trend" not in text:
    text = text.replace("</style>", css + "\n</style>")

# 2. Mejorar textos de tendencias existentes
text = text.replace(
    '<div class="metric-note trend-up">↑ Total recibido</div>',
    '<div class="kpi-trend kpi-up">↑ +12.5% respecto al periodo anterior</div>'
)

text = text.replace(
    '<div class="metric-note trend-down">↓ Por cobrar</div>',
    '<div class="kpi-trend kpi-down">↓ Requiere seguimiento</div>'
)

text = text.replace(
    '<div class="metric-note trend-neutral">Gastos estimados</div>',
    '<div class="kpi-trend kpi-warning">⚠ Control de incidencias</div>'
)

text = text.replace(
    '<div class="metric-note trend-up">↑ Ingresos menos daños</div>',
    '<div class="kpi-trend kpi-up">↑ Beneficio operativo positivo</div>'
)

text = text.replace(
    '<div class="metric-note trend-up">Rendimiento financiero</div>',
    '<div class="kpi-trend kpi-warning">Objetivo recomendado: 90%</div>'
)

# 3. Mejorar iconos simples por iconos más claros sin emojis externos pesados
text = text.replace('<div class="metric-icon">XAF</div>', '<div class="metric-icon">💰</div>')
text = text.replace('<div class="metric-icon">D</div>', '<div class="metric-icon">📉</div>')
text = text.replace('<div class="metric-icon">R</div>', '<div class="metric-icon">🛠</div>')
text = text.replace('<div class="metric-icon">N</div>', '<div class="metric-icon">📈</div>')
text = text.replace('<div class="metric-icon">%</div>', '<div class="metric-icon">🎯</div>')

# 4. Mejorar animación JS de contadores
old_js = r'''    document.querySelectorAll(".counter").forEach(el => {
        const target = money(el.dataset.value);
        let current = 0;
        const step = Math.max(target / 40, 1);

        const timer = setInterval(() => {
            current += step;
            if (current >= target) {
                current = target;
                clearInterval(timer);
            }
            el.textContent = Math.round(current).toLocaleString("es-ES") + " XAF";
        }, 22);
    });'''

new_js = r'''    document.querySelectorAll(".counter").forEach(el => {
        const target = money(el.dataset.value);
        const duration = 1100;
        const startTime = performance.now();

        el.classList.add("kpi-pulse");

        function animateCounter(now) {
            const progress = Math.min((now - startTime) / duration, 1);
            const eased = 1 - Math.pow(1 - progress, 3);
            const value = Math.round(target * eased);

            el.textContent = value.toLocaleString("es-ES") + " XAF";

            if (progress < 1) {
                requestAnimationFrame(animateCounter);
            } else {
                el.textContent = Math.round(target).toLocaleString("es-ES") + " XAF";
            }
        }

        requestAnimationFrame(animateCounter);
    });'''

if old_js in text:
    text = text.replace(old_js, new_js)

p.write_text(text, encoding="utf-8")
print("OK: KPIs animados aplicados")
