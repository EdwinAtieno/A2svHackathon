import re
from typing import Any

from django.core.exceptions import ValidationError


def phone_number_validator(value: str) -> Any:
    """
    Validate phone number.
    """

    if re.match(  # noqa W605 type: ignore["return-value"]
        r"^(?:\+?88)?01[13-9]\d{8}$", value
    ):
        return value

    raise ValidationError("Invalid phone number")
