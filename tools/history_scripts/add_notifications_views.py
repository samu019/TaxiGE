from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8")

if "from notifications.models import Notification" not in text:
    text = "from notifications.models import Notification\n" + text

block = r'''

@login_required
def panel_notifications(request):
    guard_response = panel_guard(request)
    if guard_response:
        return guard_response

    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'dashboard/notifications.html', {
        'notifications': notifications,
        'unread_count': notifications.filter(is_read=False).count(),
    })


@login_required
def mark_notification_read(request, notification_id):
    guard_response = panel_guard(request)
    if guard_response:
        return guard_response

    notification = get_object_or_404(Notification, id=notification_id, user=request.user)

    notification.is_read = True
    notification.save(update_fields=['is_read'])

    if notification.link:
        return redirect(notification.link)

    return redirect('/panel/notifications/')


@login_required
def mark_all_notifications_read(request):
    guard_response = panel_guard(request)
    if guard_response:
        return guard_response

    if request.method == 'POST':
        Notification.objects.filter(user=request.user, is_read=False).update(is_read=True)
        messages.success(request, 'Todas las notificaciones fueron marcadas como leídas.')

    return redirect('/panel/notifications/')
'''

if "def panel_notifications(request):" not in text:
    text += block

p.write_text(text, encoding="utf-8")
print("Vistas de notificaciones añadidas")
