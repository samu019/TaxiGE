from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8")

old = """def create_notification(user, title, message, level='info', link=None):
    try:
        Notification.objects.create(
            user=user,
            title=title,
            message=message,
            level=level,
            link=link,
        )
    except Exception:
        pass"""

new = """def create_notification(user, title, message, level='info', link=None):
    try:
        recent_exists = Notification.objects.filter(
            user=user,
            title=title,
            message=message,
            is_read=False,
        ).exists()

        if recent_exists:
            return None

        return Notification.objects.create(
            user=user,
            title=title,
            message=message,
            level=level,
            link=link,
        )
    except Exception:
        return None"""

text = text.replace(old, new)

p.write_text(text, encoding="utf-8")
print("Protección contra notificaciones duplicadas aplicada")
