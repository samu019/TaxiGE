from django.conf import settings
from django.db import models


class Notification(models.Model):
    LEVEL_INFO = "info"
    LEVEL_SUCCESS = "success"
    LEVEL_WARNING = "warning"
    LEVEL_DANGER = "danger"

    LEVEL_CHOICES = [
        (LEVEL_INFO, "Información"),
        (LEVEL_SUCCESS, "Éxito"),
        (LEVEL_WARNING, "Advertencia"),
        (LEVEL_DANGER, "Peligro"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notifications"
    )

    title = models.CharField(max_length=150)
    message = models.TextField()
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default=LEVEL_INFO)
    link = models.CharField(max_length=255, blank=True, null=True)

    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Notificación"
        verbose_name_plural = "Notificaciones"

    def __str__(self):
        return f"{self.user} - {self.title}"
