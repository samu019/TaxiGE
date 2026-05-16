from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8-sig").replace("\ufeff", "")

needle = "    context = {\n"
insert = """    filter_type = request.GET.get('filter', 'month')
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')

"""

if "'active_filter': filter_type" in text and insert.strip() not in text:
    text = text.replace(needle, insert + needle, 1)

p.write_text(text, encoding="utf-8")
print("OK: filter_type definido antes del context")
