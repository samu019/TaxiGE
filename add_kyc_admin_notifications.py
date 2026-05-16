from pathlib import Path

p = Path("accounts/admin.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

# Importar Notification
if "from notifications.models import Notification" not in text:
    text = text.replace(
        "from vehicles.models import Vehicle",
        "from vehicles.models import Vehicle\nfrom notifications.models import Notification"
    )

# Helper para crear notificación
helper = r'''
    def create_user_notification(self, user, title, message, level='info', link='/panel/'):
        try:
            Notification.objects.create(
                user=user,
                title=title,
                message=message,
                level=level,
                link=link,
            )
        except Exception:
            pass

'''

if "def create_user_notification(self, user, title," not in text:
    text = text.replace(
        "    def save_model(self, request, obj, form, change):",
        helper + "    def save_model(self, request, obj, form, change):",
        1
    )

# Notificación cuando pago se verifica
old_payment = """        if obj.payment_verified and not obj.payment_verified_at:
            obj.payment_verified_at = timezone.now()
"""

new_payment = """        payment_was_verified_now = False

        if obj.payment_verified and not obj.payment_verified_at:
            obj.payment_verified_at = timezone.now()
            payment_was_verified_now = True
"""

text = text.replace(old_payment, new_payment, 1)

old_after_save = """        super().save_model(request, obj, form, change)

        if obj.status == AdminRequest.STATUS_APPROVED and previous_status != AdminRequest.STATUS_APPROVED:"""

new_after_save = """        super().save_model(request, obj, form, change)

        if payment_was_verified_now:
            self.create_user_notification(
                obj.user,
                'Pago de activación verificado',
                f'Tu pago de activación para {obj.company_name} fue verificado correctamente. Tu solicitud KYC ya puede ser aprobada.',
                'success',
                '/panel/'
            )

        if obj.status == AdminRequest.STATUS_APPROVED and previous_status != AdminRequest.STATUS_APPROVED:"""

text = text.replace(old_after_save, new_after_save, 1)

# Notificación cuando KYC se aprueba
old_approved = """            super().save_model(request, obj, form, change)
"""

new_approved = """            self.create_user_notification(
                obj.user,
                'Solicitud KYC aprobada',
                f'Tu cuenta de propietario para {obj.company_name} fue aprobada. Ya puedes acceder al panel de gestión.',
                'success',
                '/panel/'
            )

            super().save_model(request, obj, form, change)
"""

# Reemplazar solo dentro del bloque de aprobación manual
if "Tu cuenta de propietario para {obj.company_name} fue aprobada" not in text:
    text = text.replace(old_approved, new_approved, 1)

# Notificación cuando KYC se rechaza en acción masiva
old_reject_save = """            admin_request.save()
            rejected_count += 1
"""

new_reject_save = """            admin_request.save()

            self.create_user_notification(
                admin_request.user,
                'Solicitud KYC rechazada',
                f'Tu solicitud KYC para {admin_request.company_name} fue rechazada. Revisa las observaciones o contacta con soporte.',
                'danger',
                '/accounts/register/owner/'
            )

            rejected_count += 1
"""

if "Tu solicitud KYC para {admin_request.company_name} fue rechazada" not in text:
    text = text.replace(old_reject_save, new_reject_save, 1)

p.write_text(text, encoding="utf-8")
print("Notificaciones KYC agregadas al admin.")
