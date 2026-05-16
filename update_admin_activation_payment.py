from pathlib import Path

p = Path("accounts/admin.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

# Agregar campos a list_display
text = text.replace(
    "list_display = ('company_name', 'user', 'status', 'created_at')",
    "list_display = ('company_name', 'user', 'status', 'payment_verified', 'activation_fee', 'created_at')"
)

# Agregar filtros
text = text.replace(
    "list_filter = ('status', 'created_at')",
    "list_filter = ('status', 'payment_verified', 'created_at')"
)

# Agregar búsqueda por referencia
text = text.replace(
    "search_fields = ('company_name', 'user__username', 'owner_full_name')",
    "search_fields = ('company_name', 'user__username', 'owner_full_name', 'payment_reference')"
)

# Insertar fieldsets si no existen
if "Datos de pago de activación" not in text:
    marker = "readonly_fields = ('created_at', 'updated_at', 'reviewed_at')"
    if marker in text:
        insert = """
    fieldsets = (
        ('Usuario', {
            'fields': ('user',)
        }),
        ('Datos del propietario', {
            'fields': ('owner_full_name', 'phone', 'city', 'address', 'identity_number', 'identity_document', 'selfie_photo')
        }),
        ('Datos de empresa y taxi', {
            'fields': ('company_name', 'taxi_count', 'main_taxi_brand', 'main_taxi_model', 'main_taxi_plate', 'main_taxi_color', 'taxi_registration_document', 'taxi_license_document', 'ownership_proof_document')
        }),
        ('Datos de pago de activación', {
            'fields': ('activation_fee', 'payment_reference', 'payment_receipt', 'payment_verified', 'payment_verified_at', 'payment_note')
        }),
        ('Revisión administrativa', {
            'fields': ('status', 'reviewed_by', 'reviewed_at', 'review_note')
        }),
        ('Mensaje', {
            'fields': ('message',)
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at')
        }),
    )
"""
        text = text.replace(marker, marker + "\n" + insert, 1)

p.write_text(text, encoding="utf-8")
print("Admin actualizado con pago de activación")
