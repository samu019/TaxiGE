from pathlib import Path

p = Path("config/urls.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

text = text.replace(
    "from accounts.models import User, AdminRequest, SaaSPaymentSettings, SaaSSubscription",
    "from accounts.models import User, AdminRequest, SaaSPaymentSettings, SaaSSubscription, SaaSPaymentHistory"
)

text = text.replace(
    "from accounts.admin import CustomUserAdmin, AdminRequestAdmin, SaaSPaymentSettingsAdmin, SaaSSubscriptionAdmin",
    "from accounts.admin import CustomUserAdmin, AdminRequestAdmin, SaaSPaymentSettingsAdmin, SaaSSubscriptionAdmin, SaaSPaymentHistoryAdmin"
)

registration = "platform_admin_site.register(SaaSPaymentHistory, SaaSPaymentHistoryAdmin)"

if registration not in text:
    text = text.replace(
        "platform_admin_site.register(SaaSSubscription, SaaSSubscriptionAdmin)",
        "platform_admin_site.register(SaaSSubscription, SaaSSubscriptionAdmin)\n" + registration
    )

p.write_text(text, encoding="utf-8")
print("SaaSPaymentHistory agregado al PlatformOwnerAdminSite.")
