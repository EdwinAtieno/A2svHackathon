from rest_framework import generics
from .models import Income, Expenses, Savings, Goals, UserProfile
from .serializers import IncomeSerializer, ExpensesSerializer, SavingsSerializer, GoalsSerializer, UserProfileSerializer

class IncomeListCreateView(generics.ListCreateAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer

class IncomeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer

class ExpensesListCreateView(generics.ListCreateAPIView):
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializer

class ExpensesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializer

class SavingsListCreateView(generics.ListCreateAPIView):
    queryset = Savings.objects.all()
    serializer_class = SavingsSerializer

class SavingsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Savings.objects.all()
    serializer_class = SavingsSerializer

class GoalsListCreateView(generics.ListCreateAPIView):
    queryset = Goals.objects.all()
    serializer_class = GoalsSerializer

class GoalsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Goals.objects.all()
    serializer_class = GoalsSerializer

class UserProfileView(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
