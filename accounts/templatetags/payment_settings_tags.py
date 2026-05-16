from django import template
from accounts.models import SaaSPaymentSettings

register = template.Library()

@register.simple_tag
def active_payment_settings():
    return SaaSPaymentSettings.get_active()
