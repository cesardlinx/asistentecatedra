import os

import pytest
from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase
from mixer.backend.django import mixer

from .conftest import clean_test_files, create_test_image

pytestmark = pytest.mark.django_db

User = get_user_model()


class TestUser(TestCase):
    """Tests del modelo de usuario"""
    def setUp(self):
        self.user = mixer.blend(User)
        self.img = create_test_image('test_logo.jpg', (500, 600))

    def test_model(self):
        user = mixer.blend(User, first_name='David', last_name='Padilla')
        assert isinstance(user, User), 'Should be an instance of User'
        slug = 'david-padilla'
        assert user.full_name == '{} {}'.format(
            user.first_name,
            user.last_name), "It should return the user's full name"
        assert user.get_absolute_url() == '/accounts/profile/{0}/{1}/'\
                                          .format(user.pk, slug)
        assert user.username == user.email, 'The username should be the email'

    def test_superuser(self):
        """Tests Superuser creation"""
        user = User.objects.create_superuser(
            email='tester@tester.com',
            password='P455w0rd'
        )
        assert user.is_superuser is True, 'User should be superuser'
        assert user.is_staff is True, 'Superuser should be staff'

    def test_superuser_invalid_staff(self):
        """
        Tests error exception when trying to create superuser with the is_staff
        attribute equals to false
        """
        with pytest.raises(ValueError,
                           match="Superuser must have is_staff=True."):
            User.objects.create_superuser(
                email='tester@tester.com',
                password='P455w0rd',
                is_staff=False,
            )

    def test_superuser_invalid_superuser(self):
        """
        Tests error exception when trying to create superuser with the
        is_superuser attribute equals to false
        """
        with pytest.raises(ValueError,
                           match="Superuser must have is_superuser=True."):
            User.objects.create_superuser(
                email='tester@tester.com',
                password='P455w0rd',
                is_superuser=False,
            )

    def test_create_user_without_email(self):
        """
        Tests error exception raising when trying to create user without email
        """
        with pytest.raises(ValueError, match="The given email must be set"):
            User.objects.create_user(
                email='',
                password='P455w0rd'
            )

    def test_institution_logo_uploading(self):
        """Test institution logo manipulation before saving"""
        self.user.institution_logo = self.img
        self.user.save()
        assert self.user.institution_logo.width == 125, \
            'width should be changed'
        assert self.user.institution_logo.height == 150, \
            'height should be changed'

    def test_no_duplicated_institution_logo_uploading(self):
        """Tests there is no duplicated images when uploading a new logo"""
        img_2 = create_test_image('test_logo_1.jpg', (500, 600))

        self.user.institution_logo = self.img
        self.user.save()

        self.user.institution_logo = img_2
        self.user.save()

        logo_path = '{0}/users/user_{1}/logo/'\
            .format(settings.MEDIA_ROOT, self.user.pk)
        assert len(os.listdir(logo_path)) == 1, 'There should be only one file'

    def test_no_duplicated_photo_uploading(self):
        """Tests there is no duplicated images when uploading a new logo"""
        img_2 = create_test_image('test_photo_1.jpg', (500, 600))

        self.user.photo = self.img
        self.user.save()

        self.user.photo = img_2
        self.user.save()

        photo_path = '{0}/users/user_{1}/photo/'\
            .format(settings.MEDIA_ROOT, self.user.pk)
        assert len(os.listdir(photo_path)) == 1, \
            'There should be only one file'

    def test_get_logo_property(self):
        """Tests the get_logo user property"""
        assert self.user.get_logo == \
            '/static/img/defaults/default-school-logo.png', \
            'Should be equal to the default image without a logo'
        self.user.institution_logo = self.img
        self.user.save()
        assert '/assets/users/user_{}/logo/'.format(self.user.pk) in \
            self.user.get_logo, 'Should be equal to the new logo'

    def test_get_photo_property(self):
        """Tests the get_photo user property"""
        assert self.user.get_photo == \
            '/static/img/defaults/user.png', \
            'Should be equal to the default image without a photo'
        self.user.photo = self.img
        self.user.save()
        assert '/assets/users/user_{}/photo/'.format(self.user.pk) in \
            self.user.get_photo, 'Should be equal to the new photo'

    def test_soft_delete(self):
        """Test user soft delete feature"""
        assert self.user.is_active is True, \
            'User should be active before soft deletion'
        self.user.soft_delete()
        assert self.user.is_active is False, \
            'User should no logner be active after soft deletion'

    def tearDown(self):
        """Method to make the image removal when necesary"""
        clean_test_files()
