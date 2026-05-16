from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8")

old = """    events = sorted(events, key=lambda x: x['date'])

    return render_panel(request, 'dashboard/calendar.html', {"""

new = """    events = sorted(events, key=lambda x: x['date'])
    visible_events = events[:8]

    return render_panel(request, 'dashboard/calendar.html', {"""

text = text.replace(old, new)

text = text.replace(
"""        'events': events,""",
"""        'events': visible_events,
        'total_events_count': len(events),"""
)

p.write_text(text, encoding="utf-8")
print("Calendario limitado a 8 eventos visibles")
