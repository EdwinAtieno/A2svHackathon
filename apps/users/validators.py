import re
from django.core.exceptions import ValidationError

def phone_number_validator(value: str) -> None:
    """
    Validate phone number.
    """

    if re.match(r"^(?:\+\d{1,3}\s?)?\d{4,15}$", value):
        return value

    raise ValidationError("Invalid phone number")
