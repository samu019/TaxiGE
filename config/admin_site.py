from django.contrib.admin import AdminSite


class PlatformOwnerAdminSite(AdminSite):
    site_header = 'TaxiGE Platform - Administración Principal'
    site_title = 'TaxiGE Admin'
    index_title = 'Panel principal del superusuario'

    def has_permission(self, request):
        user = request.user
        return bool(
            user.is_active
            and user.is_authenticated
            and user.is_superuser
            and getattr(user, 'is_platform_owner', False)
        )
