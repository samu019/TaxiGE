from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8")

if "from django.core.paginator import Paginator" not in text:
    text = "from django.core.paginator import Paginator\n" + text

old = """    notifications = notifications.order_by('-created_at')

    return render_panel(request, 'dashboard/notifications.html', {
        'notifications': notifications,
        'total_count': total_count,
        'unread_count': unread_count,
        'read_count': read_count,
        'active_filter': filter_type,
    })"""

new = """    notifications = notifications.order_by('-created_at')

    paginator = Paginator(notifications, 10)
    page_number = request.GET.get('page')
    notifications_page = paginator.get_page(page_number)

    return render_panel(request, 'dashboard/notifications.html', {
        'notifications': notifications_page,
        'total_count': total_count,
        'unread_count': unread_count,
        'read_count': read_count,
        'active_filter': filter_type,
    })"""

text = text.replace(old, new)

p.write_text(text, encoding="utf-8")
print("Paginación añadida a notificaciones")
