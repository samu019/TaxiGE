from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8")

replacements = {
"""    if request.method == 'POST':
        vehicle.delete()
        messages.success(request, 'Taxi eliminado correctamente.')""":
"""    if request.method == 'POST':
        if not user_can_edit_data(request.user, vehicle.company):
            messages.error(request, 'No tienes permiso para eliminar este taxi.')
            return redirect('/panel/vehicles/')
        vehicle.delete()
        messages.success(request, 'Taxi eliminado correctamente.')""",

"""    if request.method == 'POST':
        driver.delete()
        messages.success(request, 'Conductor eliminado correctamente.')""":
"""    if request.method == 'POST':
        if not user_can_edit_data(request.user, driver.company):
            messages.error(request, 'No tienes permiso para eliminar este conductor.')
            return redirect('/panel/drivers/')
        driver.delete()
        messages.success(request, 'Conductor eliminado correctamente.')""",

"""    if request.method == 'POST':
        payment.delete()
        messages.success(request, 'Pago eliminado correctamente.')""":
"""    if request.method == 'POST':
        if not user_can_edit_data(request.user, payment.company):
            messages.error(request, 'No tienes permiso para eliminar este pago.')
            return redirect('/panel/payments/')
        payment.delete()
        messages.success(request, 'Pago eliminado correctamente.')""",

"""    if request.method == 'POST':
        damage.delete()
        messages.success(request, 'Daño eliminado correctamente.')""":
"""    if request.method == 'POST':
        if not user_can_edit_data(request.user, damage.company):
            messages.error(request, 'No tienes permiso para eliminar este daño.')
            return redirect('/panel/damages/')
        damage.delete()
        messages.success(request, 'Daño eliminado correctamente.')""",
}

for old, new in replacements.items():
    text = text.replace(old, new)

p.write_text(text, encoding="utf-8")
print("Eliminaciones protegidas")
