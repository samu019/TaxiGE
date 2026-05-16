from pathlib import Path

p = Path("config/urls.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

text = text.replace(
    "from accounts.models import User, AdminRequest, SaaSPaymentSettings",
    "from accounts.models import User, AdminRequest, SaaSPaymentSettings, SaaSSubscription"
)

text = text.replace(
    "from accounts.admin import CustomUserAdmin, AdminRequestAdmin, SaaSPaymentSettingsAdmin",
    "from accounts.admin import CustomUserAdmin, AdminRequestAdmin, SaaSPaymentSettingsAdmin, SaaSSubscriptionAdmin"
)

registration = "platform_admin_site.register(SaaSSubscription, SaaSSubscriptionAdmin)"

if registration not in text:
    text = text.replace(
        "platform_admin_site.register(SaaSPaymentSettings, SaaSPaymentSettingsAdmin)",
        "platform_admin_site.register(SaaSPaymentSettings, SaaSPaymentSettingsAdmin)\n" + registration
    )

p.write_text(text, encoding="utf-8")
print("SaaSSubscription agregado al PlatformOwnerAdminSite.")
