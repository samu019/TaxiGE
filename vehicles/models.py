from django.conf import settings
from django.db import models
from companies.models import Company


class Vehicle(models.Model):
    STATUS_ACTIVE = 'active'
    STATUS_REPAIR = 'repair'
    STATUS_DAMAGED = 'damaged'
    STATUS_INACTIVE = 'inactive'

    STATUS_CHOICES = [
        (STATUS_ACTIVE, 'Activo'),
        (STATUS_REPAIR, 'En reparación'),
        (STATUS_DAMAGED, 'Dañado'),
        (STATUS_INACTIVE, 'Inactivo'),
    ]

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='vehicles'
    )

    internal_code = models.CharField(max_length=50, blank=True, null=True)
    plate_number = models.CharField(max_length=50, unique=True)

    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    year = models.PositiveIntegerField(blank=True, null=True)

    photo = models.ImageField(upload_to='vehicles/photos/', blank=True, null=True)
    registration_document = models.FileField(upload_to='vehicles/documents/', blank=True, null=True)
    insurance_document = models.FileField(upload_to='vehicles/documents/', blank=True, null=True)

    daily_target_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
        help_text='Cantidad que el conductor debe entregar por día'
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
        related_name='created_vehicles'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Taxi'
        verbose_name_plural = 'Taxis'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.plate_number} - {self.brand}"
