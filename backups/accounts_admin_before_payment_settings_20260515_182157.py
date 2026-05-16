from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils import timezone
from .models import User, AdminRequest
from companies.models import Company
from vehicles.models import Vehicle


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        'id',
        'username',
        'email',
        'phone',
        'role',
        'admin_approved',
        'is_platform_owner',
        'is_staff',
        'is_active',
        'date_joined',
    )

    list_filter = (
        'role',
        'admin_approved',
        'is_platform_owner',
        'is_staff',
        'is_active',
        'date_joined',
    )

    search_fields = (
        'username',
        'email',
        'phone',
        'first_name',
        'last_name',
    )

    fieldsets = UserAdmin.fieldsets + (
        ('Datos de TaxiGE Platform', {
            'fields': (
                'role',
                'phone',
                'avatar',
                'is_platform_owner',
                'admin_approved',
            )
        }),
    )


@admin.register(AdminRequest)
class AdminRequestAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'company_name',
        'owner_full_name',
        'user',
        'phone',
        'city',
        'taxi_count',
        'main_taxi_plate',
        'status',
        'payment_verified',
        'activation_fee',
        'created_at',
    )

    list_filter = (
        'status',
        'city',
        'created_at',
    )

    search_fields = (
        'company_name',
        'owner_full_name',
        'phone',
        'user__username',
        'user__email',
        'main_taxi_plate',
        'identity_number',
        'payment_reference',
    )

    readonly_fields = (
        'user',
        'owner_full_name',
        'phone',
        'city',
        'address',
        'identity_number',
        'identity_document',
        'selfie_photo',

        'company_name',
        'taxi_count',

        'main_taxi_brand',
        'main_taxi_model',
        'main_taxi_plate',
        'main_taxi_color',

        'taxi_registration_document',
        'taxi_license_document',
        'ownership_proof_document',

        'message',
        'created_at',
        'updated_at',
        'reviewed_by',
        'reviewed_at',
    )

    fieldsets = (
        ('Estado de revisión', {
            'fields': (
                'status',
                'review_note',
                'reviewed_by',
                'reviewed_at',
            )
        }),
        ('Usuario solicitante', {
            'fields': ('user',)
        }),
        ('Datos del propietario', {
            'fields': (
                'owner_full_name',
                'phone',
                'city',
                'address',
                'identity_number',
                'identity_document',
                'selfie_photo',
            )
        }),
        ('Empresa o flota', {
            'fields': (
                'company_name',
                'taxi_count',
            )
        }),
        ('Taxi principal de verificación', {
            'fields': (
                'main_taxi_brand',
                'main_taxi_model',
                'main_taxi_plate',
                'main_taxi_color',
                'taxi_registration_document',
                'taxi_license_document',
                'ownership_proof_document',
            )
        }),
        ('Pago de activación SaaS', {
            'fields': (
                'activation_fee',
                'payment_reference',
                'payment_receipt',
                'payment_verified',
                'payment_verified_at',
                'payment_note',
            )
        }),
        ('Mensaje y fechas', {
            'fields': (
                'message',
                'created_at',
                'updated_at',
            )
        }),
    )

    actions = ['approve_requests', 'reject_requests']

    def save_model(self, request, obj, form, change):
        previous_status = None

        if change and obj.pk:
            try:
                previous_status = AdminRequest.objects.get(pk=obj.pk).status
            except AdminRequest.DoesNotExist:
                previous_status = None

        if obj.payment_verified and not obj.payment_verified_at:
            obj.payment_verified_at = timezone.now()

        super().save_model(request, obj, form, change)

        if obj.status == AdminRequest.STATUS_APPROVED and previous_status != AdminRequest.STATUS_APPROVED:
            user = obj.user
            user.role = User.ROLE_ADMIN
            user.admin_approved = True
            user.is_staff = False
            user.is_superuser = False
            user.is_active = True
            user.save()

            self.create_company_and_vehicle(obj, request.user)

            obj.reviewed_by = request.user
            obj.reviewed_at = timezone.now()

            if not obj.review_note:
                obj.review_note = (
                    'Solicitud KYC aprobada manualmente desde el formulario. '
                    'Empresa y taxi inicial creados automáticamente.'
                )

            super().save_model(request, obj, form, change)

    def create_company_and_vehicle(self, admin_request, reviewer):
        user = admin_request.user

        company, created = Company.objects.get_or_create(
            owner=user,
            name=admin_request.company_name,
            defaults={
                'legal_name': admin_request.company_name,
                'phone': admin_request.phone,
                'email': user.email,
                'city': admin_request.city,
                'address': admin_request.address,
                'status': Company.STATUS_ACTIVE,
                'notes': (
                    'Empresa creada automáticamente al aprobar solicitud KYC. '
                    f'Solicitud ID: {admin_request.id}'
                ),
                'created_by': reviewer,
            }
        )

        if admin_request.main_taxi_plate:
            Vehicle.objects.get_or_create(
                plate_number=admin_request.main_taxi_plate,
                defaults={
                    'company': company,
                    'internal_code': f'TX-{admin_request.id}',
                    'brand': admin_request.main_taxi_brand or 'No especificada',
                    'model': admin_request.main_taxi_model or '',
                    'color': admin_request.main_taxi_color or '',
                    'daily_target_amount': 0,
                    'status': Vehicle.STATUS_ACTIVE,
                    'registration_document': admin_request.taxi_registration_document,
                    'insurance_document': admin_request.taxi_license_document,
                    'notes': (
                        'Taxi creado automáticamente desde solicitud KYC. '
                        f'Solicitud ID: {admin_request.id}'
                    ),
                    'created_by': reviewer,
                }
            )

        return company

    def approve_requests(self, request, queryset):
        approved_count = 0

        for admin_request in queryset.filter(status=AdminRequest.STATUS_PENDING):
            user = admin_request.user

            user.role = User.ROLE_ADMIN
            user.admin_approved = True
            user.is_staff = False
            user.is_superuser = False
            user.is_active = True
            user.save()

            self.create_company_and_vehicle(admin_request, request.user)

            admin_request.status = AdminRequest.STATUS_APPROVED
            admin_request.reviewed_by = request.user
            admin_request.reviewed_at = timezone.now()

            if not admin_request.review_note:
                admin_request.review_note = (
                    'Solicitud KYC aprobada. Usuario activado como propietario, '
                    'empresa creada automáticamente y taxi principal registrado si fue indicado.'
                )

            admin_request.save()
            approved_count += 1

        self.message_user(
            request,
            f'{approved_count} solicitud(es) KYC aprobada(s). Empresa y taxi inicial creados automáticamente.'
        )

    approve_requests.short_description = 'Aprobar KYC y crear empresa/taxi'

    def reject_requests(self, request, queryset):
        rejected_count = 0

        for admin_request in queryset.filter(status=AdminRequest.STATUS_PENDING):
            admin_request.status = AdminRequest.STATUS_REJECTED
            admin_request.reviewed_by = request.user
            admin_request.reviewed_at = timezone.now()

            if not admin_request.review_note:
                admin_request.review_note = 'Solicitud KYC rechazada desde el panel principal.'

            admin_request.save()
            rejected_count += 1

        self.message_user(
            request,
            f'{rejected_count} solicitud(es) KYC rechazada(s).'
        )

    reject_requests.short_description = 'Rechazar solicitudes KYC seleccionadas'
