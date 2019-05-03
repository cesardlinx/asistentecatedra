# import pytest
from django.test import TestCase
from accounts.forms import SignupForm


class TestSignupForm(TestCase):
    def setUp(self):
        self.data = {
            'first_name': 'David',
            'last_name': 'David',
            'email': 'tester@tester.com',
            'password1': 'P455w0rd_testing',
            'password2': 'P455w0rd_testing',
            'institution': 'Colegio Benalcázar',
            'terms': True
        }

    def test_valid_data(self):
        form = SignupForm(self.data)
        assert form.is_valid() is True, \
            'The form should be valid with valid data'

    # Test Validations
    def test_invalid_password_confirm(self):
        data = self.data
        data['password2'] = 'p4ssword_2'
        form = SignupForm(data)
        assert form.is_valid() is False, \
            'The form should be invalid with invalid second password'

    def test_invalid_email(self):
        data = self.data
        data['email'] = 'EMAIL'
        form = SignupForm(data)
        assert form.is_valid() is False, \
            'The form should be invalid with invalid email'

    def test_empty_data(self):
        form = SignupForm({})
        assert form.is_valid() is False, \
            'The form should be invalid with empty data'

    def test_alpha_validator(self):
        form = SignupForm({'first_name': '123'})
        field_errors = form.errors.get('first_name')
        assert "Este campo solo permite letras" \
            in field_errors

    def test_alpha_validator_no_error(self):
        form = SignupForm({'first_name': 'David'})
        assert "Este campo solo permite letras" \
            not in form.errors
