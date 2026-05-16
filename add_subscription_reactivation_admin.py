from pathlib import Path

p = Path("accounts/admin.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

# Asegurar import de timedelta
if "from datetime import timedelta" not in text:
    text = text.replace(
        "from django.utils import timezone",
        "from django.utils import timezone\nfrom datetime import timedelta"
    )

# Asegurar Notification
if "from notifications.models import Notification" not in text:
    text = text.replace(
        "from vehicles.models import Vehicle",
        "from vehicles.models import Vehicle\nfrom notifications.models import Notification"
    )

old = """@admin.register(SaaSSubscription)
class SaaSSubscriptionAdmin(admin.ModelAdmin):"""

new = """@admin.register(SaaSSubscription)
class SaaSSubscriptionAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        previous_status = None

        if change and obj.pk:
            try:
                previous_status = SaaSSubscription.objects.get(pk=obj.pk).status
            except SaaSSubscription.DoesNotExist:
                previous_status = None

        if obj.status == SaaSSubscription.STATUS_ACTIVE and previous_status != SaaSSubscription.STATUS_ACTIVE:
            today = timezone.localdate()
            obj.start_date = today
            obj.end_date = today + timedelta(days=30)

            if not obj.notes:
                obj.notes = 'Suscripción reactivada manualmente desde administración.'
            else:
                obj.notes += '\\nSuscripción reactivada manualmente desde administración.'

        super().save_model(request, obj, form, change)

        if obj.status == SaaSSubscription.STATUS_ACTIVE and previous_status != SaaSSubscription.STATUS_ACTIVE:
            try:
                Notification.objects.create(
                    user=obj.user,
                    title='Suscripción SaaS reactivada',
                    message=f'Tu suscripción SaaS fue reactivada correctamente hasta {obj.end_date}. Ya puedes acceder al panel.',
                    level='success',
                    link='/panel/'
                )
            except Exception:
                pass
"""

if "def save_model(self, request, obj, form, change):" not in text[text.find("class SaaSSubscriptionAdmin"):]:
    text = text.replace(old, new, 1)

p.write_text(text, encoding="utf-8")
print("Reactivación automática de suscripción agregada al admin.")
