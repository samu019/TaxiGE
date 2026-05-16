from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8")

old = """    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')

    return render_panel(request, 'dashboard/notifications.html', {
        'notifications': notifications,
        'unread_count': notifications.filter(is_read=False).count(),
    })"""

new = """    filter_type = request.GET.get('filter', 'all')

    notifications = Notification.objects.filter(user=request.user)

    total_count = notifications.count()
    unread_count = notifications.filter(is_read=False).count()
    read_count = notifications.filter(is_read=True).count()

    if filter_type == 'unread':
        notifications = notifications.filter(is_read=False)
    elif filter_type == 'read':
        notifications = notifications.filter(is_read=True)

    notifications = notifications.order_by('-created_at')

    return render_panel(request, 'dashboard/notifications.html', {
        'notifications': notifications,
        'total_count': total_count,
        'unread_count': unread_count,
        'read_count': read_count,
        'active_filter': filter_type,
    })"""

text = text.replace(old, new)

p.write_text(text, encoding="utf-8")
print("Filtros de notificaciones añadidos a la vista")
