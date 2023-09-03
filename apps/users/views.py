from django.contrib.auth import (
    get_user_model,
)
from rest_framework import (
    generics,
)
from rest_framework.permissions import IsAuthenticated
from apps.users.serializers import UserSerializer

User = get_user_model()


class UserList(generics.ListCreateAPIView):
    """
    List all users, or create a new user by admin.
    """

    queryset = User.objects.prefetch_related("groups").all()
    serializer_class = UserSerializer
    # permission_classes = (IsAuthenticated,)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a user instance.
    """

    queryset = User.objects.prefetch_related("groups").all()
    serializer_class = UserSerializer
    permission_classes = (
        IsAuthenticated,)


