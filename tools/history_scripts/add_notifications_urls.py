from pathlib import Path

p = Path("dashboard/urls.py")
text = p.read_text(encoding="utf-8")

routes = [
    "    path('notifications/', views.panel_notifications, name='panel_notifications'),",
    "    path('notifications/<int:notification_id>/read/', views.mark_notification_read, name='mark_notification_read'),",
    "    path('notifications/read-all/', views.mark_all_notifications_read, name='mark_all_notifications_read'),",
]

for route in routes:
    if route not in text:
        text = text.replace("urlpatterns = [", "urlpatterns = [\n" + route, 1)

p.write_text(text, encoding="utf-8")
print("Rutas de notificaciones añadidas")
