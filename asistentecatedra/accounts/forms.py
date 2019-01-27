from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe

User = get_user_model()


class SignupForm(UserCreationForm):

    terms = forms.BooleanField(
        label=mark_safe(
            'Acepto las <a href="#" class="terms">Condiciones de Servicio</a> '
            'y la <a href="#" class="terms">Política de Privacidad</a> de '
            'Asistente de Cátedra'),
        required=True
    )
    # institution_logo = forms.ImageField(required=False,)

    class Meta:
        model = User
        fields = (
            'name',
            'email',
            'password1',
            'password2',
        )

    def __init__(self, *args, **kwargs):
        """Makes email to be required"""
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = \
            'Asegúrese que la contraseña tenga al menos 8 caracteres, '\
            'incluidos un número y una mayúscula.'
