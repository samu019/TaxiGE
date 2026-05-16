from pathlib import Path

p = Path("accounts/admin.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

old = """@admin.register(SaaSPaymentHistory)
class SaaSPaymentHistoryAdmin(admin.ModelAdmin):"""

new = """@admin.register(SaaSPaymentHistory)
class SaaSPaymentHistoryAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        previous_status = None

        if change and obj.pk:
            try:
                previous_status = SaaSPaymentHistory.objects.get(pk=obj.pk).status
            except SaaSPaymentHistory.DoesNotExist:
                previous_status = None

        if obj.status in [SaaSPaymentHistory.STATUS_APPROVED, SaaSPaymentHistory.STATUS_REJECTED]:
            obj.reviewed_by = request.user
            obj.reviewed_at = timezone.now()

        super().save_model(request, obj, form, change)

        if obj.status == SaaSPaymentHistory.STATUS_APPROVED and previous_status != SaaSPaymentHistory.STATUS_APPROVED:
            subscription = obj.subscription
            today = timezone.localdate()

            subscription.start_date = today
            subscription.end_date = today + timedelta(days=30)
            subscription.status = SaaSSubscription.STATUS_ACTIVE
            subscription.last_payment_reference = obj.reference
            subscription.last_payment_receipt = obj.receipt
            subscription.notes = f'Renovación aprobada desde historial de pagos SaaS. Pago ID: {obj.id}'
            subscription.save()

            try:
                Notification.objects.create(
                    user=obj.user,
                    title='Pago SaaS aprobado',
                    message=f'Tu pago SaaS fue aprobado. Tu suscripción queda activa hasta {subscription.end_date}.',
                    level='success',
                    link='/panel/'
                )
            except Exception:
                pass

        if obj.status == SaaSPaymentHistory.STATUS_REJECTED and previous_status != SaaSPaymentHistory.STATUS_REJECTED:
            try:
                Notification.objects.create(
                    user=obj.user,
                    title='Pago SaaS rechazado',
                    message='Tu comprobante de renovación SaaS fue rechazado. Revisa la referencia o contacta con administración.',
                    level='danger',
                    link='/panel/subscription/renew/'
                )
            except Exception:
                pass
"""

if "Pago SaaS aprobado" not in text:
    text = text.replace(old, new, 1)

p.write_text(text, encoding="utf-8")
print("Aprobación/rechazo de historial SaaS conectada a suscripción.")
