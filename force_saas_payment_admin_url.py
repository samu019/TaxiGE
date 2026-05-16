from pathlib import Path

p = Path("accounts/admin.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

text = text.replace(
    "class SaaSPaymentSettingsAdmin(admin.ModelAdmin):",
    "class SaaSPaymentSettingsAdmin(admin.ModelAdmin):\n    app_label = 'accounts'",
    1
)

p.write_text(text, encoding="utf-8")
print("Admin SaaSPaymentSettings reforzado.")
