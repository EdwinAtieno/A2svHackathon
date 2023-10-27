from django.shortcuts import render
from apps.profiles.models import Income, Expense, Savings, Goals, Profiles
from apps.profiles.serializers import IncomeSerializer, ExpenseSerializer, SavingsSerializer, GoalsSerializer, \
    ProfilesSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# Create your views here.

class IncomeList(ListCreateAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer


class IncomeDetail(RetrieveUpdateDestroyAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer


class ExpenseList(ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class ExpenseDetail(RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class SavingsList(ListCreateAPIView):
    queryset = Savings.objects.all()
    serializer_class = SavingsSerializer


class SavingsDetail(RetrieveUpdateDestroyAPIView):
    queryset = Savings.objects.all()
    serializer_class = SavingsSerializer


class GoalsList(ListCreateAPIView):
    queryset = Goals.objects.all()
    serializer_class = GoalsSerializer


class GoalsDetail(RetrieveUpdateDestroyAPIView):
    queryset = Goals.objects.all()
    serializer_class = GoalsSerializer


class ProfilesList(ListCreateAPIView):
    queryset = Profiles.objects.all()
    serializer_class = ProfilesSerializer


class ProfilesDetail(RetrieveUpdateDestroyAPIView):
    queryset = Profiles.objects.all()
    serializer_class = ProfilesSerializer
