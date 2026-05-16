from pathlib import Path
import re

p = Path("config/settings.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

text = re.sub(r"\nAUTH_USER_MODEL\s*=\s*['\"]accounts\.User['\"]\s*\n", "\n", text)

marker = "MIDDLEWARE = ["
if marker in text:
    text = text.replace(marker, "AUTH_USER_MODEL = 'accounts.User'\n\n" + marker, 1)
else:
    text = "AUTH_USER_MODEL = 'accounts.User'\n\n" + text

p.write_text(text, encoding="utf-8")
print("AUTH_USER_MODEL fijado correctamente")
