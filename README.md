# TaxiGE Platform

Plataforma SaaS profesional para la gestión de empresas de taxis en Guinea Ecuatorial.

## Funcionalidades principales

- Multiempresa
- Gestión de taxis
- Gestión de conductores
- Registro de pagos
- Control de deudas
- Gestión de daños
- Dashboard con KPIs y gráficos
- Exportación a Excel y PDF
- Calendario operativo
- Notificaciones internas
- Compartición de acceso con roles
- Auditoría de acciones
- Control de permisos
- Modo oscuro
- Diseño responsive

## Roles disponibles

- Propietario
- Gestor
- Auditor
- Solo lectura

## Tecnologías

- Python 3.11
- Django 5.2
- SQLite (desarrollo)
- Bootstrap/Tailwind personalizado
- ReportLab
- OpenPyXL

## Instalación

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver







