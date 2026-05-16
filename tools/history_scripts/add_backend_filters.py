from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8-sig").replace("\ufeff", "")

if "from django.db.models import Q" not in text:
    text = text.replace(
        "from django.db.models import Sum",
        "from django.db.models import Sum, Q"
    )

replacements = [
    (
        "vehicles = Vehicle.objects.filter(company__owner=request.user)",
        """vehicles = Vehicle.objects.filter(company__owner=request.user)

    q = request.GET.get('q', '').strip()
    status = request.GET.get('status', '').strip()

    if q:
        vehicles = vehicles.filter(
            Q(plate_number__icontains=q) |
            Q(brand__icontains=q) |
            Q(model__icontains=q) |
            Q(color__icontains=q)
        )

    if status:
        vehicles = vehicles.filter(status=status)"""
    ),
    (
        "drivers = Driver.objects.filter(company__owner=request.user)",
        """drivers = Driver.objects.filter(company__owner=request.user)

    q = request.GET.get('q', '').strip()
    status = request.GET.get('status', '').strip()

    if q:
        drivers = drivers.filter(
            Q(full_name__icontains=q) |
            Q(phone__icontains=q) |
            Q(identity_number__icontains=q) |
            Q(license_number__icontains=q) |
            Q(assigned_vehicle__plate_number__icontains=q)
        )

    if status:
        drivers = drivers.filter(status=status)"""
    ),
    (
        "payments = DriverPayment.objects.filter(company__owner=request.user)",
        """payments = DriverPayment.objects.filter(company__owner=request.user)

    q = request.GET.get('q', '').strip()
    status = request.GET.get('status', '').strip()

    if q:
        payments = payments.filter(
            Q(driver__full_name__icontains=q) |
            Q(vehicle__plate_number__icontains=q) |
            Q(notes__icontains=q)
        )

    if status:
        payments = payments.filter(status=status)"""
    ),
    (
        "damages = VehicleDamage.objects.filter(company__owner=request.user)",
        """damages = VehicleDamage.objects.filter(company__owner=request.user)

    q = request.GET.get('q', '').strip()
    status = request.GET.get('status', '').strip()

    if q:
        damages = damages.filter(
            Q(title__icontains=q) |
            Q(description__icontains=q) |
            Q(vehicle__plate_number__icontains=q) |
            Q(driver__full_name__icontains=q)
        )

    if status:
        damages = damages.filter(status=status)"""
    ),
]

for old, new in replacements:
    if old in text and new not in text:
        text = text.replace(old, new, 1)

p.write_text(text, encoding="utf-8")
print("OK: filtros backend agregados")
