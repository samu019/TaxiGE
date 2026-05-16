from django.conf import settings
from django.db import models
from companies.models import Company
from vehicles.models import Vehicle


class Driver(models.Model):
    STATUS_ACTIVE = 'active'
    STATUS_SUSPENDED = 'suspended'
    STATUS_DISMISSED = 'dismissed'
    STATUS_INACTIVE = 'inactive'

    STATUS_CHOICES = [
        (STATUS_ACTIVE, 'Activo'),
        (STATUS_SUSPENDED, 'Suspendido'),
        (STATUS_DISMISSED, 'Despedido'),
        (STATUS_INACTIVE, 'Inactivo'),
    ]

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='drivers'
    )

    assigned_vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='drivers'
    )

    full_name = models.CharField(max_length=180)
    phone = models.CharField(max_length=30)
    email = models.EmailField(blank=True, null=True)

    identity_number = models.CharField(max_length=100, blank=True, null=True)
    license_number = models.CharField(max_length=100, blank=True, null=True)

    address = models.CharField(max_length=255, blank=True, null=True)

    photo = models.ImageField(upload_to='drivers/photos/', blank=True, null=True)
    identity_document = models.FileField(upload_to='drivers/documents/', blank=True, null=True)
    license_document = models.FileField(upload_to='drivers/documents/', blank=True, null=True)

    start_date = models.DateField(blank=True, null=True)

    daily_payment_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    payment_day = models.CharField(
        max_length=50,
        default='Diario',
        help_text='Ejemplo: Diario, Lunes, Viernes, Cada semana'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_ACTIVE
    )

    notes = models.TextField(blank=True, null=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='created_drivers'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Conductor'
        verbose_name_plural = 'Conductores'
        ordering = ['-created_at']

    def __str__(self):
        return self.full_name
