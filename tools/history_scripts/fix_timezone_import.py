from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8-sig").replace("\ufeff", "")

if "from django.utils import timezone" not in text:
    text = text.replace(
        "from django.shortcuts import render, redirect, get_object_or_404",
        "from django.shortcuts import render, redirect, get_object_or_404\nfrom django.utils import timezone"
    )

if "from django.utils import timezone" not in text:
    text = "from django.utils import timezone\n" + text

p.write_text(text, encoding="utf-8")
print("OK: timezone importado")
