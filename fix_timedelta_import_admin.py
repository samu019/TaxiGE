from pathlib import Path

p = Path("accounts/admin.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

if "from datetime import timedelta" not in text.splitlines()[:20]:
    text = text.replace(
        "from django.utils import timezone",
        "from django.utils import timezone\nfrom datetime import timedelta",
        1
    )

p.write_text(text, encoding="utf-8")
print("Import global de timedelta corregido.")
