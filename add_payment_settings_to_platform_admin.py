from pathlib import Path

p = Path("config/urls.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

# Importar modelo y admin
if "SaaSPaymentSettings" not in text:
    text = text.replace(
        "from accounts.models import User, AdminRequest",
        "from accounts.models import User, AdminRequest, SaaSPaymentSettings"
    )

    text = text.replace(
        "from accounts.admin import CustomUserAdmin, AdminRequestAdmin",
        "from accounts.admin import CustomUserAdmin, AdminRequestAdmin, SaaSPaymentSettingsAdmin"
    )

# Registrar en el admin personalizado
registration = "platform_admin_site.register(SaaSPaymentSettings, SaaSPaymentSettingsAdmin)"

if registration not in text:
    text = text.replace(
        "platform_admin_site.register(AdminRequest, AdminRequestAdmin)",
        "platform_admin_site.register(AdminRequest, AdminRequestAdmin)\n" + registration
    )

p.write_text(text, encoding="utf-8")
print("SaaSPaymentSettings agregado al PlatformOwnerAdminSite.")
