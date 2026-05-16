from pathlib import Path

p = Path("accounts/models.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

if "class SaaSPaymentHistory" not in text:
    block = r'''

class SaaSPaymentHistory(models.Model):
    STATUS_PENDING = 'pending'
    STATUS_APPROVED = 'approved'
    STATUS_REJECTED = 'rejected'

    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pendiente'),
        (STATUS_APPROVED, 'Aprobado'),
        (STATUS_REJECTED, 'Rechazado'),
    ]

    subscription = models.ForeignKey(
        SaaSSubscription,
        on_delete=models.CASCADE,
        related_name='payment_history'
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='saas_payment_history'
    )

    amount = models.DecimalField(max_digits=12, decimal_places=2, default=50000)
    reference = models.CharField(max_length=120)
    receipt = models.FileField(upload_to='subscriptions/payment_history/')

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)

    reviewed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='reviewed_saas_payments'
    )

    reviewed_at = models.DateTimeField(blank=True, null=True)
    admin_note = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Pago SaaS'
        verbose_name_plural = 'Historial de pagos SaaS'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user} - {self.amount} XAF - {self.get_status_display()}'
'''
    text += block

p.write_text(text, encoding="utf-8")
print("Modelo SaaSPaymentHistory agregado.")
