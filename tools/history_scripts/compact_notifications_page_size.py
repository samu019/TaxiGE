from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8")
text = text.replace("Paginator(notifications, 10)", "Paginator(notifications, 6)")
p.write_text(text, encoding="utf-8")
print("Paginación reducida a 6 notificaciones por página")
