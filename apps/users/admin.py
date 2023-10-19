from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from apps.admin_filters import CreatedAtFilter
from apps.users.constants import USER_SEARCH_FIELDS

User = get_user_model()

class MonthlyIncomeValidator:
    def __init__(self, min_value=0):
        self.min_value = min_value

    def __call__(self, value):
        if value < self.min_value:
            raise ValidationError(
                f'{value} is less than the minimum allowed value of {self.min_value}',
                params={'value': value, 'min_value': self.min_value},
            )

class CustomUserAdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'middle_name',
            'last_name',
            'phone_number',
            'country',
            'email',
            'gender',
            'is_active',
            'is_staff',
            'is_available',
            'account_type',
            'monthly_income',
            'monthly_expenses',
            'savings_balance',
            'loan_balance',
            'credit_card_limit',
            'fixed_deposit_balance',
            'monthly_deposit',
            'mortgage_balance',
            'employment_type',
            'default',
            'loan',
            'age',
            'dependants',
            'marital_status',
            'emergency_fund_bal',
        ]

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

    personal_info_fields = ("first_name", "last_name", "country", "age")
    contact_info_fields = ("email", "phone_number")
    financial_info_fields = (
        "employment_type", "account_type", "monthly_income", "monthly_expenses",
        "savings_balance", "loan_balance", "credit_card_limit",
        "fixed_deposit_balance", "monthly_deposit", "mortgage_balance","loan", "default",
    )
    other_info_fields = ("dependants", "marital_status")

    fieldsets = (
        ("Personal info", {"fields": personal_info_fields}),
        ("Contact info", {"fields": contact_info_fields}),
        ("Important dates", {"fields": ("last_login",)}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Financial info", {"fields": financial_info_fields}),
        ("Other information", {"fields": other_info_fields}),
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
                    "account_type", "monthly_income", "monthly_expenses",
                    "savings_balance", "loan_balance", "credit_card_limit",
                    "fixed_deposit_balance", "monthly_deposit", "mortgage_balance",
                    "employment_type", "emergency_fund_bal",
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
