from pathlib import Path

p = Path("accounts/admin.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

# 1. list_display
if "'payment_verified'," not in text:
    text = text.replace(
        "        'status',\n        'created_at',",
        "        'status',\n        'payment_verified',\n        'activation_fee',\n        'created_at',",
        1
    )

# 2. list_filter
if "'payment_verified'," not in text[text.find("class AdminRequestAdmin"):text.find("search_fields", text.find("class AdminRequestAdmin"))]:
    text = text.replace(
        "        'status',\n        'city',\n        'created_at',",
        "        'status',\n        'payment_verified',\n        'city',\n        'created_at',",
        1
    )

# 3. search_fields
if "'payment_reference'," not in text:
    text = text.replace(
        "        'identity_number',",
        "        'identity_number',\n        'payment_reference',",
        1
    )

# 4. readonly_fields: payment_verified debe ser editable; receipt/reference/note también editables si admin quiere ajustar
for field in [
    "'activation_fee',",
    "'payment_reference',",
    "'payment_receipt',",
    "'payment_verified_at',",
]:
    if field not in text:
        pass

# 5. Insertar fieldset de pago antes de Mensaje y fechas
payment_fieldset = """        ('Pago de activación SaaS', {
            'fields': (
                'activation_fee',
                'payment_reference',
                'payment_receipt',
                'payment_verified',
                'payment_verified_at',
                'payment_note',
            )
        }),
"""

if "Pago de activación SaaS" not in text:
    text = text.replace(
        "        ('Mensaje y fechas', {",
        payment_fieldset + "        ('Mensaje y fechas', {",
        1
    )

# 6. Auto fecha de verificación si se marca pago verificado
old = """        super().save_model(request, obj, form, change)

        if obj.status == AdminRequest.STATUS_APPROVED and previous_status != AdminRequest.STATUS_APPROVED:"""

new = """        if obj.payment_verified and not obj.payment_verified_at:
            obj.payment_verified_at = timezone.now()

        super().save_model(request, obj, form, change)

        if obj.status == AdminRequest.STATUS_APPROVED and previous_status != AdminRequest.STATUS_APPROVED:"""

if "if obj.payment_verified and not obj.payment_verified_at:" not in text:
    text = text.replace(old, new, 1)

p.write_text(text, encoding="utf-8")
print("Admin KYC actualizado exactamente para pago de activación.")
