from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8")

if "from notifications.models import Notification" not in text:
    text = "from notifications.models import Notification\n" + text

helper = r'''

def create_notification(user, title, message, level='info', link=None):
    try:
        Notification.objects.create(
            user=user,
            title=title,
            message=message,
            level=level,
            link=link,
        )
    except Exception:
        pass

'''

if "def create_notification(user, title," not in text:
    text = text.replace("def audit_event(request, action,", helper + "\ndef audit_event(request, action,", 1)

p.write_text(text, encoding="utf-8")
print("Helper de notificaciones añadido")
