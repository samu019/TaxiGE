from pathlib import Path

p = Path("config/settings.py")
text = p.read_text(encoding="utf-8")

if "'notifications'," not in text and '"notifications",' not in text:
    if "'sharing'," in text:
        text = text.replace("'sharing',", "'sharing',\n    'notifications',")
    else:
        text = text.replace("INSTALLED_APPS = [", "INSTALLED_APPS = [\n    'notifications',")

p.write_text(text, encoding="utf-8")
print("App notifications activada")
