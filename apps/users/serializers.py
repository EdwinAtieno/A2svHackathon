from typing import Any

from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from apps.users.validators import phone_number_validator

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=255)
    middle_name = serializers.CharField(max_length=255, required=False)
    last_name = serializers.CharField(max_length=255)
    phone_number = serializers.CharField(
        max_length=20,
        validators=[
            phone_number_validator,
            UniqueValidator(
                queryset=User.objects.all(),
                message="This phonenumber already exists",
                lookup="iexact",
            ),
        ],
    )
    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="This email already exists",
                lookup="iexact",
            )
        ],
    )
    country = serializers.CharField(
        required=False, default="Kenya", max_length=255
    )
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "middle_name",
            "last_name",
            "phone_number",
            "email",
            "country",
            "user",
        )
        read_only_fields = ("id",)

    def validate_phone_number(self, phone_number: Any) -> Any:
        if not User.objects.filter(
            Q(phone_number=phone_number)
            | Q(alternate_phone_number=phone_number)
        ).exists():
            return phone_number

        raise serializers.ValidationError("This phonenumber already exists")

    def validate_email(self, email: Any) -> Any:
        if not User.objects.filter(email=email).exists():
            return email

        raise serializers.ValidationError("This email already exists")

    def create(self, validated_data: dict) -> User:
        return User.objects.create(**validated_data)

