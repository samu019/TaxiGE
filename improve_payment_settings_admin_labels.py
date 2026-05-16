from pathlib import Path

p = Path("accounts/admin.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

marker = "class SaaSPaymentSettingsAdmin(admin.ModelAdmin):"

admin_methods = r'''
    def formfield_for_dbfield(self, db_field, request, **kwargs):
        labels = {
            'activation_fee': 'Importe de activación',
            'is_active': 'Configuración activa',
            'primary_bank_name': 'Banco principal',
            'primary_account_holder': 'Nombre del titular de la cuenta principal',
            'primary_account_number': 'Número de cuenta principal',
            'secondary_bank_name': 'Banco alternativo opcional',
            'secondary_account_holder': 'Nombre del titular de la cuenta alternativa',
            'secondary_account_number': 'Número de cuenta alternativa',
            'payment_instructions': 'Instrucciones visibles para el solicitante',
        }

        formfield = super().formfield_for_dbfield(db_field, request, **kwargs)

        if db_field.name in labels:
            formfield.label = labels[db_field.name]

        return formfield

'''

if "Nombre del titular de la cuenta principal" not in text:
    text = text.replace(marker, marker + "\n" + admin_methods, 1)

p.write_text(text, encoding="utf-8")
print("Etiquetas del admin de pagos SaaS mejoradas.")
