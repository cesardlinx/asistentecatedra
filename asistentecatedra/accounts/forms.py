from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
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
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'institution',
        )

    def __init__(self, *args, **kwargs):
        """Makes email to be required"""
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = \
            'Asegúrese que la contraseña tenga al menos 8 caracteres, '\
            'incluidos un número y una mayúscula.'
        self.fields['institution'].label = 'Institución'


class ProfileForm(ModelForm):
    """Profile form used to update users"""
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'institution',
            'institution_logo',
            'allow_notifications'
        )

    def __init__(self, *args, **kwargs):
        """Sets the fields as not required """
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = False
        self.fields['last_name'].required = False
        self.fields['institution'].required = False
        self.fields['institution_logo'].required = False
        self.fields['allow_notifications'].required = False

    def clean(self):
        """Returns cleaned data only if is not none"""
        cleaned_data = super().clean()
        cleaned_data = {key: field for key, field in cleaned_data.items()
                        if field is not None}
        return cleaned_data
