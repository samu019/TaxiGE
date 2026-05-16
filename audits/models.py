from django.conf import settings
from django.db import models


class AuditLog(models.Model):
    ACTION_CREATE = 'create'
    ACTION_UPDATE = 'update'
    ACTION_DELETE = 'delete'
    ACTION_LOGIN = 'login'
    ACTION_LOGOUT = 'logout'
    ACTION_VIEW = 'view'

    ACTION_CHOICES = [
        (ACTION_CREATE, 'Creación'),
        (ACTION_UPDATE, 'Actualización'),
        (ACTION_DELETE, 'Eliminación'),
        (ACTION_LOGIN, 'Inicio de sesión'),
        (ACTION_LOGOUT, 'Cierre de sesión'),
        (ACTION_VIEW, 'Consulta'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='audit_logs'
    )

    action = models.CharField(max_length=20, choices=ACTION_CHOICES)

    app_label = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    object_id = models.CharField(max_length=100, blank=True, null=True)
    object_repr = models.CharField(max_length=255, blank=True, null=True)

    description = models.TextField(blank=True, null=True)

    ip_address = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Registro de auditoría'
        verbose_name_plural = 'Registros de auditoría'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user} - {self.action} - {self.model_name}"
