from pathlib import Path

p = Path("accounts/admin.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

# Asegurar import del modelo
text = text.replace(
    "from .models import User, AdminRequest, SaaSPaymentSettings, SaaSSubscription",
    "from .models import User, AdminRequest, SaaSPaymentSettings, SaaSSubscription"
)

# Helper para crear/renovar suscripción
helper = r'''
    def create_or_renew_subscription(self, user, admin_request):
        from django.utils import timezone
        from datetime import timedelta

        today = timezone.localdate()
        end_date = today + timedelta(days=30)

        subscription, created = SaaSSubscription.objects.get_or_create(
            user=user,
            defaults={
                'monthly_fee': admin_request.activation_fee,
                'start_date': today,
                'end_date': end_date,
                'status': SaaSSubscription.STATUS_ACTIVE,
                'last_payment_reference': admin_request.payment_reference,
                'last_payment_receipt': admin_request.payment_receipt,
                'notes': f'Suscripción creada automáticamente al aprobar KYC ID {admin_request.id}.',
            }
        )

        if not created:
            subscription.monthly_fee = admin_request.activation_fee
            subscription.start_date = today
            subscription.end_date = end_date
            subscription.status = SaaSSubscription.STATUS_ACTIVE
            subscription.last_payment_reference = admin_request.payment_reference
            subscription.last_payment_receipt = admin_request.payment_receipt
            subscription.notes = f'Suscripción renovada automáticamente al aprobar KYC ID {admin_request.id}.'
            subscription.save()

        return subscription

'''

if "def create_or_renew_subscription(self, user, admin_request):" not in text:
    text = text.replace(
        "    def create_company_and_vehicle(self, admin_request, reviewer):",
        helper + "    def create_company_and_vehicle(self, admin_request, reviewer):",
        1
    )

# Insertar creación de suscripción en aprobación manual
old_manual = """            self.create_company_and_vehicle(obj, request.user)

            obj.reviewed_by = request.user
"""

new_manual = """            self.create_company_and_vehicle(obj, request.user)
            subscription = self.create_or_renew_subscription(user, obj)

            obj.reviewed_by = request.user
"""

if "subscription = self.create_or_renew_subscription(user, obj)" not in text:
    text = text.replace(old_manual, new_manual, 1)

# Mejorar notificación de aprobación manual con fecha fin
old_notification = """                f'Tu cuenta de propietario para {obj.company_name} fue aprobada. Ya puedes acceder al panel de gestión.',
                'success',
                '/panel/'
            )
"""

new_notification = """                f'Tu cuenta de propietario para {obj.company_name} fue aprobada. Tu suscripción SaaS está activa hasta {subscription.end_date}.',
                'success',
                '/panel/'
            )
"""

text = text.replace(old_notification, new_notification, 1)

# Insertar creación de suscripción en aprobación masiva
old_bulk = """            self.create_company_and_vehicle(admin_request, request.user)

            admin_request.status = AdminRequest.STATUS_APPROVED
"""

new_bulk = """            self.create_company_and_vehicle(admin_request, request.user)
            self.create_or_renew_subscription(user, admin_request)

            admin_request.status = AdminRequest.STATUS_APPROVED
"""

if "self.create_or_renew_subscription(user, admin_request)" not in text:
    text = text.replace(old_bulk, new_bulk, 1)

p.write_text(text, encoding="utf-8")
print("Suscripción automática al aprobar KYC agregada.")
