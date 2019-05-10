import pytest
from django.contrib.auth import get_user_model
from django.test import TestCase
from mixer.backend.django import mixer
from accounts.models import Plan, Subscription
from .conftest import create_test_image, clean_test_files

pytestmark = pytest.mark.django_db

User = get_user_model()


class TestPlan:
    """Tests del modelo Plan"""
    def test_model(self):
        plan = mixer.blend('accounts.Plan')
        assert isinstance(plan, Plan), 'Should be an instance of Plan'
        assert str(plan) == plan.plan_type, \
            "The string representation should be the plan's type"
        assert plan._meta.db_table == 'planes', \
            'The table should be named "planes"'
        assert plan._meta.verbose_name_plural == 'planes', \
            'The plural name should be "planes"'


class TestUser(TestCase):
    """Tests del modelo de usuario"""
    def test_model(self):
        user = mixer.blend(User, first_name='David', last_name='Padilla')
        assert isinstance(user, User), 'Should be an instance of User'
        assert isinstance(user.plan, Plan), \
            'The plan field should be an instance of Plan'
        slug = 'david-padilla'
        assert user.get_absolute_url() == '/accounts/profile/{0}/{1}/'\
                                          .format(user.pk, slug)

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
        img = create_test_image('test_logo.jpg', (500, 600))
        user = mixer.blend(User)
        user.institution_logo = img
        user.save()
        assert user.institution_logo.width == 125, 'width should be changed'
        assert user.institution_logo.height == 150, 'height should be changed'

    def tearDown(self):
        """Method to make the image removal when necesary"""
        clean_test_files()


class TestSubscription:
    """Tests del modelo de Subscription"""
    def test_model(self):
        user = mixer.blend(User)
        subscription = mixer.blend('accounts.Subscription',
                                   user=user)
        assert isinstance(subscription, Subscription), \
            'Should be an instance of Subscription'
        assert isinstance(subscription.user, User)
        assert str(subscription) == subscription.user.username, \
            "The string representation should be the plan's type"
        assert subscription._meta.db_table == 'subscripciones', \
            'The table should be named "subscripciones"'
        assert subscription._meta.verbose_name_plural == 'subscripciones', \
            'The plural name should be "subscripciones"'