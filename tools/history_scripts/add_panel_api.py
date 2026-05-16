from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8")

api_code = r'''

@login_required
def api_panel_summary(request):
    guard_response = panel_guard(request)
    if guard_response:
        return JsonResponse({'ok': False, 'error': 'Acceso denegado'}, status=403)

    user = request.user

    companies = Company.objects.filter(owner=user)
    vehicles = Vehicle.objects.filter(company__owner=user)
    drivers = Driver.objects.filter(company__owner=user)
    payments = DriverPayment.objects.filter(company__owner=user)
    damages = VehicleDamage.objects.filter(company__owner=user)

    total_expected = payments.aggregate(total=Sum('expected_amount'))['total'] or 0
    total_paid = payments.aggregate(total=Sum('paid_amount'))['total'] or 0
    total_debt = total_expected - total_paid
    damages_cost = damages.aggregate(total=Sum('estimated_cost'))['total'] or 0

    data = {
        'companies_count': companies.count(),
        'vehicles_count': vehicles.count(),
        'active_vehicles': vehicles.filter(status='active').count(),
        'drivers_count': drivers.count(),
        'active_drivers': drivers.filter(status='active').count(),
        'payments_count': payments.count(),
        'damages_count': damages.count(),
        'damages_pending': damages.filter(status='pending').count(),
        'total_expected': str(total_expected),
        'total_paid': str(total_paid),
        'total_debt': str(total_debt),
        'damages_cost': str(damages_cost),
    }

    return JsonResponse({
        'ok': True,
        'data': data,
    })


@login_required
def api_panel_vehicles(request):
    guard_response = panel_guard(request)
    if guard_response:
        return JsonResponse({'ok': False, 'error': 'Acceso denegado'}, status=403)

    vehicles = Vehicle.objects.filter(company__owner=request.user).select_related('company').order_by('-created_at')

    data = []
    for v in vehicles:
        data.append({
            'id': v.id,
            'plate_number': v.plate_number,
            'brand': v.brand,
            'model': v.model,
            'color': v.color,
            'year': v.year,
            'daily_target_amount': str(v.daily_target_amount),
            'status': v.status,
            'status_display': v.get_status_display(),
        })

    return JsonResponse({'ok': True, 'data': data})


@login_required
def api_panel_drivers(request):
    guard_response = panel_guard(request)
    if guard_response:
        return JsonResponse({'ok': False, 'error': 'Acceso denegado'}, status=403)

    drivers = Driver.objects.filter(company__owner=request.user).select_related('assigned_vehicle').order_by('-created_at')

    data = []
    for d in drivers:
        data.append({
            'id': d.id,
            'full_name': d.full_name,
            'phone': d.phone,
            'assigned_vehicle': d.assigned_vehicle.plate_number if d.assigned_vehicle else None,
            'daily_payment_amount': str(d.daily_payment_amount),
            'payment_day': d.payment_day,
            'status': d.status,
            'status_display': d.get_status_display(),
        })

    return JsonResponse({'ok': True, 'data': data})


@login_required
def api_panel_payments(request):
    guard_response = panel_guard(request)
    if guard_response:
        return JsonResponse({'ok': False, 'error': 'Acceso denegado'}, status=403)

    payments = DriverPayment.objects.filter(company__owner=request.user).select_related('driver', 'vehicle').order_by('-payment_date', '-created_at')[:100]

    data = []
    for p in payments:
        data.append({
            'id': p.id,
            'driver': p.driver.full_name,
            'vehicle': p.vehicle.plate_number if p.vehicle else None,
            'payment_date': str(p.payment_date),
            'expected_amount': str(p.expected_amount),
            'paid_amount': str(p.paid_amount),
            'debt_amount': str(p.debt_amount),
            'status': p.status,
            'status_display': p.get_status_display(),
        })

    return JsonResponse({'ok': True, 'data': data})


@login_required
def api_panel_damages(request):
    guard_response = panel_guard(request)
    if guard_response:
        return JsonResponse({'ok': False, 'error': 'Acceso denegado'}, status=403)

    damages = VehicleDamage.objects.filter(company__owner=request.user).select_related('driver', 'vehicle').order_by('-damage_date', '-created_at')[:100]

    data = []
    for d in damages:
        data.append({
            'id': d.id,
            'vehicle': d.vehicle.plate_number if d.vehicle else None,
            'driver': d.driver.full_name if d.driver else None,
            'title': d.title,
            'damage_date': str(d.damage_date),
            'estimated_cost': str(d.estimated_cost),
            'final_cost': str(d.final_cost),
            'status': d.status,
            'status_display': d.get_status_display(),
        })

    return JsonResponse({'ok': True, 'data': data})
'''

if "def api_panel_summary" not in text:
    text += api_code

p.write_text(text, encoding="utf-8")
print("OK: API real agregada")
