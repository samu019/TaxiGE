from pathlib import Path

p = Path("accounts/models.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

if "class SaaSSubscription" not in text:
    block = r'''

class SaaSSubscription(models.Model):
    STATUS_ACTIVE = 'active'
    STATUS_EXPIRED = 'expired'
    STATUS_SUSPENDED = 'suspended'
    STATUS_PENDING = 'pending'

    STATUS_CHOICES = [
        (STATUS_ACTIVE, 'Activa'),
        (STATUS_EXPIRED, 'Expirada'),
        (STATUS_SUSPENDED, 'Suspendida'),
        (STATUS_PENDING, 'Pendiente'),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='saas_subscription'
    )

    monthly_fee = models.DecimalField(max_digits=12, decimal_places=2, default=50000)

    start_date = models.DateField()
    end_date = models.DateField()

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_ACTIVE)

    last_payment_reference = models.CharField(max_length=120, blank=True, null=True)
    last_payment_receipt = models.FileField(upload_to='subscriptions/receipts/', blank=True, null=True)

    notes = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Suscripción SaaS'
        verbose_name_plural = 'Suscripciones SaaS'
        ordering = ['-end_date', '-created_at']

    def __str__(self):
        return f'{self.user} - {self.get_status_display()} hasta {self.end_date}'

    def is_valid(self):
        from django.utils import timezone
        return self.status == self.STATUS_ACTIVE and self.end_date >= timezone.localdate()
'''
    text += block

p.write_text(text, encoding="utf-8")
print("Modelo SaaSSubscription agregado.")
