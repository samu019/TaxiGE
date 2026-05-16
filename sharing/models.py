from django.conf import settings
from django.db import models
from django.utils import timezone
from secrets import token_urlsafe

from companies.models import Company


class CompanyMember(models.Model):
    ROLE_OWNER = "owner"
    ROLE_PARTNER = "partner"
    ROLE_MANAGER = "manager"
    ROLE_VIEWER = "viewer"
    ROLE_ACCOUNTANT = "accountant"

    ROLE_CHOICES = [
        (ROLE_OWNER, "Propietario principal"),
        (ROLE_PARTNER, "Socio"),
        (ROLE_MANAGER, "Gestor"),
        (ROLE_VIEWER, "Solo lectura"),
        (ROLE_ACCOUNTANT, "Contable"),
    ]

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="members"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="company_memberships"
    )
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=ROLE_VIEWER
    )

    can_view_payments = models.BooleanField(default=True)
    can_view_damages = models.BooleanField(default=True)
    can_add_payments = models.BooleanField(default=False)
    can_add_damages = models.BooleanField(default=False)
    can_edit_data = models.BooleanField(default=False)
    can_invite_members = models.BooleanField(default=False)
    can_export_reports = models.BooleanField(default=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("company", "user")
        verbose_name = "Miembro de empresa"
        verbose_name_plural = "Miembros de empresas"

    def __str__(self):
        return f"{self.user} - {self.company} - {self.role}"


class TaxiShareInvite(models.Model):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="share_invites"
    )
    invited_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="created_taxi_invites"
    )

    token = models.CharField(max_length=120, unique=True, blank=True)
    role = models.CharField(
        max_length=20,
        choices=CompanyMember.ROLE_CHOICES,
        default=CompanyMember.ROLE_VIEWER
    )

    max_uses = models.PositiveIntegerField(default=1)
    used_count = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)
    expires_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Invitación compartida"
        verbose_name_plural = "Invitaciones compartidas"

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = token_urlsafe(32)
        super().save(*args, **kwargs)

    @property
    def is_valid(self):
        if not self.is_active:
            return False
        if self.used_count >= self.max_uses:
            return False
        if self.expires_at and timezone.now() > self.expires_at:
            return False
        return True

    def __str__(self):
        return f"Invitación {self.company} - {self.role}"