from pathlib import Path
import re

path = Path("dashboard/views.py")
text = path.read_text(encoding="utf-8")

original = text

# 1. Asegurar import Q
if "from django.db.models import Q" not in text:
    if "from django.db.models import" in text:
        text = re.sub(
            r"from django\.db\.models import ([^\n]+)",
            lambda m: m.group(0) if "Q" in m.group(1).split(",") else m.group(0) + ", Q",
            text,
            count=1
        )
    else:
        text = "from django.db.models import Q\n" + text

# 2. Añadir helpers de acceso compartido
helper = '''
def user_company_access_q(user):
    """
    Permite ver datos de empresas donde el usuario es dueño
    o miembro compartido activo.
    """
    return (
        Q(company__owner=user) |
        Q(company__members__user=user, company__members__is_active=True)
    )


def user_company_direct_access_q(user):
    """
    Permite ver empresas donde el usuario es dueño
    o miembro compartido activo.
    """
    return (
        Q(owner=user) |
        Q(members__user=user, members__is_active=True)
    )

'''

if "def user_company_access_q(user):" not in text:
    marker = "@login_required"
    if marker in text:
        text = text.replace(marker, helper + marker, 1)
    else:
        text += "\n\n" + helper

# 3. Reemplazos seguros en filtros normales
replacements = {
    "Vehicle.objects.filter(company__owner=request.user)": "Vehicle.objects.filter(user_company_access_q(request.user))",
    "Driver.objects.filter(company__owner=request.user)": "Driver.objects.filter(user_company_access_q(request.user))",
    "DriverPayment.objects.filter(company__owner=request.user)": "DriverPayment.objects.filter(user_company_access_q(request.user))",
    "VehicleDamage.objects.filter(company__owner=request.user)": "VehicleDamage.objects.filter(user_company_access_q(request.user))",
    "Company.objects.filter(owner=request.user)": "Company.objects.filter(user_company_direct_access_q(request.user))",
}

for old, new in replacements.items():
    text = text.replace(old, new)

# 4. Reemplazos seguros en get_object_or_404
object_replacements = {
    "get_object_or_404(Vehicle, id=vehicle_id, company__owner=request.user)": "get_object_or_404(Vehicle.objects.filter(user_company_access_q(request.user)), id=vehicle_id)",
    "get_object_or_404(Driver, id=driver_id, company__owner=request.user)": "get_object_or_404(Driver.objects.filter(user_company_access_q(request.user)), id=driver_id)",
    "get_object_or_404(DriverPayment, id=payment_id, company__owner=request.user)": "get_object_or_404(DriverPayment.objects.filter(user_company_access_q(request.user)), id=payment_id)",
    "get_object_or_404(VehicleDamage, id=damage_id, company__owner=request.user)": "get_object_or_404(VehicleDamage.objects.filter(user_company_access_q(request.user)), id=damage_id)",
}

for old, new in object_replacements.items():
    text = text.replace(old, new)

# 5. Reemplazo controlado de líneas sueltas dentro de .filter(...)
text = text.replace("company__owner=request.user", "user_company_access_q(request.user)")

path.write_text(text, encoding="utf-8")

print("MODIFICADO:", path)
print("Cambios aplicados:", original != text)
