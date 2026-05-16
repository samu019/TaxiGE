from django.contrib import admin
from .models import AuditLog


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'action', 'app_label', 'model_name', 'object_repr', 'created_at')
    list_filter = ('action', 'app_label', 'model_name', 'created_at')
    search_fields = ('user__username', 'model_name', 'object_repr', 'description')
    readonly_fields = (
        'user',
        'action',
        'app_label',
        'model_name',
        'object_id',
        'object_repr',
        'description',
        'ip_address',
        'user_agent',
        'created_at',
    )

    def has_add_permission(self, request):
        return False
