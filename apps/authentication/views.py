from typing import Any

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.authentication.permissions import IsOwner
from apps.authentication.serializers import (
    ChangePasswordSerializer,
    ForgotPasswordSerializer,
    MyTokenObtainPairSerializer,
)

User = get_user_model()


class MyTokenObtainPairView(TokenObtainPairView):  # type: ignore
    serializer_class = MyTokenObtainPairSerializer


class ChangePassword(GenericAPIView):
    """
    Validates a user's password and changes it to a new password
    """

    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer
    permission_classes = (IsAuthenticated, IsOwner)

    def patch(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"message": "Password changed successfully"},
            status=status.HTTP_200_OK,
        )


class ForgotPassword(GenericAPIView):
    """
    Sends a new password to a user's phone number
    """

    serializer_class = ForgotPasswordSerializer

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"message": "New password sent to phone number"},
            status=status.HTTP_200_OK,
        )
