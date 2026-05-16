from django.conf import settings
from django.db import models
from companies.models import Company
from vehicles.models import Vehicle
from drivers.models import Driver


class VehicleDamage(models.Model):
    STATUS_PENDING = 'pending'
    STATUS_IN_REPAIR = 'in_repair'
    STATUS_REPAIRED = 'repaired'
    STATUS_CHARGED = 'charged'

    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pendiente'),
        (STATUS_IN_REPAIR, 'En reparación'),
        (STATUS_REPAIRED, 'Reparado'),
        (STATUS_CHARGED, 'Cobrado al conductor'),
    ]

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='damages'
    )

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        related_name='damages'
    )

    driver = models.ForeignKey(
        Driver,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='damages'
    )

    title = models.CharField(max_length=180)
    description = models.TextField()

    estimated_cost = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    final_cost = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    photo = models.ImageField(upload_to='damages/photos/', blank=True, null=True)

    damage_date = models.DateField()
    repaired_date = models.DateField(blank=True, null=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING
    )

    registered_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='registered_damages'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Daño de taxi'
        verbose_name_plural = 'Daños de taxis'
        ordering = ['-damage_date', '-created_at']

    def __str__(self):
        return f"{self.vehicle} - {self.title}"
