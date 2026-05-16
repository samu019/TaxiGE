from pathlib import Path

p = Path('dashboard/views.py')
text = p.read_text(encoding='utf-8-sig').replace('\ufeff','')

old_block = '''    payments = DriverPayment.objects.filter(company__owner=user)
    damages = VehicleDamage.objects.filter(company__owner=user)

    total_expected = payments.aggregate(total=Sum('expected_amount'))['total'] or Decimal('0')
'''

new_block = '''    payments = DriverPayment.objects.filter(company__owner=user)
    damages = VehicleDamage.objects.filter(company__owner=user)

    today = timezone.localdate()
    filter_type = request.GET.get('filter', 'month')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if filter_type == 'today':
        payments = payments.filter(payment_date=today)
        damages = damages.filter(damage_date=today)
    elif filter_type == 'week':
        week_start = today - timedelta(days=7)
        payments = payments.filter(payment_date__gte=week_start)
        damages = damages.filter(damage_date__gte=week_start)
    elif filter_type == 'custom' and start_date and end_date:
        payments = payments.filter(payment_date__range=[start_date,end_date])
        damages = damages.filter(damage_date__range=[start_date,end_date])
    else:
        payments = payments.filter(payment_date__year=today.year,payment_date__month=today.month)
        damages = damages.filter(damage_date__year=today.year,damage_date__month=today.month)

    total_expected = payments.aggregate(total=Sum('expected_amount'))['total'] or Decimal('0')
'''

if old_block in text:
    text = text.replace(old_block,new_block)

context_old = """        'recent_payments': payments.order_by('-payment_date', '-created_at')[:5],
        'recent_damages': damages.order_by('-damage_date', '-created_at')[:5],
"""

context_new = """        'recent_payments': payments.order_by('-payment_date', '-created_at')[:5],
        'recent_damages': damages.order_by('-damage_date', '-created_at')[:5],

        'active_filter': filter_type,
        'start_date': start_date or '',
        'end_date': end_date or '',
"""

if context_old in text:
    text = text.replace(context_old,context_new)

p.write_text(text,encoding='utf-8')
print("OK: filtros backend agregados")
