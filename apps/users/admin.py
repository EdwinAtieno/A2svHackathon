from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from apps.admin_filters import CreatedAtFilter
from apps.users.constants import USER_SEARCH_FIELDS

User = get_user_model()

class CustomUserAdmin(DjangoUserAdmin):
    list_display = (
        "id",
        "email",
        "first_name",
        "last_name",
        "phone_number",
        "is_active",
        "is_staff",
        "is_superuser",
        "last_login",
    )
    list_filter = ("is_staff", "is_superuser", CreatedAtFilter)
    search_fields = USER_SEARCH_FIELDS
    ordering = ("first_name", "last_name")
    list_per_page = 25

    fieldsets = (
        ("Personal info", {"fields": ("first_name", "last_name", "country")}),
        ("Contact info", {"fields": ("email", "phone_number")}),
        ("Important dates", {"fields": ("last_login",)}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
    )

    add_fieldsets = (
        (
            "Personal info",
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "phone_number",
                    "password1",
                    "password2",
                ),
            },
        ),
        (
            "Permissions",
            {
                "fields": ("is_active", "is_staff", "is_superuser"),
            },
        ),
    )

admin.site.register(User, CustomUserAdmin)
