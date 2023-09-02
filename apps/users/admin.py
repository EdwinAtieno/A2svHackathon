from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from apps.admin_filters import CreatedAtFilter
from apps.users.constants import (
    USER_SEARCH_FIELDS,
)



User = get_user_model()


class UserAdmin(DjangoUserAdmin):
    model = User
    list_display = (
        "id",
        "first_name",
        "middle_name",
        "last_name",
        "country",
        "phone_number",
        "email",
        "created_at",
        "is_superuser",
    )
    list_display_links = (
        "id",
        "phone_number",
    )
    readonly_fields = ("id", "created_at", "updated_at")
    list_filter = (
        CreatedAtFilter,
        "is_staff",
        "is_superuser",
        "is_active",
    )
    ordering = ("first_name", "last_name")
    search_fields = USER_SEARCH_FIELDS
    exclude = ("username", "email", "date_joined")

    fieldsets = (
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "middle_name",
                    "last_name",
                    "password",
                )
            },
        ),
        (
            "Contact info",
            {"fields": ("phone_number", "email", "country")},
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
                    "middle_name",
                    "password1",
                    "password2",
                ),
            },
        ),
        (
            "Contact info",
            {"fields": ("phone_number", "email", "country")},
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
