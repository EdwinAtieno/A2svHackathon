<<<<<<< HEAD
from django.urls import path

from apps.users.views import UserDetail, UserList

urlpatterns = [
    path("users/", UserList.as_view(), name="users-list"),
    path("users/<str:pk>/", UserDetail.as_view(), name="users-detail"),
]
=======
from django.urls import path

from apps.users.views import (
    UserDetail,
    UserList,
)

urlpatterns = [
    path(
        "users/",
        UserList.as_view(),
        name="users-list",
    ),
    path("users/<str:pk>/", UserDetail.as_view(), name="users-detail"),
]
>>>>>>> 75c18a1 (feat profiles)
