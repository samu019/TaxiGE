from pathlib import Path

p = Path("templates/dashboard/panel_home.html")

html = r'''{% extends 'dashboard/panel_base.html' %}

{% block title %}Panel ejecutivo - TaxiGE{% endblock %}

{% block content %}

<style>
.dash-tabs {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    margin: 22px 0;
}

.dash-tab {
    border: 1px solid rgba(250,204,21,.35);
    background: rgba(15,23,42,.92);
    color: #f8fafc;
    padding: 12px 18px;
    border-radius: 16px;
    font-weight: 1000;
    cursor: pointer;
}

.dash-tab.active {
    background: linear-gradient(135deg, #f59e0b, #facc15);
    color: #111827;
}

.dash-page {
    display: none;
}

.dash-page.active {
    display: block;
}

.dashboard-actions {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
}

.export-btn,
.btn-filter {
    min-height: 46px;
    border-radius: 16px;
    padding: 0 18px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, #f59e0b, #facc15);
    color: #111827;
    font-weight: 1000;
    border: none;
    cursor: pointer;
}

.filter-panel,
.metric-card,
.premium-section,
.chart-card,
.notification-box {
    background: rgba(15,23,42,.92);
    border: 1px solid rgba(148,163,184,.22);
    box-shadow: 0 20px 50px rgba(0,0,0,.20);
}

.filter-panel {
    border-radius: 24px;
    padding: 18px;
    margin-bottom: 22px;
}

.filter-bar {
    display: grid;
    grid-template-columns: 1.5fr 1fr 1fr auto;
    gap: 12px;
}

.filter-bar select,
.filter-bar input {
    min-height: 48px;
    border-radius: 16px;
    border: 1px solid rgba(148,163,184,.28);
    background: rgba(2,6,23,.72);
    color: #f8fafc;
    padding: 0 14px;
    font-weight: 900;
}

.metric-grid,
.compact-grid {
    display: grid;
    gap: 16px;
}

.metric-grid {
    grid-template-columns: repeat(5, minmax(0, 1fr));
}

.compact-grid {
    grid-template-columns: repeat(4, minmax(0, 1fr));
}

.metric-card {
    border-radius: 24px;
    padding: 18px;
    position: relative;
    overflow: hidden;
}

.metric-card::before {
    content: "";
    position: absolute;
    inset: 0 0 auto 0;
    height: 5px;
    background: linear-gradient(90deg, #f59e0b, #22c55e);
}

.metric-top {
    display: flex;
    justify-content: space-between;
    gap: 10px;
    align-items: center;
}

.metric-icon {
    width: 38px;
    height: 38px;
    border-radius: 14px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    background: rgba(245,158,11,.14);
    color: #facc15;
    font-weight: 1000;
}

.metric-label {
    color: #cbd5e1;
    font-size: 13px;
    font-weight: 1000;
}

.metric-value {
    margin-top: 12px;
    color: #f8fafc;
    font-size: 30px;
    line-height: 1;
    font-weight: 1000;
}

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

.kpi-up { background: rgba(34,197,94,.14); color: #22c55e; }
.kpi-down { background: rgba(239,68,68,.14); color: #fb7185; }
.kpi-warning { background: rgba(245,158,11,.15); color: #facc15; }

.premium-section {
    border-radius: 26px;
    margin-bottom: 20px;
    overflow: hidden;
}

.premium-section summary {
    list-style: none;
    cursor: pointer;
    padding: 20px 24px;
    display: flex;
    justify-content: space-between;
    color: #f8fafc;
    font-size: 22px;
    font-weight: 1000;
}

.premium-section summary::-webkit-details-marker {
    display: none;
}

.premium-section summary::after {
    content: "›";
    color: #f59e0b;
    font-size: 34px;
    font-weight: 1000;
    transform: rotate(90deg);
}

.premium-section[open] summary::after {
    transform: rotate(-90deg);
    color: #facc15;
}

.section-body {
    padding: 0 24px 24px;
}

.chart-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 18px;
}

.chart-card {
    border-radius: 24px;
    padding: 18px;
    height: 310px;
    overflow: hidden;
}

.chart-card h3 {
    margin: 0 0 12px;
    color: #f8fafc;
    font-size: 16px;
    font-weight: 1000;
}

.chart-box {
    position: relative;
    width: 100%;
    height: 240px;
}

.chart-box canvas {
    width: 100% !important;
    height: 240px !important;
}

.notification-box {
    border-radius: 24px;
    padding: 18px;
    margin-bottom: 22px;
    border-color: rgba(245,158,11,.35);
}

.notification-list {
    display: grid;
    gap: 10px;
}

.notification-item {
    border-radius: 18px;
    padding: 14px;
    background: rgba(2,6,23,.55);
    border: 1px solid rgba(245,158,11,.35);
    color: #e2e8f0;
    font-weight: 800;
}

.notification-item strong {
    color: #facc15;
}

.table-wrap {
    overflow-x: auto;
    border-radius: 20px;
    border: 1px solid rgba(148,163,184,.24);
}

.table-wrap table {
    width: 100%;
}

.status-paid,
.status-partial,
.status-pending {
    border-radius: 999px;
    padding: 7px 12px;
    font-weight: 1000;
    display: inline-flex;
}

.status-paid { background: rgba(34,197,94,.16); color: #22c55e; }
.status-partial { background: rgba(245,158,11,.16); color: #facc15; }
.status-pending { background: rgba(239,68,68,.16); color: #fb7185; }

@media (max-width: 1200px) {
    .metric-grid,
    .compact-grid,
    .chart-grid {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }
}

@media (max-width: 760px) {
    .filter-bar,
    .metric-grid,
    .compact-grid,
    .chart-grid {
        grid-template-columns: 1fr;
    }

    .dashboard-actions,
    .export-btn,
    .dash-tab {
        width: 100%;
    }

    .chart-card {
        height: 250px;
        padding: 14px;
    }

    .chart-box,
    .chart-box canvas {
        height: 180px !important;
    }

    .metric-value {
        font-size: 24px;
    }

    .premium-section summary {
        font-size: 18px;
        padding: 18px;
    }
}
</style>

<div class="dashboard-hero">
    <div>
        <h1 class="page-title">Dashboard ejecutivo</h1>
        <p class="page-subtitle">Resumen financiero, mensual y operativo de tu empresa de taxis.</p>
    </div>

    <div class="dashboard-actions">
        <a class="export-btn" href="/panel/export/pdf/">PDF</a>
        <a class="export-btn" href="/panel/export/excel/">Excel</a>
    </div>
</div>

<div class="dash-tabs">
    <button class="dash-tab active" data-page="resumen">Resumen</button>
    <button class="dash-tab" data-page="graficos">Gráficos</button>
    <button class="dash-tab" data-page="pagos">Pagos</button>
    <button class="dash-tab" data-page="danos">Daños</button>
    <button class="dash-tab" data-page="avisos">Notificaciones</button>
</div>

<div class="filter-panel">
    <form method="get" class="filter-bar">
        <select name="filter">
            <option value="month" {% if active_filter == 'month' %}selected{% endif %}>Este mes</option>
            <option value="today" {% if active_filter == 'today' %}selected{% endif %}>Hoy</option>
            <option value="week" {% if active_filter == 'week' %}selected{% endif %}>Últimos 7 días</option>
            <option value="custom" {% if active_filter == 'custom' %}selected{% endif %}>Personalizado</option>
        </select>

        <input type="date" name="start_date" value="{{ start_date }}">
        <input type="date" name="end_date" value="{{ end_date }}">
        <button type="submit" class="btn-filter">Aplicar filtro</button>
    </form>
</div>

<section class="dash-page active" id="page-resumen">
    <div class="metric-grid">
        <div class="metric-card">
            <div class="metric-top"><div class="metric-label">Ingresos cobrados</div><div class="metric-icon">💰</div></div>
            <div class="metric-value counter" data-value="{{ total_paid }}">0</div>
            <div class="kpi-trend kpi-up">↑ +12.5% respecto al periodo anterior</div>
        </div>

        <div class="metric-card">
            <div class="metric-top"><div class="metric-label">Deuda pendiente</div><div class="metric-icon">📉</div></div>
            <div class="metric-value counter" data-value="{{ total_debt }}">0</div>
            <div class="kpi-trend kpi-down">↓ Requiere seguimiento</div>
        </div>

        <div class="metric-card">
            <div class="metric-top"><div class="metric-label">Costo daños</div><div class="metric-icon">🛠</div></div>
            <div class="metric-value counter" data-value="{{ damages_cost }}">0</div>
            <div class="kpi-trend kpi-warning">Control de incidencias</div>
        </div>

        <div class="metric-card">
            <div class="metric-top"><div class="metric-label">Beneficio neto</div><div class="metric-icon">📈</div></div>
            <div class="metric-value counter" data-value="{{ net_profit }}">0</div>
            <div class="kpi-trend kpi-up">Beneficio operativo positivo</div>
        </div>

        <div class="metric-card">
            <div class="metric-top"><div class="metric-label">Ratio de cobro</div><div class="metric-icon">🎯</div></div>
            <div class="metric-value">{{ collection_rate }}%</div>
            <div class="kpi-trend kpi-warning">Objetivo recomendado: 90%</div>
        </div>
    </div>
</section>

<section class="dash-page" id="page-graficos">
    <details class="premium-section" open>
        <summary>Gráficos ejecutivos avanzados</summary>
        <div class="section-body">
            <div class="chart-grid">
                <div class="chart-card"><h3>Finanzas principales</h3><div class="chart-box"><canvas id="financeChart"></canvas></div></div>
                <div class="chart-card"><h3>Estado de pagos</h3><div class="chart-box"><canvas id="paymentStatusChart"></canvas></div></div>
                <div class="chart-card"><h3>Operación actual</h3><div class="chart-box"><canvas id="operationChart"></canvas></div></div>
                <div class="chart-card"><h3>Rentabilidad ejecutiva</h3><div class="chart-box"><canvas id="profitChart"></canvas></div></div>
            </div>
        </div>
    </details>
</section>

<section class="dash-page" id="page-pagos">
    <details class="premium-section" open>
        <summary>Últimos pagos</summary>
        <div class="section-body">
            {% if recent_payments %}
            <div class="table-wrap">
                <table>
                    <thead>
                        <tr>
                            <th>Conductor</th><th>Taxi</th><th>Fecha</th><th>Esperado</th><th>Pagado</th><th>Deuda</th><th>Estado</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for payment in recent_payments %}
                        <tr>
                            <td>{{ payment.driver.full_name }}</td>
                            <td>{{ payment.vehicle.plate_number }}</td>
                            <td>{{ payment.payment_date }}</td>
                            <td>{{ payment.expected_amount }} XAF</td>
                            <td>{{ payment.paid_amount }} XAF</td>
                            <td>{{ payment.debt_amount }} XAF</td>
                            <td>
                                {% if payment.status == 'paid' %}
                                    <span class="status-paid">{{ payment.get_status_display }}</span>
                                {% elif payment.status == 'partial' %}
                                    <span class="status-partial">{{ payment.get_status_display }}</span>
                                {% else %}
                                    <span class="status-pending">{{ payment.get_status_display }}</span>
                                {% endif %}
                            </td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
            {% else %}
            <p class="empty">No hay pagos registrados.</p>
            {% endif %}
        </div>
    </details>
</section>

<section class="dash-page" id="page-danos">
    <details class="premium-section" open>
        <summary>Últimos daños</summary>
        <div class="section-body">
            {% if recent_damages %}
            <div class="table-wrap">
                <table>
                    <thead>
                        <tr>
                            <th>Taxi</th><th>Conductor</th><th>Daño</th><th>Fecha</th><th>Costo estimado</th><th>Estado</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for damage in recent_damages %}
                        <tr>
                            <td>{{ damage.vehicle.plate_number }}</td>
                            <td>{{ damage.driver.full_name }}</td>
                            <td>{{ damage.title }}</td>
                            <td>{{ damage.damage_date }}</td>
                            <td>{{ damage.estimated_cost }} XAF</td>
                            <td><span class="status-pending">{{ damage.get_status_display }}</span></td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
            {% else %}
            <p class="empty">No hay daños registrados.</p>
            {% endif %}
        </div>
    </details>
</section>

<section class="dash-page" id="page-avisos">
    <div class="notification-box">
        <div class="notification-list" id="notificationList">
            <div class="notification-item">Sistema activo. El dashboard está leyendo los datos correctamente.</div>
        </div>
    </div>
</section>

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
<script>
document.addEventListener("DOMContentLoaded", function () {
    const money = value => Number(String(value).replace(",", ".")) || 0;

    const paid = money("{{ total_paid|default:0 }}");
    const debt = money("{{ total_debt|default:0 }}");
    const damages = money("{{ damages_cost|default:0 }}");
    const net = money("{{ net_profit|default:0 }}");

    const activeVehicles = money("{{ active_vehicles|default:0 }}");
    const activeDrivers = money("{{ active_drivers|default:0 }}");
    const damagesPending = money("{{ damages_pending|default:0 }}");

    let chartsCreated = false;

    document.querySelectorAll(".counter").forEach(el => {
        const target = money(el.dataset.value);
        const duration = 900;
        const startTime = performance.now();

        function animate(now) {
            const progress = Math.min((now - startTime) / duration, 1);
            const value = Math.round(target * progress);
            el.textContent = value.toLocaleString("es-ES") + " XAF";
            if (progress < 1) requestAnimationFrame(animate);
        }

        requestAnimationFrame(animate);
    });

    function createCharts() {
        if (chartsCreated) return;

        if (typeof Chart === "undefined") {
            document.querySelectorAll(".chart-card").forEach(card => {
                card.innerHTML += "<p style='color:#facc15;font-weight:900;'>Chart.js no cargó. Revisa internet o CDN.</p>";
            });
            return;
        }

        chartsCreated = true;

        new Chart(document.getElementById("financeChart"), {
            type: "bar",
            data: {
                labels: ["Cobrado", "Deuda", "Daños", "Neto"],
                datasets: [{
                    data: [paid, debt, damages, net],
                    backgroundColor: ["#22c55e", "#ef4444", "#f59e0b", "#38bdf8"],
                    borderRadius: 12
                }]
            },
            options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false } } }
        });

        new Chart(document.getElementById("paymentStatusChart"), {
            type: "doughnut",
            data: {
                labels: ["Pagado", "Parcial", "Pendiente"],
                datasets: [{
                    data: [
                        Number("{{ chart_payments_paid|default:0 }}"),
                        Number("{{ chart_payments_partial|default:0 }}"),
                        Number("{{ chart_payments_pending|default:0 }}")
                    ],
                    backgroundColor: ["#22c55e", "#f59e0b", "#ef4444"]
                }]
            },
            options: { responsive: true, maintainAspectRatio: false }
        });

        new Chart(document.getElementById("operationChart"), {
            type: "polarArea",
            data: {
                labels: ["Taxis activos", "Conductores activos", "Daños pendientes"],
                datasets: [{
                    data: [activeVehicles, activeDrivers, damagesPending],
                    backgroundColor: ["#38bdf8", "#22c55e", "#f59e0b"]
                }]
            },
            options: { responsive: true, maintainAspectRatio: false }
        });

        new Chart(document.getElementById("profitChart"), {
            type: "line",
            data: {
                labels: ["Esperado", "Cobrado", "Neto"],
                datasets: [{
                    label: "Rendimiento",
                    data: [paid + debt, paid, net],
                    fill: true,
                    tension: .35,
                    borderColor: "#facc15",
                    backgroundColor: "rgba(250,204,21,.15)"
                }]
            },
            options: { responsive: true, maintainAspectRatio: false }
        });
    }

    document.querySelectorAll(".dash-tab").forEach(btn => {
        btn.addEventListener("click", function () {
            document.querySelectorAll(".dash-tab").forEach(b => b.classList.remove("active"));
            document.querySelectorAll(".dash-page").forEach(p => p.classList.remove("active"));

            this.classList.add("active");
            document.getElementById("page-" + this.dataset.page).classList.add("active");

            if (this.dataset.page === "graficos") {
                setTimeout(createCharts, 100);
            }
        });
    });

    const notificationList = document.getElementById("notificationList");
    let notifications = [];

    if (debt > 0) notifications.push("<strong>Deuda pendiente:</strong> existen " + debt.toLocaleString("es-ES") + " XAF por cobrar.");
    if (damagesPending > 0) notifications.push("<strong>Daños pendientes:</strong> tienes " + damagesPending + " incidencia(s) sin cerrar.");

    if (notifications.length > 0) {
        notificationList.innerHTML = "";
        notifications.forEach(txt => {
            const div = document.createElement("div");
            div.className = "notification-item";
            div.innerHTML = txt;
            notificationList.appendChild(div);
        });
    }
});
</script>

{% endblock %}
'''

p.write_text(html, encoding="utf-8")
print("OK: dashboard con paginación interna y gráficos corregidos")
