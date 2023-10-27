from django.contrib.auth import get_user_model
from rest_framework import generics, views, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
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

    def perform_create(self, serializer):
        serializer.save()


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a user instance.
    """

    queryset = User.objects.prefetch_related("groups").all()
    serializer_class = UserSerializer
    # permission_classes = (IsAuthenticated,)

