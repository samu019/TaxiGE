from django.contrib import admin
from .models import DriverPayment


@admin.register(DriverPayment)
class DriverPaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'driver', 'vehicle', 'company', 'payment_date', 'expected_amount', 'paid_amount', 'debt_amount', 'status')
    list_filter = ('status', 'company', 'payment_date')
    search_fields = ('driver__full_name', 'vehicle__plate_number', 'company__name')
    readonly_fields = ('created_at', 'updated_at', 'debt_amount')
