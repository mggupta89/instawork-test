from django.core.exceptions import ValidationError
from django.utils import timezone
from django.core.validators import validate_email

default_tzone = timezone.get_default_timezone()


def is_valid_email(email):
    try:
        validate_email(email)
    except ValidationError:
        return False
    return True