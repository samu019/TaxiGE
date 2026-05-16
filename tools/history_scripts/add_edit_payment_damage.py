from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8")

insert_after = """def panel_payment_create(request):
    guard_response = panel_guard(request)
    if guard_response:
        return guard_response

    company = get_user_company(request.user)

    if not company:
        return HttpResponseForbidden(
            'No tienes una empresa activa asignada. Contacta con el soporte de TaxiGE.'
        )

    if request.method == 'POST':
        form = DriverPaymentForm(request.POST, company=company)

        if form.is_valid():
            payment = form.save(commit=False)
            payment.company = company
            payment.registered_by = request.user
            payment.status = calculate_payment_status(
                payment.expected_amount,
                payment.paid_amount
            )
            payment.save()
            return redirect('/panel/payments/')
    else:
        form = DriverPaymentForm(company=company)

    return render(request, 'dashboard/panel_payment_form.html', {
        'form': form,
        'title': 'Registrar pago',
        'button_text': 'Guardar pago',
    })
"""

payment_edit = """
@login_required
def panel_payment_edit(request, payment_id):
    guard_response = panel_guard(request)
    if guard_response:
        return guard_response

    company = get_user_company(request.user)

    payment = get_object_or_404(
        DriverPayment,
        id=payment_id,
        company__owner=request.user
    )

    if request.method == 'POST':
        form = DriverPaymentForm(request.POST, instance=payment, company=company)

        if form.is_valid():
            payment = form.save(commit=False)
            payment.company = company
            payment.registered_by = request.user
            payment.status = calculate_payment_status(
                payment.expected_amount,
                payment.paid_amount
            )
            payment.save()
            return redirect('/panel/payments/')
    else:
        form = DriverPaymentForm(instance=payment, company=company)

    return render(request, 'dashboard/panel_payment_form.html', {
        'form': form,
        'title': 'Editar pago',
        'button_text': 'Guardar cambios',
    })
"""

if "def panel_payment_edit" not in text:
    text = text.replace(insert_after, insert_after + payment_edit)

insert_after_damage = """def panel_damage_create(request):
    guard_response = panel_guard(request)
    if guard_response:
        return guard_response

    company = get_user_company(request.user)

    if not company:
        return HttpResponseForbidden(
            'No tienes una empresa activa asignada. Contacta con el soporte de TaxiGE.'
        )

    if request.method == 'POST':
        form = VehicleDamageForm(request.POST, request.FILES, company=company)

        if form.is_valid():
            damage = form.save(commit=False)
            damage.company = company
            damage.registered_by = request.user
            damage.save()
            return redirect('/panel/damages/')
    else:
        form = VehicleDamageForm(company=company)

    return render(request, 'dashboard/panel_damage_form.html', {
        'form': form,
        'title': 'Registrar daño',
        'button_text': 'Guardar daño',
    })
"""

damage_edit = """
@login_required
def panel_damage_edit(request, damage_id):
    guard_response = panel_guard(request)
    if guard_response:
        return guard_response

    company = get_user_company(request.user)

    damage = get_object_or_404(
        VehicleDamage,
        id=damage_id,
        company__owner=request.user
    )

    if request.method == 'POST':
        form = VehicleDamageForm(request.POST, request.FILES, instance=damage, company=company)

        if form.is_valid():
            damage = form.save(commit=False)
            damage.company = company
            damage.registered_by = request.user
            damage.save()
            return redirect('/panel/damages/')
    else:
        form = VehicleDamageForm(instance=damage, company=company)

    return render(request, 'dashboard/panel_damage_form.html', {
        'form': form,
        'title': 'Editar daño',
        'button_text': 'Guardar cambios',
    })
"""

if "def panel_damage_edit" not in text:
    text = text.replace(insert_after_damage, insert_after_damage + damage_edit)

p.write_text(text, encoding="utf-8")
print("OK: views.py actualizado con edición de pagos y daños")
