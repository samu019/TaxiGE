from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8")

helper = r'''

def render_panel(request, template_name, context=None):
    context = context or {}
    try:
        context['global_unread_notifications'] = Notification.objects.filter(
            user=request.user,
            is_read=False
        ).count()
    except Exception:
        context['global_unread_notifications'] = 0

    return render(request, template_name, context)

'''

if "def render_panel(request, template_name" not in text:
    text = text.replace("def create_notification(user, title,", helper + "\ndef create_notification(user, title,", 1)

text = text.replace("return render(request, 'dashboard/notifications.html', {", "return render_panel(request, 'dashboard/notifications.html', {")
text = text.replace("return render(request, 'dashboard/shared_access.html', {", "return render_panel(request, 'dashboard/shared_access.html', {")
text = text.replace("return render(request, 'dashboard/panel_home.html', context)", "return render_panel(request, 'dashboard/panel_home.html', context)")

p.write_text(text, encoding="utf-8")
print("render_panel con contador global añadido")
