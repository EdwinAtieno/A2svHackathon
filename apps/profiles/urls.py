from django.urls import path
from .views import (
    IncomeListCreateView,
    IncomeDetailView,
    ExpensesListCreateView,
    ExpensesDetailView,
    SavingsListCreateView,
    SavingsDetailView,
    GoalsListCreateView,
    GoalsDetailView,
    UserProfileView,
)

urlpatterns = [
    path('api/income/', IncomeListCreateView.as_view(), name='income-list'),
    path('api/income/<int:pk>/', IncomeDetailView.as_view(), name='income-detail'),

    path('api/expenses/', ExpensesListCreateView.as_view(), name='expenses-list'),
    path('api/expenses/<int:pk>/', ExpensesDetailView.as_view(), name='expenses-detail'),

    path('api/savings/', SavingsListCreateView.as_view(), name='savings-list'),
    path('api/savings/<int:pk>/', SavingsDetailView.as_view(), name='savings-detail'),

    path('api/goals/', GoalsListCreateView.as_view(), name='goals-list'),
    path('api/goals/<int:pk>/', GoalsDetailView.as_view(), name='goals-detail'),

    path('api/profile/', UserProfileView.as_view(), name='user-profile'),
]
