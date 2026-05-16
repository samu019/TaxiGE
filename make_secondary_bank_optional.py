from pathlib import Path
import re

p = Path("accounts/models.py")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

text = text.replace(
    "secondary_bank_name = models.CharField(max_length=100, default='ECOBANK')",
    "secondary_bank_name = models.CharField(max_length=100, blank=True, null=True, default='ECOBANK')"
)

text = text.replace(
    "secondary_account_holder = models.CharField(max_length=150, default='TaxiGE Platform')",
    "secondary_account_holder = models.CharField(max_length=150, blank=True, null=True, default='TaxiGE Platform')"
)

text = text.replace(
    "secondary_account_number = models.CharField(max_length=100, default='Pendiente de configurar')",
    "secondary_account_number = models.CharField(max_length=100, blank=True, null=True, default='')"
)

p.write_text(text, encoding="utf-8")
print("Banco alternativo marcado como opcional.")
