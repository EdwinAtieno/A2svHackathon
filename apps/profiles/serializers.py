from rest_framework import serializers
from apps.profiles.models import Income, Expense, Savings, Goals, Profiles
from django.contrib.auth import get_user_model

User = get_user_model()


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'


class SavingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Savings
        fields = '__all__'


class GoalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goals
        fields = '__all__'


class ProfilesSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='first_name'
    )

    class Meta:
        model = Profiles
        fields = '__all__'
