from pathlib import Path

p = Path("accounts/admin.py")
text = p.read_text(encoding="utf-8")

old = """    actions = ['approve_requests', 'reject_requests']

    def create_company_and_vehicle(self, admin_request, reviewer):
"""

new = """    actions = ['approve_requests', 'reject_requests']

    def save_model(self, request, obj, form, change):
        previous_status = None

        if change and obj.pk:
            try:
                previous_status = AdminRequest.objects.get(pk=obj.pk).status
            except AdminRequest.DoesNotExist:
                previous_status = None

        super().save_model(request, obj, form, change)

        if obj.status == AdminRequest.STATUS_APPROVED and previous_status != AdminRequest.STATUS_APPROVED:
            user = obj.user
            user.role = User.ROLE_ADMIN
            user.admin_approved = True
            user.is_staff = False
            user.is_superuser = False
            user.is_active = True
            user.save()

            self.create_company_and_vehicle(obj, request.user)

            obj.reviewed_by = request.user
            obj.reviewed_at = timezone.now()

            if not obj.review_note:
                obj.review_note = (
                    'Solicitud KYC aprobada manualmente desde el formulario. '
                    'Empresa y taxi inicial creados automáticamente.'
                )

            super().save_model(request, obj, form, change)

    def create_company_and_vehicle(self, admin_request, reviewer):
"""

if old not in text:
    print("AVISO: no encontré el bloque exacto. Revisaremos manualmente si hace falta.")
else:
    text = text.replace(old, new, 1)
    p.write_text(text, encoding="utf-8")
    print("OK: save_model automático agregado")
