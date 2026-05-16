from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8")

old = """    events = sorted(events, key=lambda x: x['date'])

    return render_panel(request, 'dashboard/calendar.html', {
        'today': today,
        'events': events,"""

new = """    filter_type = request.GET.get('filter', 'all')

    if filter_type == 'payments':
        events = [e for e in events if e['type'] == 'payment']
    elif filter_type == 'damages':
        events = [e for e in events if e['type'] == 'damage']
    elif filter_type == 'late':
        events = [e for e in events if e['level'] == 'danger']

    events = sorted(events, key=lambda x: x['date'])

    return render_panel(request, 'dashboard/calendar.html', {
        'today': today,
        'events': events,
        'active_filter': filter_type,"""

text = text.replace(old, new)

p.write_text(text, encoding="utf-8")
print("Filtros añadidos al calendario")
