from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8")

replacements = {
"""    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES, instance=vehicle)""":
"""    if request.method == 'POST':
        if not user_can_edit_data(request.user, vehicle.company):
            messages.error(request, 'No tienes permiso para editar este taxi.')
            return redirect('/panel/vehicles/')
        form = VehicleForm(request.POST, request.FILES, instance=vehicle)""",

"""    if request.method == 'POST':
        form = DriverForm(request.POST, request.FILES, instance=driver, company=company)""":
"""    if request.method == 'POST':
        if not user_can_edit_data(request.user, driver.company):
            messages.error(request, 'No tienes permiso para editar este conductor.')
            return redirect('/panel/drivers/')
        form = DriverForm(request.POST, request.FILES, instance=driver, company=company)""",

"""    if request.method == 'POST':
        form = DriverPaymentForm(request.POST, instance=payment, company=company)""":
"""    if request.method == 'POST':
        if not user_can_edit_data(request.user, payment.company):
            messages.error(request, 'No tienes permiso para editar este pago.')
            return redirect('/panel/payments/')
        form = DriverPaymentForm(request.POST, instance=payment, company=company)""",

"""    if request.method == 'POST':
        form = VehicleDamageForm(request.POST, request.FILES, instance=damage, company=company)""":
"""    if request.method == 'POST':
        if not user_can_edit_data(request.user, damage.company):
            messages.error(request, 'No tienes permiso para editar este daño.')
            return redirect('/panel/damages/')
        form = VehicleDamageForm(request.POST, request.FILES, instance=damage, company=company)""",
}

for old, new in replacements.items():
    text = text.replace(old, new)

p.write_text(text, encoding="utf-8")
print("Ediciones protegidas por permisos")
