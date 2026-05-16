from pathlib import Path

p = Path("config/settings.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

start = text.find("DATABASES =")
if start == -1:
    raise SystemExit("No se encontró DATABASES")

# Buscar el siguiente bloque importante después de DATABASES
markers = [
    "\nAUTH_PASSWORD_VALIDATORS",
    "\nLANGUAGE_CODE",
    "\nTIME_ZONE",
    "\nSTATIC_URL",
]

end_positions = [text.find(m, start) for m in markers if text.find(m, start) != -1]
if not end_positions:
    raise SystemExit("No se encontró el final seguro del bloque DATABASES")

end = min(end_positions)

sqlite_config = """DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

"""

text = text[:start] + sqlite_config + text[end:].lstrip()

p.write_text(text, encoding="utf-8")
print("DATABASES restaurado a SQLite correctamente")
