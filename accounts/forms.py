from io import BytesIO
from django.core.files import File
from PIL import Image
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (PasswordChangeForm, SetPasswordForm,
                                       UserCreationForm)
from django.core.validators import MinValueValidator
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

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
            'La contraseña debe tener al menos 8 caracteres'
        self.fields['institution'].label = 'Institución'


class ProfileForm(forms.ModelForm):
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
        widgets = {'institution_logo': forms.FileInput()}

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


class PhotoForm(forms.ModelForm):
    """Form for the user to upload a photo"""
    x = forms.FloatField(
        widget=forms.HiddenInput(),
        validators=[MinValueValidator(0)]
    )
    y = forms.FloatField(
        widget=forms.HiddenInput(),
        validators=[MinValueValidator(0)]
    )
    width = forms.FloatField(
        widget=forms.HiddenInput(),
        validators=[MinValueValidator(0)]
    )
    height = forms.FloatField(
        widget=forms.HiddenInput(),
        validators=[MinValueValidator(0)]
    )

    class Meta:
        model = User
        fields = ('photo',)

    def __init__(self, *args, **kwargs):
        """Sets the fields as required """
        super().__init__(*args, **kwargs)
        self.fields['x'].required = True
        self.fields['y'].required = True
        self.fields['width'].required = True
        self.fields['height'].required = True
        self.fields['photo'].required = True

    def clean(self):
        cleaned_data = super().clean()
        photo = cleaned_data.get('photo')
        x = cleaned_data.get('x')
        y = cleaned_data.get('y')
        width = cleaned_data.get('width')
        height = cleaned_data.get('height')

        if photo and x and x > photo.image.size[0]:
            raise forms.ValidationError(
                'x field cant be bigger than image width.'
            )

        if photo and y and y > photo.image.size[1]:
            raise forms.ValidationError(
                'y field cant be bigger than image height.'
            )

        if photo and width and width > photo.image.size[0]:
            raise forms.ValidationError(
                'width field cant be bigger than image width.'
            )

        if photo and height and height > photo.image.size[1]:
            raise forms.ValidationError(
                'height field cant be bigger than image height.'
            )

        return cleaned_data

    def save(self, commit=True):
        super().save(commit=False)

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')

        # Cropping and resizing image

        image = Image.open(self.instance.photo)
        cropped_image = image.crop((x, y, w+x, h+y))
        resized_image = cropped_image.resize((180, 180), Image.ANTIALIAS)

        stream = BytesIO()

        try:
            resized_image.save(stream, format=image.format)

            # Saving image in instance field
            self.instance.photo.save(self.instance.photo.name,
                                     File(stream), save=False)
        except IOError:
            pass
        finally:
            stream.close()

        if commit:
            self.instance.save()

        return self.instance


class CustomSetPasswordForm(SetPasswordForm):
    """
    Formulario usado en Password Confirm para setear la contraseña.
    Se hereda de SetPasswordForm para cambiar el help_text en el password
    """
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput,
        strip=False,
        help_text='La contraseña debe tener al menos 8 caracteres, '
    )


class CustomPasswordChangeForm(PasswordChangeForm):
    """
    Formulario usado en Password Change para cambiar la contraseña.
    Se hereda de PasswordChangeForm para cambiar el help_text en el password
    """
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput,
        strip=False,
        help_text='La contraseña debe tener al menos 8 caracteres, '
    )
