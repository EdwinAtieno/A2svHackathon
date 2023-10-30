from django.contrib import admin
from .models import Income, Expenses, Savings, Goals, UserProfile

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('user', 'source', 'amount', 'frequency')

@admin.register(Expenses)
class ExpensesAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'amount')

@admin.register(Savings)
class SavingsAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'amount')

@admin.register(Goals)
class GoalsAdmin(admin.ModelAdmin):
    list_display = ('user', 'description', 'target')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    filter_horizontal = ('income', 'expenses', 'savings', 'goals')
