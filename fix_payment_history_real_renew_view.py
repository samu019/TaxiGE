from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

# Asegurar import
if "SaaSPaymentHistory" not in text.split("\n")[0:80].__str__():
    text = text.replace(
        "from accounts.models import SaaSSubscription,",
        "from accounts.models import SaaSSubscription, SaaSPaymentHistory,",
        1
    )

old = """        subscription.last_payment_reference = reference
        subscription.last_payment_receipt = receipt
        subscription.status = SaaSSubscription.STATUS_PENDING
        subscription.notes = 'Comprobante de renovación enviado por el usuario. Pendiente de revisión administrativa.'
        subscription.save()
"""

new = """        subscription.last_payment_reference = reference
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
"""

if "SaaSPaymentHistory.objects.create(" not in text:
    if old not in text:
        raise SystemExit("No se encontró el bloque real de guardado de renovación.")
    text = text.replace(old, new, 1)

p.write_text(text, encoding="utf-8")
print("Historial SaaS conectado al formulario real de renovación.")
