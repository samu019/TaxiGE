from pathlib import Path

p = Path("accounts/admin.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

text = text.replace(
    "from .models import User, AdminRequest, SaaSPaymentSettings",
    "from .models import User, AdminRequest, SaaSPaymentSettings, SaaSSubscription"
)

if "@admin.register(SaaSSubscription)" not in text:
    text += r'''

@admin.register(SaaSSubscription)
class SaaSSubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'monthly_fee',
        'start_date',
        'end_date',
        'status',
        'updated_at',
    )

    list_filter = (
        'status',
        'start_date',
        'end_date',
    )

    search_fields = (
        'user__username',
        'user__email',
        'last_payment_reference',
    )

    fieldsets = (
        ('Propietario', {
            'fields': (
                'user',
            )
        }),
        ('Periodo de suscripción', {
            'fields': (
                'monthly_fee',
                'start_date',
                'end_date',
                'status',
            )
        }),
        ('Último pago', {
            'fields': (
                'last_payment_reference',
                'last_payment_receipt',
            )
        }),
        ('Notas', {
            'fields': (
                'notes',
            )
        }),
    )
'''
p.write_text(text, encoding="utf-8")
print("SaaSSubscription registrado en accounts/admin.py.")
