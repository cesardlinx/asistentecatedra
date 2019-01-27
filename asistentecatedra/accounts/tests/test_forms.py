# import pytest
import os
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from accounts.forms import SignupForm
from PIL import Image


class TestSignupForm(TestCase):
    def setUp(self):
        self.data = {
            'username': 'tester',
            'password1': 'p455w0rd',
            'password2': 'p455w0rd',
            'email': 'tester@tester.com',
            'first_name': 'David',
            'last_name': 'Padilla',
            'institution': 'Colegio Benalcázar',
        }
        img = Image.new('RGB', (60, 30), color=(73, 109, 137))
        img.save('media/test_image.png')

        img = open('media/test_image.png', 'rb')
        img_content = img.read()

        image = SimpleUploadedFile(
            name='test_image.png',
            content=img_content,
            content_type='image/jpeg'
        )
        img.close()

        self.file_data = {'institution_logo': image}

    def tearDown(self):
        os.remove('media/test_image.png')

    def test_valid_data(self):
        form = SignupForm(self.data, self.file_data)
        assert form.is_valid() is True, \
            'The form should be valid with valid data'

    def test_invalid_second_password(self):
        data = self.data
        data['password2'] = 'p4ssword_2'
        form = SignupForm(data, self.file_data)
        assert form.is_valid() is False, \
            'The form should be invalid with invalid second password'

    def test_invalid_email(self):
        data = self.data
        data['email'] = 'EMAIL'
        form = SignupForm(data, self.file_data)
        assert form.is_valid() is False, \
            'The form should be invalid with invalid email'

    def test_empty_data(self):
        form = SignupForm({})
        assert form.is_valid() is False, \
            'The form should be invalid with empty data'

    def test_number_validator(self):
        form = SignupForm({'password1': 'asd', 'password2': 'asd'})
        field_errors = form.errors.get('password2')
        assert "La contraseña debe tener la menos 1 dígito, 0-9." \
            in field_errors

    def test_uppercase_validator(self):
        form = SignupForm({'password1': 'asd', 'password2': 'asd'})
        field_errors = form.errors.get('password2')
        assert "La contraseña debe tener la menos 1 letra mayúscula, A-Z." \
            in field_errors

    def test_lowercase_validator(self):
        form = SignupForm({'password1': 'ASD', 'password2': 'ASD'})
        field_errors = form.errors.get('password2')
        assert "La contraseña debe tener la menos 1 letra minúscula, a-z." \
            in field_errors
