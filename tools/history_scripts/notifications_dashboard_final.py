from pathlib import Path

p = Path("templates/dashboard/panel_home.html")
text = p.read_text(encoding="utf-8-sig").replace("\ufeff", "")

# 1. Agregar CSS de notificaciones antes de </style>
css = r'''
.notification-box {
    background: rgba(15,23,42,.92);
    border: 1px solid rgba(245,158,11,.35);
    border-radius: 24px;
    padding: 18px;
    margin-bottom: 22px;
    box-shadow: 0 18px 45px rgba(0,0,0,.20);
}

.notification-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 14px;
    cursor: pointer;
    color: #f8fafc;
    font-weight: 1000;
    font-size: 18px;
}

.notification-badge {
    min-width: 34px;
    height: 34px;
    border-radius: 999px;
    background: linear-gradient(135deg, #f59e0b, #facc15);
    color: #111827;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-weight: 1000;
}

.notification-list {
    margin-top: 16px;
    display: grid;
    gap: 10px;
}

.notification-item {
    border-radius: 18px;
    padding: 14px;
    background: rgba(2,6,23,.55);
    border: 1px solid rgba(148,163,184,.20);
    color: #e2e8f0;
    font-weight: 800;
}

.notification-item strong {
    color: #facc15;
}

.notification-ok {
    border-color: rgba(34,197,94,.35);
}

.notification-warning {
    border-color: rgba(245,158,11,.45);
}

.notification-danger {
    border-color: rgba(239,68,68,.45);
}

.notification-box summary {
    list-style: none;
}

.notification-box summary::-webkit-details-marker {
    display: none;
}

.notification-box summary::after {
    content: "›";
    color: #f59e0b;
    font-size: 30px;
    font-weight: 1000;
    transform: rotate(90deg);
    transition: .22s ease;
}

.notification-box[open] summary::after {
    transform: rotate(-90deg);
    color: #facc15;
}

@media (max-width: 760px) {
    .notification-header {
        font-size: 16px;
    }

    .notification-item {
        font-size: 13px;
    }
}
'''

if ".notification-box" not in text:
    text = text.replace("</style>", css + "\n</style>")

# 2. Insertar bloque de notificaciones después de liveAlert
target = '''<div id="liveAlert" class="live-alert">
    Hay indicadores pendientes que requieren revisión.
</div>'''

notifications = r'''
<details class="notification-box" open>
    <summary class="notification-header">
        <span>Centro de notificaciones</span>
        <span class="notification-badge" id="notificationCount">0</span>
    </summary>

    <div class="notification-list" id="notificationList">
        <div class="notification-item notification-ok">
            Sistema activo. El dashboard está leyendo los datos correctamente.
        </div>
    </div>
</details>
'''

if "Centro de notificaciones" not in text:
    text = text.replace(target, target + "\n" + notifications)

# 3. Añadir JS dinámico antes de cierre DOMContentLoaded
js_marker = '''    setInterval(() => {
        const now = new Date().toLocaleTimeString("es-ES");
        console.log("TaxiGE dashboard activo:", now);
    }, 30000);'''

js_notifications = r'''
    const notificationList = document.getElementById("notificationList");
    const notificationCount = document.getElementById("notificationCount");

    let notifications = [];

    if (debt > 0) {
        notifications.push({
            type: "notification-warning",
            text: "<strong>Deuda pendiente:</strong> existen " + debt.toLocaleString("es-ES") + " XAF por cobrar."
        });
    }

    if (damagesPending > 0) {
        notifications.push({
            type: "notification-danger",
            text: "<strong>Daños pendientes:</strong> tienes " + damagesPending + " incidencia(s) sin cerrar."
        });
    }

    if (paid > 0 && debt > 0) {
        const total = paid + debt;
        const ratio = Math.round((paid / total) * 100);
        if (ratio < 85) {
            notifications.push({
                type: "notification-warning",
                text: "<strong>Ratio de cobro bajo:</strong> el rendimiento está en " + ratio + "%."
            });
        }
    }

    if (notifications.length > 0 && notificationList && notificationCount) {
        notificationList.innerHTML = "";
        notifications.forEach(item => {
            const div = document.createElement("div");
            div.className = "notification-item " + item.type;
            div.innerHTML = item.text;
            notificationList.appendChild(div);
        });
        notificationCount.textContent = notifications.length;
    } else if (notificationCount) {
        notificationCount.textContent = "0";
    }

'''

if "notificationCount" in text and "Ratio de cobro bajo" not in text:
    text = text.replace(js_marker, js_notifications + "\n" + js_marker)

p.write_text(text, encoding="utf-8")
print("OK: centro de notificaciones aplicado")
