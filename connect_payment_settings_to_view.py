from pathlib import Path

p = Path("accounts/views.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

text = text.replace(
    "from .models import AdminRequest",
    "from .models import AdminRequest, SaaSPaymentSettings"
)

if "payment_settings = SaaSPaymentSettings.get_active()" not in text:
    text = text.replace(
        "        form = OwnerKYCRegisterForm()",
        "        form = OwnerKYCRegisterForm()\n\n    payment_settings = SaaSPaymentSettings.get_active()",
        1
    )

text = text.replace(
    "return render(request, 'accounts/register_owner_kyc.html', {'form': form})",
    "return render(request, 'accounts/register_owner_kyc.html', {'form': form, 'payment_settings': payment_settings})"
)

p.write_text(text, encoding="utf-8")
print("Vista KYC conectada con configuración de pagos.")
