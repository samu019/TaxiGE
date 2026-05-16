from pathlib import Path

p = Path("accounts/admin.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

# Asegurar import correcto
if "SaaSPaymentSettings" not in text.split("\n")[0:20].__str__():
    text = text.replace(
        "from .models import User, AdminRequest",
        "from .models import User, AdminRequest, SaaSPaymentSettings"
    )

# Eliminar registros incompletos duplicados si existieran no hace falta; solo agregamos si falta
if "@admin.register(SaaSPaymentSettings)" not in text:
    text += r'''

@admin.register(SaaSPaymentSettings)
class SaaSPaymentSettingsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'activation_fee',
        'primary_bank_name',
        'primary_account_number',
        'secondary_bank_name',
        'secondary_account_number',
        'is_active',
        'updated_at',
    )

    list_filter = (
        'is_active',
        'primary_bank_name',
        'secondary_bank_name',
    )

    search_fields = (
        'primary_bank_name',
        'primary_account_holder',
        'primary_account_number',
        'secondary_bank_name',
        'secondary_account_holder',
        'secondary_account_number',
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

p.write_text(text, encoding="utf-8")
print("Admin de SaaSPaymentSettings reparado.")
