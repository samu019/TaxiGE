from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8")

extra = r'''

@login_required
def panel_vehicle_delete(request, vehicle_id):
    guard_response = panel_guard(request)
    if guard_response:
        return guard_response

    vehicle = get_object_or_404(Vehicle, id=vehicle_id, company__owner=request.user)

    if request.method == 'POST':
        vehicle.delete()
        return redirect('/panel/vehicles/')

    return render(request, 'dashboard/panel_confirm_delete.html', {
        'title': 'Eliminar taxi',
        'object_name': vehicle.plate_number,
        'cancel_url': '/panel/vehicles/',
    })


@login_required
def panel_driver_delete(request, driver_id):
    guard_response = panel_guard(request)
    if guard_response:
        return guard_response

    driver = get_object_or_404(Driver, id=driver_id, company__owner=request.user)

    if request.method == 'POST':
        driver.delete()
        return redirect('/panel/drivers/')

    return render(request, 'dashboard/panel_confirm_delete.html', {
        'title': 'Eliminar conductor',
        'object_name': driver.full_name,
        'cancel_url': '/panel/drivers/',
    })


@login_required
def panel_payment_delete(request, payment_id):
    guard_response = panel_guard(request)
    if guard_response:
        return guard_response

    payment = get_object_or_404(DriverPayment, id=payment_id, company__owner=request.user)

    if request.method == 'POST':
        payment.delete()
        return redirect('/panel/payments/')

    return render(request, 'dashboard/panel_confirm_delete.html', {
        'title': 'Eliminar pago',
        'object_name': f'{payment.driver.full_name} - {payment.payment_date}',
        'cancel_url': '/panel/payments/',
    })


@login_required
def panel_damage_delete(request, damage_id):
    guard_response = panel_guard(request)
    if guard_response:
        return guard_response

    damage = get_object_or_404(VehicleDamage, id=damage_id, company__owner=request.user)

    if request.method == 'POST':
        damage.delete()
        return redirect('/panel/damages/')

    return render(request, 'dashboard/panel_confirm_delete.html', {
        'title': 'Eliminar daño',
        'object_name': damage.title,
        'cancel_url': '/panel/damages/',
    })
'''

if "def panel_vehicle_delete" not in text:
    text += extra

p.write_text(text, encoding="utf-8")
print("OK: vistas delete agregadas")
