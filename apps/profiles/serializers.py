from rest_framework import serializers
from .models import Income, Expenses, Savings, Goals, UserProfile

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'

class ExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = '__all__'

class SavingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Savings
        fields = '__all__'

class GoalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goals
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    income = IncomeSerializer(many=True)
    expenses = ExpensesSerializer(many=True)
    savings = SavingsSerializer(many=True)
    goals = GoalsSerializer(many=True)

    class Meta:
        model = UserProfile
        fields = '__all__'
