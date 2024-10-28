from django.core.validators import MinLengthValidator
from django.db import models
from FurryFunnies.author.utils import ValidatorOnlyLetters, ValidatorPasscode


class Author(models.Model):
    first_name = models.CharField(
        max_length=40,
        validators=[ValidatorOnlyLetters(), MinLengthValidator(4)],
    )

    last_name = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2), ValidatorOnlyLetters]
    )

    passcode = models.CharField(
        max_length=6,
        validators=[ValidatorPasscode()],
        help_text= "Your passcode must be a combination of 6 digits.",
    )

    pets_number = models.PositiveSmallIntegerField()
    info = models.TextField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
