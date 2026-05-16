from pathlib import Path
import re

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

if "SaaSPaymentHistory" not in text.splitlines()[0:100].__str__():
    text = text.replace(
        "from accounts.models import SaaSSubscription,",
        "from accounts.models import SaaSSubscription, SaaSPaymentHistory,",
        1
    )

pattern = r"@login_required\s*\ndef panel_subscription_renew\(request\):.*?(?=\n@login_required|\Z)"

new_view = r'''@login_required
def panel_subscription_renew(request):
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

        SaaSPaymentHistory.objects.create(
            subscription=subscription,
            user=request.user,
            amount=subscription.monthly_fee,
            reference=reference,
            receipt=receipt,
            status=SaaSPaymentHistory.STATUS_PENDING,
        )

        messages.success(
            request,
            'Comprobante enviado correctamente. Tu renovación queda pendiente de revisión administrativa.'
        )
        return redirect('/panel/subscription/renew/')

    return render(request, 'dashboard/subscription_renew.html', {
        'subscription': subscription,
        'payment_settings': payment_settings,
    })

'''

text, count = re.subn(pattern, new_view, text, count=1, flags=re.DOTALL)

if count != 1:
    raise SystemExit("No se pudo reemplazar panel_subscription_renew.")

p.write_text(text, encoding="utf-8")
print("Vista panel_subscription_renew reemplazada correctamente.")
