from django.conf import settings
from django.db import models
from companies.models import Company
from vehicles.models import Vehicle
from drivers.models import Driver


class DriverPayment(models.Model):
    STATUS_PENDING = 'pending'
    STATUS_PAID = 'paid'
    STATUS_PARTIAL = 'partial'
    STATUS_LATE = 'late'

    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pendiente'),
        (STATUS_PAID, 'Pagado'),
        (STATUS_PARTIAL, 'Pago parcial'),
        (STATUS_LATE, 'Atrasado'),
    ]

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='payments'
    )

    driver = models.ForeignKey(
        Driver,
        on_delete=models.CASCADE,
        related_name='payments'
    )

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='payments'
    )

    payment_date = models.DateField()
    expected_amount = models.DecimalField(max_digits=12, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING
    )

    notes = models.TextField(blank=True, null=True)

    registered_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='registered_driver_payments'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def debt_amount(self):
        return self.expected_amount - self.paid_amount

    class Meta:
        verbose_name = 'Pago de conductor'
        verbose_name_plural = 'Pagos de conductores'
        ordering = ['-payment_date', '-created_at']

    def __str__(self):
        return f"{self.driver} - {self.payment_date} - {self.paid_amount}"
