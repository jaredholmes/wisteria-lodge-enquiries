from datetime import timedelta, date
# from required import Required, R

from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_email, validate_integer

# Validators
"""Check that name does not contain numbers or
special characters"""
def validate_alpha(value):
    if not value.isalpha():
        raise ValidationError(
            _('\'%(value)s\' contains non-alphabetical characters'),
            params={'value': value},
        )
    return value

"""Check that date is tomorrow or later"""
def validate_future(value):
    now = date.today()
    if value - now < timedelta(days=1):
        raise ValidationError(
         _('%(value)s is earlier than tomorrow'),
         params={'value': value},
        )
