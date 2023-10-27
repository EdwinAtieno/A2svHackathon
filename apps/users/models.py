from typing import Any

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import (
    AbstractBaseUser,
    Group,
    PermissionsMixin,
)
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.abstracts import (
    IDModel,
    TimeStampedModel,
)
from apps.users.validators import phone_number_validator


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(
        self, email: str, password: str, **kwargs: Any
    ) -> Any:
        """
        Creates and saves a User with the given phone_number and password.
        """

        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(
        self, email: str, password: str, **kwargs: Any
    ) -> Any:
        kwargs.setdefault("is_superuser", False)
        return self._create_user(email, password, **kwargs)

    def create_superuser(
        self, email: str, password: str, **kwargs: Any
    ) -> Any:
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("is_staff", True)
        superuser = self._create_user(email, password, **kwargs)
        group, _ = Group.objects.get_or_create(name="admin")
        superuser.groups.add(group)

        return superuser


class User(AbstractBaseUser, PermissionsMixin, IDModel, TimeStampedModel):
    first_name = models.CharField(max_length=255, verbose_name=_("First Name"))
    middle_name = models.CharField(
        max_length=255, verbose_name=_("Middle Name"), blank=True, null=True
    )
    last_name = models.CharField(max_length=255, verbose_name=_("Last Name"))
    phone_number = models.CharField(
        max_length=20,
        unique=True,
        verbose_name=_("Phone Number"),
        validators=[
            phone_number_validator,
        ],
    )

    country = models.CharField(
        max_length=255, verbose_name=_("country"),
    )

    email = models.CharField(
        verbose_name=_("Email Address"),
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_(
            "Designates whether the user can log into this admin site."
        ),
    )

    is_available = models.BooleanField(
        _("available"),
        default=True,
    )

    objects = UserManager()

    USERNAME_FIELD = "email"

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ["-created_at"]

    def __str__(self) -> str:
        # return f"{self.first_name} {self.last_name} - {self.phone_number}"
        return f"{self.id}"

    def get_full_name(self) -> str:
        return f"{self.first_name or ''} {self.middle_name or ''} {self.last_name or ''}"

