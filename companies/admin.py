from django.contrib import admin
from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'phone', 'city', 'status', 'created_at')
    list_filter = ('status', 'city', 'created_at')
    search_fields = ('name', 'legal_name', 'phone', 'email', 'owner__username')
    readonly_fields = ('created_at', 'updated_at')
