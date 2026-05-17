from django.contrib.auth import get_user_model
from django.db import transaction

from audits.models import AuditLog
from notifications.models import Notification
from sharing.models import CompanyMember, TaxiShareInvite
from damages.models import VehicleDamage
from payments.models import DriverPayment
from drivers.models import Driver
from vehicles.models import Vehicle
from companies.models import Company
from accounts.models import AdminRequest, SaaSSubscription, SaaSPaymentHistory

User = get_user_model()

SUPER_USERNAME = "AdminTaxiGE"
SUPER_EMAIL = "admin@taxige.local"
SUPER_PASSWORD = "TaxiGEAdmin2026!"

NORMAL_USERNAME = "Samuelmba"
NORMAL_EMAIL = "Slimmysamuelmba@gmail.com"
NORMAL_PASSWORD = "TaxiGEUser2026!"

with transaction.atomic():
    SaaSPaymentHistory.objects.all().delete()
    SaaSSubscription.objects.all().delete()
    AdminRequest.objects.all().delete()
    TaxiShareInvite.objects.all().delete()
    CompanyMember.objects.all().delete()
    AuditLog.objects.all().delete()
    Notification.objects.all().delete()
    VehicleDamage.objects.all().delete()
    DriverPayment.objects.all().delete()
    Driver.objects.all().delete()
    Vehicle.objects.all().delete()
    Company.objects.all().delete()
    User.objects.all().delete()

    superuser = User.objects.create(
        username=SUPER_USERNAME,
        email=SUPER_EMAIL,
        first_name="Admin",
        last_name="TaxiGE",
        role=getattr(User, "ROLE_PLATFORM_OWNER", "platform_owner"),
        is_platform_owner=True,
        admin_approved=True,
        is_staff=True,
        is_superuser=True,
        is_active=True,
    )
    superuser.set_password(SUPER_PASSWORD)
    superuser.save()

    normal = User.objects.create(
        username=NORMAL_USERNAME,
        email=NORMAL_EMAIL,
        first_name="Samuel",
        last_name="Mba",
        phone="+240000000000",
        role=getattr(User, "ROLE_USER", "user"),
        admin_approved=False,
        is_staff=False,
        is_superuser=False,
        is_active=True,
    )
    normal.set_password(NORMAL_PASSWORD)
    normal.save()

print("BASE LIMPIA")
print("SUPER:", SUPER_USERNAME, SUPER_EMAIL, SUPER_PASSWORD)
print("NORMAL:", NORMAL_USERNAME, NORMAL_EMAIL, NORMAL_PASSWORD)
print("TOTAL:", User.objects.count())
