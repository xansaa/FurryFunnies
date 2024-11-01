# author/forms.py
from django import forms
from .models import Author
from FurryFunnies.mixins import PlaceholderMixin


class AuthorProfileForm(forms.ModelForm, PlaceholderMixin):
    passcode = forms.CharField(
        label="Passcode",
        widget=forms.PasswordInput(),
        help_text="Your passcode must be a combination of 6 digits"
    )

    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'passcode', 'pets_number']
