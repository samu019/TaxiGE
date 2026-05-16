from django.contrib import admin
from .models import VehicleDamage


@admin.register(VehicleDamage)
class VehicleDamageAdmin(admin.ModelAdmin):
    list_display = ('id', 'vehicle', 'driver', 'company', 'title', 'estimated_cost', 'final_cost', 'damage_date', 'status')
    list_filter = ('status', 'company', 'damage_date')
    search_fields = ('title', 'vehicle__plate_number', 'driver__full_name', 'company__name')
    readonly_fields = ('created_at', 'updated_at')
