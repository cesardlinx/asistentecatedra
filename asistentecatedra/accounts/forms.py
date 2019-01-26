from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignupForm(UserCreationForm):
    institution = forms.CharField(
        label='Institución',
        max_length=100,
        required=False,
    )
    institution_logo = forms.ImageField(required=False,)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        )

    def __init__(self, *args, **kwargs):
        """Makes email to be required"""
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
