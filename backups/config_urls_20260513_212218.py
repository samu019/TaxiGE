from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from config.admin_site import PlatformOwnerAdminSite
from accounts.views import (
    custom_logout,
    public_register,
    owner_kyc_register,
    register_choice,
    request_admin_access,
    SmartLoginView,
    home_page,
)

from accounts.admin import CustomUserAdmin, AdminRequestAdmin
from accounts.models import User, AdminRequest

from companies.admin import CompanyAdmin
from companies.models import Company

from vehicles.admin import VehicleAdmin
from vehicles.models import Vehicle

from drivers.admin import DriverAdmin
from drivers.models import Driver

from payments.admin import DriverPaymentAdmin
from payments.models import DriverPayment

from damages.admin import VehicleDamageAdmin
from damages.models import VehicleDamage

from audits.admin import AuditLogAdmin
from audits.models import AuditLog


platform_admin_site = PlatformOwnerAdminSite(name='platform_admin')

platform_admin_site.register(User, CustomUserAdmin)
platform_admin_site.register(AdminRequest, AdminRequestAdmin)
platform_admin_site.register(Company, CompanyAdmin)
platform_admin_site.register(Vehicle, VehicleAdmin)
platform_admin_site.register(Driver, DriverAdmin)
platform_admin_site.register(DriverPayment, DriverPaymentAdmin)
platform_admin_site.register(VehicleDamage, VehicleDamageAdmin)
platform_admin_site.register(AuditLog, AuditLogAdmin)


urlpatterns = [
    path('', home_page, name='home'),

    path('admin/', platform_admin_site.urls),

    path('accounts/login/', SmartLoginView.as_view(), name='login'),
    path('accounts/register/', register_choice, name='register_choice'),
    path('accounts/register/user/', public_register, name='register_user'),
    path('accounts/register/owner/', owner_kyc_register, name='register_owner'),
    path('accounts/logout/', custom_logout, name='logout'),

    path('request-admin/', request_admin_access, name='request_admin'),

    path('panel/', include('dashboard.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
