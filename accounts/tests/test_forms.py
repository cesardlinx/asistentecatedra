import pytest
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.test import TestCase
from mixer.backend.django import mixer
from accounts.forms import PhotoForm, SignupForm

from .conftest import create_test_image, clean_test_files

User = get_user_model()


class TestSignupForm(TestCase):
    """Tests for the signup form"""
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
        """Test when post data is valid"""
        form = SignupForm(self.data)
        assert form.is_valid() is True, \
            'The form should be valid with valid data'

    # Test Validations
    def test_invalid_password_confirm(self):
        """Test when the password confirm field is invalid"""
        data = self.data
        data['password2'] = 'p4ssword_2'
        form = SignupForm(data)
        assert form.is_valid() is False, \
            'The form should be invalid with invalid second password'

    def test_invalid_email(self):
        """Test when data has an invalid email"""
        data = self.data
        data['email'] = 'EMAIL'
        form = SignupForm(data)
        assert form.is_valid() is False, \
            'The form should be invalid with invalid email'

    def test_empty_data(self):
        """Test when data is empty"""
        form = SignupForm({})
        assert form.is_valid() is False, \
            'The form should be invalid with empty data'

    def test_alpha_validator(self):
        """
        Tests the alphanumeric validator for fields when there is an error
        """
        form = SignupForm({'first_name': '123'})
        field_errors = form.errors.get('first_name')
        assert "Este campo solo permite letras" \
            in field_errors

    def test_alpha_validator_no_error(self):
        """
        Tests the alphanumeric validator for fields when there is no error
        """
        form = SignupForm({'first_name': 'David'})
        assert "Este campo solo permite letras" \
            not in form.errors


class TestPhotoForm(TestCase):
    """Tests for the photo uploading form"""
    def setUp(self):
        # Image creation
        self.img = create_test_image('test.jpg', (500, 600))
        self.data = {
            'x': 0,
            'y': 0,
            'width': 50,
            'height': 60
        }
        self.file_data = {'photo': self.img}

    @pytest.mark.django_db
    def test_image_upload_success(self):
        """Test when post data is valid"""
        user = mixer.blend(User, email='tester@tester.com')
        instance = get_object_or_404(User, pk=user.pk)

        form = PhotoForm(self.data, self.file_data, instance=instance)
        assert form.is_valid() is True, \
            'The form should be valid with valid data'

        instance = form.save()

        assert instance.photo.width == 180, 'Image width should be modified'
        assert instance.photo.height == 180, 'Image height should be modified'
        assert instance.email == 'tester@tester.com'

    def test_data_empty(self):
        """Test when data is empty"""
        form = PhotoForm({}, self.file_data)
        assert form.is_valid() is False, \
            'The form should not be empty'

    def test_image_wrong_extension(self):
        """Test when the image has a wrong extension"""
        img = create_test_image('test.ico', (200, 300),
                                content_type='image/x-icon')
        file_data = {'photo': img}
        form = PhotoForm(self.data, file_data)
        assert form.is_valid() is False, \
            'The form should not be valid if the photo has wrong extension'

    def test_x_field_cant_be_negative(self):
        """Tests that x field can't be negative"""
        data = {
            'x': -1,
            'y': 0,
            'width': 50,
            'height': 50
        }
        form = PhotoForm(data, self.file_data)
        assert form.is_valid() is False, \
            'the x field should not be negative'

    def test_y_field_cant_be_negative(self):
        """Tests that y field can't be negative"""
        data = {
            'x': 0,
            'y': -1,
            'width': 50,
            'height': 50
        }
        form = PhotoForm(data, self.file_data)
        assert form.is_valid() is False, \
            'the y field should not be negative'

    def test_width_cant_be_negative(self):
        """Tests that width field can't be negative"""
        data = {
            'x': 0,
            'y': 0,
            'width': -50,
            'height': 50
        }
        form = PhotoForm(data, self.file_data)
        assert form.is_valid() is False, \
            'the width field should not be negative'

    def test_height_cant_be_negative(self):
        """Tests that height field can't be negative"""
        data = {
            'x': 0,
            'y': 0,
            'width': 50,
            'height': -50
        }
        form = PhotoForm(data, self.file_data)
        assert form.is_valid() is False, \
            'the height field should not be negative'

    def test_x_not_bigger_than_image_width(self):
        """Tests that x can't be bigger than width"""
        data = {
            'x': 700,
            'y': 0,
            'width': 50,
            'height': 50
        }
        form = PhotoForm(data, self.file_data)
        assert form.is_valid() is False, \
            'the x field should not be bigger than width'

    def test_y_not_bigger_than_image_height(self):
        """Tests that y can't be bigger than height"""
        data = {
            'x': 0,
            'y': 700,
            'width': 50,
            'height': 50
        }
        form = PhotoForm(data, self.file_data)
        assert form.is_valid() is False, \
            'the y field should not be bigger than height'

    def test_width_not_bigger_than_image_width(self):
        """Tests that width can't be bigger than image width"""
        data = {
            'x': 0,
            'y': 0,
            'width': 700,
            'height': 50
        }
        form = PhotoForm(data, self.file_data)
        assert form.is_valid() is False, \
            'the width field should not be bigger than image width'

    def test_height_not_bigger_than_image_height(self):
        """Tests that height can't be bigger than image height"""
        data = {
            'x': 0,
            'y': 0,
            'width': 50,
            'height': 700
        }
        form = PhotoForm(data, self.file_data)
        assert form.is_valid() is False, \
            'the height field should not be bigger than image height'

    def tearDown(self):
        clean_test_files()
