from pathlib import Path

p = Path("accounts/models.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

if "class SaaSPaymentSettings" not in text:
    block = r'''

class SaaSPaymentSettings(models.Model):
    activation_fee = models.DecimalField(max_digits=12, decimal_places=2, default=50000)

    primary_bank_name = models.CharField(max_length=100, default='BANGE')
    primary_account_holder = models.CharField(max_length=150, default='TaxiGE Platform')
    primary_account_number = models.CharField(max_length=100, default='100200300400')

    secondary_bank_name = models.CharField(max_length=100, default='ECOBANK')
    secondary_account_holder = models.CharField(max_length=150, default='TaxiGE Platform')
    secondary_account_number = models.CharField(max_length=100, default='Pendiente de configurar')

    payment_instructions = models.TextField(
        default='Realiza el pago de activación y sube el comprobante. Tu solicitud será revisada por el administrador antes de activar tu cuenta de propietario.'
    )

    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Configuración de pago SaaS'
        verbose_name_plural = 'Configuración de pagos SaaS'

    def __str__(self):
        return f'Pago SaaS - {self.activation_fee} XAF'

    @classmethod
    def get_active(cls):
        obj = cls.objects.filter(is_active=True).first()
        if obj:
            return obj
        return cls.objects.create()
'''
    text += block

p.write_text(text, encoding="utf-8")
print("Modelo SaaSPaymentSettings agregado.")
