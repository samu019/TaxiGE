from pathlib import Path

p = Path("config/settings.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

# Imports necesarios
if "import dj_database_url" not in text:
    text = text.replace("import os", "import os\nimport dj_database_url", 1)

# ALLOWED_HOSTS Render
text = text.replace(
    "ALLOWED_HOSTS = ['127.0.0.1', 'localhost']",
    "ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.onrender.com']"
)

# WhiteNoise middleware después de SecurityMiddleware
if "whitenoise.middleware.WhiteNoiseMiddleware" not in text:
    text = text.replace(
        "'django.middleware.security.SecurityMiddleware',",
        "'django.middleware.security.SecurityMiddleware',\n    'whitenoise.middleware.WhiteNoiseMiddleware',",
        1
    )

# STATIC_ROOT y storage
if "STATIC_ROOT" not in text:
    text = text.replace(
        "STATIC_URL = 'static/'",
        "STATIC_URL = 'static/'\nSTATIC_ROOT = BASE_DIR / 'staticfiles'",
        1
    )

if "STORAGES =" not in text:
    text += """

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
"""

# DATABASE_URL para Render PostgreSQL o fallback SQLite
if "dj_database_url.config" not in text:
    text += """

if config('DATABASE_URL', default=''):
    DATABASES['default'] = dj_database_url.config(
        default=config('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=True
    )
"""

p.write_text(text, encoding="utf-8")
print("settings.py preparado para Render.")
