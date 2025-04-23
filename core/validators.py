import re
from django.core.exceptions import ValidationError

def validate_phone_number(value):
    phone_regex = re.compile(r"^[6-9]\d{9}$")
    if not phone_regex.match(value):
        raise ValidationError(
            f"{value} is not a valid phone number. It should start with 6, 7, 8, or 9 and be followed by 9 digits."
        )