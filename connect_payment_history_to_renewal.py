from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

# Importar modelo
if "SaaSPaymentHistory" not in text:
    text = text.replace(
        "from accounts.models import SaaSSubscription, SaaSPaymentSettings",
        "from accounts.models import SaaSSubscription, SaaSPaymentSettings, SaaSPaymentHistory"
    )

# Crear historial al guardar renovación
marker = """        subscription.last_payment_receipt = form.cleaned_data['receipt']
        subscription.status = SaaSSubscription.STATUS_PENDING
        subscription.save()
"""

replacement = """        subscription.last_payment_receipt = form.cleaned_data['receipt']
        subscription.status = SaaSSubscription.STATUS_PENDING
        subscription.save()

        SaaSPaymentHistory.objects.create(
            subscription=subscription,
            user=request.user,
            amount=subscription.monthly_fee,
            reference=form.cleaned_data['reference'],
            receipt=form.cleaned_data['receipt'],
            status=SaaSPaymentHistory.STATUS_PENDING,
        )
"""

if "SaaSPaymentHistory.objects.create(" not in text:
    text = text.replace(marker, replacement, 1)

p.write_text(text, encoding="utf-8")
print("Creación automática del historial de pagos integrada.")
