from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible()
class ValidatorOnlyLetters:
    message = "Your name must contain letters only!"

    def __call__(self, value):
        if not value.isalpha():
            raise ValidationError(self.message)


@deconstructible()
class ValidatorPasscode:
    message = "Your passcode must be exactly 6 digits!"

    def __call__(self, value):
        if not (value.isdigit() and len(value) == 6):
            raise ValidationError(self.message)
