from django.contrib import admin
from .models import Driver


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone', 'company', 'assigned_vehicle', 'daily_payment_amount', 'status')
    list_filter = ('status', 'company')
    search_fields = ('full_name', 'phone', 'identity_number', 'license_number', 'company__name')
    readonly_fields = ('created_at', 'updated_at')
