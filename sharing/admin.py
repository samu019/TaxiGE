from django.contrib import admin
from .models import CompanyMember, TaxiShareInvite


@admin.register(CompanyMember)
class CompanyMemberAdmin(admin.ModelAdmin):
    list_display = (
        "company",
        "user",
        "role",
        "is_active",
        "can_view_payments",
        "can_view_damages",
        "can_add_payments",
        "can_edit_data",
        "created_at",
    )
    list_filter = ("role", "is_active", "created_at")
    search_fields = ("company__name", "user__username", "user__email")


@admin.register(TaxiShareInvite)
class TaxiShareInviteAdmin(admin.ModelAdmin):
    list_display = (
        "company",
        "invited_by",
        "role",
        "used_count",
        "max_uses",
        "is_active",
        "expires_at",
        "created_at",
    )
    list_filter = ("role", "is_active", "created_at")
    search_fields = ("company__name", "invited_by__username", "token")
    readonly_fields = ("token", "used_count", "created_at")