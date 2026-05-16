from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models


class User(AbstractUser):
    ROLE_PLATFORM_OWNER = 'platform_owner'
    ROLE_ADMIN = 'admin'
    ROLE_USER = 'user'

    ROLE_CHOICES = [
        (ROLE_PLATFORM_OWNER, 'Superusuario / Dueño de la plataforma'),
        (ROLE_ADMIN, 'Administrador / Dueño de taxis'),
        (ROLE_USER, 'Usuario normal'),
    ]

    role = models.CharField(max_length=30, choices=ROLE_CHOICES, default=ROLE_USER)
    phone = models.CharField(max_length=30, blank=True, null=True)
    avatar = models.ImageField(upload_to='users/avatars/', blank=True, null=True)

    is_platform_owner = models.BooleanField(default=False)
    admin_approved = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def is_owner(self):
        return self.role == self.ROLE_PLATFORM_OWNER or self.is_platform_owner or self.is_superuser

    def is_taxi_admin(self):
        return self.role == self.ROLE_ADMIN and self.admin_approved

    def is_normal_user(self):
        return self.role == self.ROLE_USER

    def __str__(self):
        return f"{self.username} - {self.get_role_display()}"


class AdminRequest(models.Model):
    STATUS_PENDING = 'pending'
    STATUS_APPROVED = 'approved'
    STATUS_REJECTED = 'rejected'

    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pendiente'),
        (STATUS_APPROVED, 'Aprobada'),
        (STATUS_REJECTED, 'Rechazada'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='admin_requests'
    )

    # Datos del propietario
    owner_full_name = models.CharField(max_length=180)
    phone = models.CharField(max_length=30)
    city = models.CharField(max_length=100, default='Malabo')
    address = models.CharField(max_length=255, blank=True, null=True)

    identity_number = models.CharField(max_length=100, blank=True, null=True)
    identity_document = models.FileField(upload_to='kyc/identity_documents/', blank=True, null=True)
    selfie_photo = models.ImageField(upload_to='kyc/selfies/', blank=True, null=True)

    # Datos empresa/flota
    company_name = models.CharField(max_length=150)
    taxi_count = models.PositiveIntegerField(default=1)

    # Taxi principal de verificación
    main_taxi_brand = models.CharField(max_length=100, blank=True, null=True)
    main_taxi_model = models.CharField(max_length=100, blank=True, null=True)
    main_taxi_plate = models.CharField(max_length=50, blank=True, null=True)
    main_taxi_color = models.CharField(max_length=50, blank=True, null=True)

    taxi_registration_document = models.FileField(upload_to='kyc/taxi_documents/', blank=True, null=True)
    taxi_license_document = models.FileField(upload_to='kyc/taxi_licenses/', blank=True, null=True)
    ownership_proof_document = models.FileField(upload_to='kyc/ownership_proofs/', blank=True, null=True)


    activation_fee = models.DecimalField(max_digits=12, decimal_places=2, default=50000)
    payment_reference = models.CharField(max_length=100, blank=True, null=True)
    payment_receipt = models.FileField(upload_to='kyc/payment_receipts/', blank=True, null=True)
    payment_verified = models.BooleanField(default=False)
    payment_verified_at = models.DateTimeField(blank=True, null=True)
    payment_note = models.TextField(blank=True, null=True)

    message = models.TextField(blank=True, null=True)


    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)

    reviewed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='reviewed_admin_requests'
    )

    reviewed_at = models.DateTimeField(blank=True, null=True)
    review_note = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Solicitud KYC de dueño de taxi'
        verbose_name_plural = 'Solicitudes KYC de dueños de taxis'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.company_name} - {self.user.username} - {self.get_status_display()}"
