from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8")

replacements = {
"""    if request.method == 'POST':
        form = DriverPaymentForm(request.POST, company=company)""":
"""    if request.method == 'POST':
        if not user_can_add_payments(request.user, company):
            messages.error(request, 'No tienes permiso para registrar pagos.')
            return redirect('/panel/payments/')
        form = DriverPaymentForm(request.POST, company=company)""",

"""    if request.method == 'POST':
        form = VehicleDamageForm(request.POST, request.FILES, company=company)""":
"""    if request.method == 'POST':
        if not user_can_add_damages(request.user, company):
            messages.error(request, 'No tienes permiso para registrar daños.')
            return redirect('/panel/damages/')
        form = VehicleDamageForm(request.POST, request.FILES, company=company)""",
}

for old, new in replacements.items():
    text = text.replace(old, new)

p.write_text(text, encoding="utf-8")
print("Creación de pagos y daños protegida")
