from django.urls import path

from apps.users.views import (
    UserDetail,
    UserList,
    analyze_customer
)

urlpatterns = [
    path(
        "users/",
        UserList.as_view(),
        name="users-list",
    ),
    path("users/<str:pk>/", UserDetail.as_view(), name="users-detail"),
    path('analyze/<int:id>/', analyze_customer, name='analyze_customer'),
]
