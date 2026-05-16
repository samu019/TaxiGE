# TaxiGE Platform - Despliegue

## Requisitos

- Ubuntu 24.04 LTS
- Python 3.11
- PostgreSQL
- Nginx
- Gunicorn
- Certbot

## Pasos generales

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic
gunicorn config.wsgi:application --bind 127.0.0.1:8000



