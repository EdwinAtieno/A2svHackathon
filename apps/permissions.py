from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.views import APIView


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Only grant permissions to actions if admin else can only read
    """

    def has_permission(self, request: Request, view: APIView) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user.is_staff)


class IsAdminOrDeliveryOfficer(permissions.BasePermission):
    def has_permission(self, request: Request, view: APIView) -> bool:
        if request.user.is_superuser:
            return True

        if request.user.groups.filter(name="delivery_officer").exists():  # type: ignore[union-attr]
            return True

        return False


class IsAdminOrDeliveryAdmin(permissions.BasePermission):
    def has_permission(self, request: Request, view: APIView) -> bool:
        if request.user.is_superuser:
            return True

        if request.user.groups.filter(name="delivery_admin").exists():  # type: ignore[union-attr]
            return True

        return False


class IsAdminAgentOrDeliveryOfficer(permissions.BasePermission):
    def has_permission(self, request: Request, view: APIView) -> bool:
        if request.user.is_superuser:
            return True

        if request.user.groups.filter(name="agent").exists():  # type: ignore[union-attr]
            return True

        if request.user.groups.filter(name="delivery_officer").exists():  # type: ignore[union-attr]
            return True

        return False


class IsAdminAgentCX(permissions.BasePermission):
    def has_permission(self, request: Request, view: APIView) -> bool:
        if request.user.is_superuser:
            return True

        if request.user.groups.filter(name="agent").exists():  # type: ignore[union-attr]
            return True

        if request.user.groups.filter(name="customer_experience").exists():  # type: ignore[union-attr]
            return True

        return False
