from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8")

text = text.replace(
"""    if request.method == 'POST':
        vehicle.delete()""",
"""    if request.method == 'POST':
        if not user_can_edit_data(request.user, vehicle.company):
            messages.error(request, 'No tienes permiso para eliminar este taxi.')
            return redirect('/panel/vehicles/')
        vehicle.delete()"""
)

text = text.replace(
"""    if request.method == 'POST':
        driver.delete()""",
"""    if request.method == 'POST':
        if not user_can_edit_data(request.user, driver.company):
            messages.error(request, 'No tienes permiso para eliminar este conductor.')
            return redirect('/panel/drivers/')
        driver.delete()"""
)

text = text.replace(
"""    if request.method == 'POST':
        payment.delete()""",
"""    if request.method == 'POST':
        if not user_can_edit_data(request.user, payment.company):
            messages.error(request, 'No tienes permiso para eliminar este pago.')
            return redirect('/panel/payments/')
        payment.delete()"""
)

text = text.replace(
"""    if request.method == 'POST':
        damage.delete()""",
"""    if request.method == 'POST':
        if not user_can_edit_data(request.user, damage.company):
            messages.error(request, 'No tienes permiso para eliminar este daño.')
            return redirect('/panel/damages/')
        damage.delete()"""
)

p.write_text(text, encoding="utf-8")
print("Eliminaciones protegidas exactamente")
