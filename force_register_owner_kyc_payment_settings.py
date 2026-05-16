from pathlib import Path
import re

p = Path("accounts/views.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

if "SaaSPaymentSettings" not in text.splitlines()[0:30].__str__():
    text = text.replace(
        "from .models import AdminRequest",
        "from .models import AdminRequest, SaaSPaymentSettings",
        1
    )

pattern = r"def register_owner_kyc\(request\):.*?(?=\ndef |\Z)"

new_view = r'''def register_owner_kyc(request):
    payment_settings = SaaSPaymentSettings.get_active()

    if request.method == 'POST':
        form = OwnerKYCRegisterForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('accounts:request_admin_success')
    else:
        form = OwnerKYCRegisterForm()

    return render(request, 'accounts/register_owner_kyc.html', {
        'form': form,
        'payment_settings': payment_settings,
    })

'''

text, count = re.subn(pattern, new_view, text, count=1, flags=re.DOTALL)

if count != 1:
    raise SystemExit("No se pudo reemplazar register_owner_kyc. Revisa el nombre exacto de la vista.")

p.write_text(text, encoding="utf-8")
print("Vista register_owner_kyc conectada correctamente con payment_settings.")
