from pathlib import Path

p = Path("accounts/admin.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

text = text.replace(
    "from .models import User, AdminRequest",
    "from .models import User, AdminRequest, SaaSPaymentSettings"
)

if "@admin.register(SaaSPaymentSettings)" not in text:
    block = r'''

@admin.register(SaaSPaymentSettings)
class SaaSPaymentSettingsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'activation_fee',
        'primary_bank_name',
        'primary_account_holder',
        'primary_account_number',
        'secondary_bank_name',
        'secondary_account_holder',
        'secondary_account_number',
        'is_active',
        'updated_at',
    )

    list_filter = (
        'is_active',
        'primary_bank_name',
        'secondary_bank_name',
    )

    fieldsets = (
        ('Importe de activación', {
            'fields': (
                'activation_fee',
                'is_active',
            )
        }),
        ('Banco principal', {
            'fields': (
                'primary_bank_name',
                'primary_account_holder',
                'primary_account_number',
            )
        }),
        ('Banco alternativo', {
            'fields': (
                'secondary_bank_name',
                'secondary_account_holder',
                'secondary_account_number',
            )
        }),
        ('Instrucciones visibles para el solicitante', {
            'fields': (
                'payment_instructions',
            )
        }),
    )
'''
    text += block

p.write_text(text, encoding="utf-8")
print("SaaSPaymentSettings registrado en admin.")
