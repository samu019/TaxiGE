from django.contrib import admin
from .models import Vehicle


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'plate_number', 'brand', 'model', 'company', 'daily_target_amount', 'status')
    list_filter = ('status', 'brand', 'company')
    search_fields = ('plate_number', 'brand', 'model', 'company__name')
    readonly_fields = ('created_at', 'updated_at')
