from pathlib import Path

p = Path("templates/dashboard/panel_home.html")

html = r'''{% extends "dashboard/panel_base.html" %}

{% block title %}Panel ejecutivo - TaxiGE{% endblock %}

{% block content %}
<h1 class="page-title">Dashboard ejecutivo</h1>
<p class="page-subtitle">Resumen financiero, mensual y operativo de tu empresa de taxis.</p>

<div class="cards">
    <div class="card"><h3>Ingresos cobrados</h3><strong>{{ total_paid }} XAF</strong></div>
    <div class="card"><h3>Deuda pendiente</h3><strong>{{ total_debt }} XAF</strong></div>
    <div class="card"><h3>Costo daños</h3><strong>{{ damages_cost }} XAF</strong></div>
    <div class="card"><h3>Beneficio neto</h3><strong>{{ net_profit }} XAF</strong></div>
    <div class="card"><h3>Ratio de cobro</h3><strong>{{ collection_rate }}%</strong></div>
</div>

<div class="section">
    <h2>Resumen mensual - {{ month_label }}</h2>
    <div class="cards" style="margin-bottom:0;">
        <div class="card"><h3>Ingresos del mes</h3><strong>{{ month_paid }} XAF</strong></div>
        <div class="card"><h3>Deuda del mes</h3><strong>{{ month_debt }} XAF</strong></div>
        <div class="card"><h3>Daños del mes</h3><strong>{{ month_damages_cost }} XAF</strong></div>
        <div class="card"><h3>Neto mensual</h3><strong>{{ month_net_profit }} XAF</strong></div>
        <div class="card"><h3>Pagado hoy</h3><strong>{{ today_paid }} XAF</strong></div>
        <div class="card"><h3>Últimos 7 días</h3><strong>{{ last_7_paid }} XAF</strong></div>
    </div>
</div>

<div class="cards">
    <div class="card"><h3>Empresas</h3><strong>{{ companies_count }}</strong></div>
    <div class="card"><h3>Taxis activos</h3><strong>{{ active_vehicles }}</strong></div>
    <div class="card"><h3>Conductores activos</h3><strong>{{ active_drivers }}</strong></div>
    <div class="card"><h3>Pagos registrados</h3><strong>{{ payments_count }}</strong></div>
    <div class="card"><h3>Daños pendientes</h3><strong>{{ damages_pending }}</strong></div>
</div>

<div class="charts-grid">
    <div class="section">
        <h2>Finanzas principales</h2>
        <div class="chart-box"><canvas id="financeChart"></canvas></div>
    </div>

    <div class="section">
        <h2>Operación actual</h2>
        <div class="chart-box"><canvas id="operationChart"></canvas></div>
    </div>
</div>

<div class="section">
    <h2>Últimos pagos</h2>
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
                            <td><span class="badge">{{ payment.get_status_display }}</span></td>
                        </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    {% else %}
        <p class="empty">Todavía no hay pagos registrados.</p>
    {% endif %}
</div>

<div class="section">
    <h2>Últimos daños</h2>
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
                            <td><span class="badge">{{ damage.get_status_display }}</span></td>
                        </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    {% else %}
        <p class="empty">Todavía no hay daños registrados.</p>
    {% endif %}
</div>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
document.addEventListener('DOMContentLoaded', function () {
    const paid = Number('{{ total_paid|default:0 }}'.replace(',', '.')) || 0;
    const debt = Number('{{ total_debt|default:0 }}'.replace(',', '.')) || 0;
    const damagesCost = Number('{{ damages_cost|default:0 }}'.replace(',', '.')) || 0;
    const netProfit = Number('{{ net_profit|default:0 }}'.replace(',', '.')) || 0;

    const activeVehicles = Number('{{ active_vehicles|default:0 }}') || 0;
    const activeDrivers = Number('{{ active_drivers|default:0 }}') || 0;
    const damagesPending = Number('{{ damages_pending|default:0 }}') || 0;

    const financeCanvas = document.getElementById('financeChart');
    const operationCanvas = document.getElementById('operationChart');

    if (financeCanvas) {
        new Chart(financeCanvas, {
            type: 'bar',
            data: {
                labels: ['Cobrado', 'Deuda', 'Daños', 'Neto'],
                datasets: [{
                    label: 'XAF',
                    data: [paid, debt, damagesCost, netProfit],
                    borderWidth: 1,
                    borderRadius: 12
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: { legend: { display: false } },
                scales: { y: { beginAtZero: true } }
            }
        });
    }

    if (operationCanvas) {
        new Chart(operationCanvas, {
            type: 'doughnut',
            data: {
                labels: ['Taxis activos', 'Conductores activos', 'Daños pendientes'],
                datasets: [{
                    data: [activeVehicles, activeDrivers, damagesPending],
                    borderWidth: 2
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false
            }
        });
    }
});
</script>
{% endblock %}
'''

p.write_text(html, encoding="utf-8")
print("OK: panel_home.html limpio y único")
