from pathlib import Path
import re

p = Path("config/settings.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

storages = '''
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
'''

text = re.sub(
    r"STORAGES\s*=\s*\{.*?\n\}",
    storages.strip(),
    text,
    flags=re.DOTALL
)

if "STORAGES =" not in text:
    text += "\n\n" + storages

p.write_text(text, encoding="utf-8")
print("STORAGES corregido con default y staticfiles.")
