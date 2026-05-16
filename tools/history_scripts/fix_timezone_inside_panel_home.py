from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8-sig").replace("\ufeff", "")

old = """def panel_home(request):
    guard_response = panel_guard(request)"""

new = """def panel_home(request):
    from django.utils import timezone

    guard_response = panel_guard(request)"""

if old in text and "def panel_home(request):\n    from django.utils import timezone" not in text:
    text = text.replace(old, new, 1)

p.write_text(text, encoding="utf-8")
print("OK: timezone importado dentro de panel_home")
