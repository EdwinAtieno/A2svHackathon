from typing import Any

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import (
    AbstractBaseUser,
    Group,
    PermissionsMixin,
)
from django.db.models import JSONField 
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from apps.abstracts import IDModel, TimeStampedModel
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
    # Basic information
    first_name = models.CharField(max_length=255, verbose_name=_("First Name"))
    middle_name = models.CharField(
        max_length=255, verbose_name=_("Middle Name"), blank=True, null=True
    )
    last_name = models.CharField(max_length=255, verbose_name=_("Last Name"))
    phone_number = models.CharField(
        max_length=20,
        unique=True,
        verbose_name=_("Phone Number"),
        validators=[phone_number_validator],
    )

    country = models.CharField(
        max_length=255, verbose_name=_("Country"),
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

    # Financial Information
    ACCOUNT_TYPES = [
        ('Savings', 'Savings Account'),
        ('Checking', 'Checking Account'),
        ('Investment', 'Investment Account'),
        ('Loan', 'Loan Account'),
    ]
    
    account_type = models.CharField(
        max_length=50,
        choices=ACCOUNT_TYPES,
        verbose_name=_("Account Type"),
        default='Savings',
    )
    monthly_income = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        verbose_name=_("Monthly Income"),
        default=0.00  
    )

    monthly_expenses = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        verbose_name=_("Monthly Expenses"),
        default=0.00  
    )

    savings_balance = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        verbose_name=_("Savings Balance"),
        default=0.00 
    )

    loan_balance = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        verbose_name=_("Loan Balance"),
        default=0.00 
    )

    credit_card_limit = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name=_("Credit Card Limit"),
        default=None 
    )

    fixed_deposit_balance = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name=_("Fixed Deposit Balance"),
        default=None 
    )

    monthly_deposit = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Monthly Deposit"),
        default=0.00 
    )

    mortgage_balance = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name=_("Mortgage Balance"),
        default=None
    )

    spending_pattern = models.CharField(
        max_length=20,
        choices=[
            ('Low', 'Low'),
            ('Medium', 'Medium'),
            ('High', 'High'),
        ],
        verbose_name=_("Spending Pattern"),
        default='Low'
    )

    risk_tolerance = models.CharField(
        max_length=20,
        choices=[
            ('Low', 'Low'),
            ('Medium', 'Medium'),
            ('High', 'High'),
        ],
        verbose_name=_("Risk Tolerance"),
        default='Medium'
    )

    employment_type = models.CharField(
        max_length=50,
        choices=[
            ('Salaried', 'Salaried'),
            ('Self-Employed', 'Self-Employed'),
            ('Business Owner', 'Business Owner'),
        ],
        verbose_name=_("Employment Type"),
        default='Salaried'
    )

    age = models.PositiveIntegerField(verbose_name=_("Age"),  default=30)
    dependents = models.PositiveIntegerField(verbose_name=_("Dependents"),  default=3)
    chat_records = JSONField(verbose_name=_("Chat Records"), default=list)

    objects = UserManager()

    USERNAME_FIELD = "email"

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} - {self.phone_number}"

    def get_full_name(self) -> str:
        return f"{self.first_name or ''} {self.middle_name or ''} {self.last_name or ''}"

    def assess_spending_pattern(self):
        if (
            self.credit_card_limit is not None
            and self.loan_balance is not None
            and self.mortgage_balance is not None
        ):
            if (
                self.credit_card_limit > 10000
                and self.loan_balance > 5000
                and self.mortgage_balance > 50000
            ):
                return 'High'
        return 'Low'

    def assess_risk_tolerance(self):
        if self.spending_pattern == 'High':
            return 'High'
        elif self.savings_balance is not None and self.savings_balance > 10000:
            return 'Low'
        else:
            return 'Medium'

    def clean(self):
        super().clean()

        # Validate that expenses are not greater than income
        if self.monthly_expenses > self.monthly_income:
            raise ValidationError("Expenses cannot be greater than income.")

        # Validate that the savings balance is non-negative
        if self.savings_balance is not None and self.savings_balance < 0:
            raise ValidationError("Savings balance cannot be negative.")

        # Validate that the loan balance, if provided, is non-negative
        if self.loan_balance is not None and self.loan_balance < 0:
            raise ValidationError("Loan balance cannot be negative.")

        # Validate that the credit card limit, if provided, is non-negative
        if self.credit_card_limit is not None and self.credit_card_limit < 0:
            raise ValidationError("Credit card limit cannot be negative.")

        # Validate that the monthly deposit is non-negative
        if self.monthly_deposit < 0:
            raise ValidationError("Monthly deposit cannot be negative.")
