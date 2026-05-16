from pathlib import Path

p = Path("accounts/admin.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

text = text.replace(
    "from .models import User, AdminRequest, SaaSPaymentSettings, SaaSSubscription",
    "from .models import User, AdminRequest, SaaSPaymentSettings, SaaSSubscription, SaaSPaymentHistory"
)

if "@admin.register(SaaSPaymentHistory)" not in text:
    text += r'''

@admin.register(SaaSPaymentHistory)
class SaaSPaymentHistoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'amount',
        'reference',
        'status',
        'created_at',
        'reviewed_by',
        'reviewed_at',
    )

    list_filter = (
        'status',
        'created_at',
        'reviewed_at',
    )

    search_fields = (
        'user__username',
        'user__email',
        'reference',
    )

    readonly_fields = (
        'subscription',
        'user',
        'amount',
        'reference',
        'receipt',
        'created_at',
    )

    fieldsets = (
        ('Pago recibido', {
            'fields': (
                'subscription',
                'user',
                'amount',
                'reference',
                'receipt',
                'created_at',
            )
        }),
        ('Revisión administrativa', {
            'fields': (
                'status',
                'reviewed_by',
                'reviewed_at',
                'admin_note',
            )
        }),
    )
'''
p.write_text(text, encoding="utf-8")
print("SaaSPaymentHistory registrado en admin.")
