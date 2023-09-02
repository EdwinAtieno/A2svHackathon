from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from apps.admin_filters import CreatedAtFilter
from apps.users.constants import (
    USER_SEARCH_FIELDS,
)



User = get_user_model()


class UserAdmin(DjangoUserAdmin):
    list_display = (
        # "id",
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
        "is_superuser",
        "phone_number",
    )

    list_filter = ("is_staff", "is_superuser")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("first_name", "last_name")
    fieldsets = (
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "password",
                    "country",
                )
            },
        ),
        (
            "Contact info",
            {"fields": ("email",)},
        ),
        ("Important dates", {"fields": ("last_login",)}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
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
                    "password1",
                    "password2",
                ),
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
    )


admin.site.register(User, UserAdmin)
