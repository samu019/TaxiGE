from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

old = """@login_required
def panel_subscription_renew(request):
    subscription = None

    try:
        subscription = request.user.saas_subscription
    except Exception:
        subscription = None

    payment_settings = None
    try:
        from accounts.models import SaaSPaymentSettings
        payment_settings = SaaSPaymentSettings.get_active()
    except Exception:
        payment_settings = None

    return render(request, 'dashboard/subscription_renew.html', {
        'subscription': subscription,
        'payment_settings': payment_settings,
    })
"""

new = """@login_required
def panel_subscription_renew(request):
    subscription = None

    try:
        subscription = request.user.saas_subscription
    except Exception:
        subscription = None

    payment_settings = None
    try:
        from accounts.models import SaaSPaymentSettings
        payment_settings = SaaSPaymentSettings.get_active()
    except Exception:
        payment_settings = None

    if request.method == 'POST':
        if not subscription:
            messages.error(request, 'No se encontró una suscripción asociada a tu cuenta.')
            return redirect('/panel/subscription/renew/')

        reference = request.POST.get('payment_reference', '').strip()
        receipt = request.FILES.get('payment_receipt')

        if not reference:
            messages.error(request, 'Debes escribir la referencia del pago.')
            return redirect('/panel/subscription/renew/')

        if not receipt:
            messages.error(request, 'Debes subir el comprobante del pago.')
            return redirect('/panel/subscription/renew/')

        subscription.last_payment_reference = reference
        subscription.last_payment_receipt = receipt
        subscription.status = SaaSSubscription.STATUS_PENDING
        subscription.notes = 'Comprobante de renovación enviado por el usuario. Pendiente de revisión administrativa.'
        subscription.save()

        messages.success(
            request,
            'Comprobante enviado correctamente. Tu renovación queda pendiente de revisión administrativa.'
        )
        return redirect('/panel/subscription/renew/')

    return render(request, 'dashboard/subscription_renew.html', {
        'subscription': subscription,
        'payment_settings': payment_settings,
    })
"""

if old in text:
    text = text.replace(old, new, 1)
else:
    raise SystemExit("No se encontró la vista panel_subscription_renew exacta.")

p.write_text(text, encoding="utf-8")
print("Vista de renovación actualizada con subida de comprobante.")
