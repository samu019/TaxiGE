import os
import sys

# Leer el archivo settings.py actual
settings_path = 'config/settings.py'
with open(settings_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Verificar si ya existe configuración de PostgreSQL
if 'postgresql' not in content:
    # Agregar import de dotenv al inicio si no existe
    if 'from dotenv import load_dotenv' not in content:
        content = 'from dotenv import load_dotenv\nimport os\n\nload_dotenv()\n\n' + content
    
    # Buscar la configuración de DATABASES
    import re
    pattern = r'DATABASES\s*=\s*\{[^}]*\}'
    
    postgres_config = '''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'taxige_db'),
        'USER': os.getenv('DB_USER', 'taxige_user'),
        'PASSWORD': os.getenv('DB_PASSWORD', ''),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}'''
    
    # Reemplazar o agregar la configuración
    if re.search(pattern, content):
        content = re.sub(pattern, postgres_config, content, flags=re.DOTALL)
    else:
        content += '\n\n' + postgres_config
    
    # Guardar cambios
    with open(settings_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✓ Configuración de PostgreSQL agregada a settings.py")
else:
    print("✓ La configuración de PostgreSQL ya existe")

