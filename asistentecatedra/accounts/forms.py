from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe

User = get_user_model()


class SignupForm(UserCreationForm):

    terms = forms.BooleanField(
        label=mark_safe(
            'Acepto las <a href="#">Condiciones de Servicio</a> y la '
            '<a href="#">Política de Privacidad</a> de Asistente de Cátedra'),
        required=True
    )
    # institution_logo = forms.ImageField(required=False,)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'institution'
        )
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'institution': 'Institución',
        }

    def __init__(self, *args, **kwargs):
        """Makes email to be required"""
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['password1'].help_text = \
            'Asegúrese que la contraseña contenga más de 10 caracteres, '\
            'incluidos un número y una mayúscula.'
        self.fields['first_name'].help_text = '(Opcional)'
        self.fields['last_name'].help_text = '(Opcional)'
        self.fields['institution'].help_text = '(Opcional)'
