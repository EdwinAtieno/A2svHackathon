from django.urls import path
from .views import UserList, UserDetail, analyze_customer

urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<uuid:pk>/', UserDetail.as_view(), name='user-detail'),
    path('analyze-customer/<uuid:customer_id>/', analyze_customer, name='analyze-customer'),
]
