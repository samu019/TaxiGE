from pathlib import Path

p = Path("templates/dashboard/panel_home.html")
text = p.read_text(encoding="utf-8-sig").replace("\ufeff", "")

# Reemplazar sección de gráficos ejecutivos
start = text.find('<details class="premium-section" open>\n    <summary>Gráficos ejecutivos</summary>')
end = text.find('</details>', start)

if start != -1 and end != -1:
    end = end + len('</details>')
    new_section = r'''<details class="premium-section" open>
    <summary>Gráficos ejecutivos avanzados</summary>
    <div class="section-body">
        <div class="chart-grid">
            <div class="chart-card">
                <h3>Finanzas principales</h3>
                <canvas id="financeChart"></canvas>
            </div>

            <div class="chart-card">
                <h3>Estado de pagos</h3>
                <canvas id="paymentStatusChart"></canvas>
            </div>

            <div class="chart-card">
                <h3>Operación actual</h3>
                <canvas id="operationChart"></canvas>
            </div>

            <div class="chart-card">
                <h3>Rentabilidad ejecutiva</h3>
                <canvas id="profitChart"></canvas>
            </div>
        </div>
    </div>
</details>'''
    text = text[:start] + new_section + text[end:]

# Añadir CSS de grid mejorado
if ".chart-grid-advanced" not in text:
    text = text.replace(
""".chart-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 18px;
}""",
""".chart-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 18px;
}

.chart-card {
    position: relative;
}

.chart-card canvas {
    display: block;
}"""
)

# Reemplazar JS de charts completo desde const financeChart
marker_start = text.find('    const financeChart = document.getElementById("financeChart");')
marker_end = text.find('    const notificationList = document.getElementById("notificationList");')

if marker_start != -1 and marker_end != -1:
    charts_js = r'''    const chartTheme = {
        textColor: "#cbd5e1",
        gridColor: "rgba(148,163,184,.16)",
        yellow: "#facc15",
        green: "#22c55e",
        red: "#ef4444",
        blue: "#38bdf8",
        orange: "#f59e0b"
    };

    Chart.defaults.color = chartTheme.textColor;
    Chart.defaults.borderColor = chartTheme.gridColor;
    Chart.defaults.font.family = "Arial";

    const commonOptions = {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                labels: {
                    boxWidth: 12,
                    usePointStyle: true
                }
            }
        },
        scales: {
            y: {
                beginAtZero: true,
                grid: { color: chartTheme.gridColor },
                ticks: { color: chartTheme.textColor }
            },
            x: {
                grid: { display: false },
                ticks: { color: chartTheme.textColor }
            }
        }
    };

    const financeChart = document.getElementById("financeChart");
    if (financeChart) {
        new Chart(financeChart, {
            type: "bar",
            data: {
                labels: ["Cobrado", "Deuda", "Daños", "Neto"],
                datasets: [{
                    label: "XAF",
                    data: [paid, debt, damages, net],
                    backgroundColor: [
                        "rgba(34,197,94,.75)",
                        "rgba(239,68,68,.75)",
                        "rgba(245,158,11,.75)",
                        "rgba(56,189,248,.75)"
                    ],
                    borderRadius: 14,
                    borderWidth: 0
                }]
            },
            options: {
                ...commonOptions,
                plugins: {
                    legend: { display: false }
                }
            }
        });
    }

    const paymentStatusChart = document.getElementById("paymentStatusChart");
    if (paymentStatusChart) {
        new Chart(paymentStatusChart, {
            type: "doughnut",
            data: {
                labels: ["Pagado", "Parcial", "Pendiente"],
                datasets: [{
                    data: [
                        Number("{{ chart_payments_paid|default:0 }}"),
                        Number("{{ chart_payments_partial|default:0 }}"),
                        Number("{{ chart_payments_pending|default:0 }}")
                    ],
                    backgroundColor: [
                        "rgba(34,197,94,.8)",
                        "rgba(245,158,11,.8)",
                        "rgba(239,68,68,.8)"
                    ],
                    borderColor: "rgba(15,23,42,1)",
                    borderWidth: 4
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                cutout: "68%",
                plugins: {
                    legend: {
                        position: "bottom",
                        labels: { usePointStyle: true }
                    }
                }
            }
        });
    }

    const operationChart = document.getElementById("operationChart");
    if (operationChart) {
        new Chart(operationChart, {
            type: "polarArea",
            data: {
                labels: ["Taxis activos", "Conductores activos", "Daños pendientes"],
                datasets: [{
                    data: [activeVehicles, activeDrivers, damagesPending],
                    backgroundColor: [
                        "rgba(56,189,248,.7)",
                        "rgba(34,197,94,.7)",
                        "rgba(245,158,11,.7)"
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: "bottom",
                        labels: { usePointStyle: true }
                    }
                }
            }
        });
    }

    const profitChart = document.getElementById("profitChart");
    if (profitChart) {
        new Chart(profitChart, {
            type: "line",
            data: {
                labels: ["Esperado", "Cobrado", "Neto"],
                datasets: [{
                    label: "Rendimiento",
                    data: [paid + debt, paid, net],
                    fill: true,
                    tension: .38,
                    borderColor: "rgba(250,204,21,1)",
                    backgroundColor: "rgba(250,204,21,.12)",
                    pointBackgroundColor: "rgba(250,204,21,1)",
                    pointRadius: 5,
                    pointHoverRadius: 7
                }]
            },
            options: commonOptions
        });
    }

'''
    text = text[:marker_start] + charts_js + text[marker_end:]

p.write_text(text, encoding="utf-8")
print("OK: gráficos avanzados aplicados")
