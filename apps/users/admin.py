from django import forms
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from apps.admin_filters import CreatedAtFilter
from apps.users.constants import USER_SEARCH_FIELDS
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class MonthlyIncomeValidator:
    def __init__(self, min_value=0):
        self.min_value = min_value

    def __call__(self, value):
        if value < self.min_value:
            raise ValidationError(
                _('%(value)s is less than the minimum allowed value of %(min_value)s'),
                params={'value': value, 'min_value': self.min_value},
            )

class CustomUserAdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

    monthly_income = forms.DecimalField(
        label='Monthly Income',
        widget=forms.TextInput(attrs={'placeholder': 'Enter monthly income'}),
        validators=[MonthlyIncomeValidator()],
    )

    def clean_monthly_income(self):
        monthly_income = self.cleaned_data['monthly_income']
        if monthly_income < 0:
            raise forms.ValidationError("Monthly income cannot be negative.")
        return monthly_income

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
    form = CustomUserAdminForm 

    fieldsets = (
        ("Personal info", {"fields": ("first_name", "last_name", "country", "age", "dependants","marital_status")}),
        ("Contact info", {"fields": ("email", "phone_number")}),
        ("Important dates", {"fields": ("last_login",)}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Financial info", {
            "fields": (
                "employment_type",
                "account_type",
                "monthly_income",
                "monthly_expenses",
                "savings_balance",
                "loan_balance",
                "credit_card_limit",
                "fixed_deposit_balance",
                "monthly_deposit",
                "mortgage_balance",
                "spending_pattern",
                "risk_tolerance",
            ),
        }),
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
            "Financial info",
            {
                "fields": (
                    "account_type",
                    "monthly_income",
                    "monthly_expenses",
                    "savings_balance",
                    "loan_balance",
                    "credit_card_limit",
                    "fixed_deposit_balance",
                    "monthly_deposit",
                    "mortgage_balance",
                    "spending_pattern",
                    "risk_tolerance",
                    "employment_type",
                    "age",
                    "dependents",
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
