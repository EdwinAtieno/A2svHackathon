from django.contrib import admin
from apps.profiles.models import Profiles, Income, Expense, Savings, Goals


# Register your models here.

class IncomeListInline(admin.TabularInline):
    model = Income
    extra = 0


class ExpenseListInline(admin.TabularInline):
    model = Expense
    extra = 0


class SavingsListInline(admin.TabularInline):
    model = Savings
    extra = 0


class GoalsListInline(admin.TabularInline):
    model = Goals
    extra = 0


class ProfilesAdmin(admin.ModelAdmin):
    model = Profiles
    inlines = [IncomeListInline, ExpenseListInline, SavingsListInline, GoalsListInline]
    list_display = (
        "id",
        "user",
    )


admin.site.register(Profiles, ProfilesAdmin)
