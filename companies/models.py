from django.conf import settings
from django.db import models


class Company(models.Model):
    STATUS_ACTIVE = 'active'
    STATUS_SUSPENDED = 'suspended'
    STATUS_PENDING = 'pending'

    STATUS_CHOICES = [
        (STATUS_ACTIVE, 'Activa'),
        (STATUS_SUSPENDED, 'Suspendida'),
        (STATUS_PENDING, 'Pendiente'),
    ]

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='taxi_companies'
    )

    name = models.CharField(max_length=150)
    legal_name = models.CharField(max_length=200, blank=True, null=True)
    tax_id = models.CharField(max_length=100, blank=True, null=True)

    phone = models.CharField(max_length=30)
    email = models.EmailField(blank=True, null=True)

    city = models.CharField(max_length=100, default='Malabo')
    address = models.CharField(max_length=255, blank=True, null=True)

    logo = models.ImageField(upload_to='companies/logos/', blank=True, null=True)

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
        related_name='created_companies'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Empresa de taxi'
        verbose_name_plural = 'Empresas de taxis'
        ordering = ['-created_at']

    def __str__(self):
        return self.name
