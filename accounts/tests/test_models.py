import os
import pytest
from django.contrib.auth import get_user_model
from django.test import TestCase
from mixer.backend.django import mixer
from accounts.models import Plan, Subscription
from .conftest import create_test_image, clean_test_files
from django.conf import settings
from unittest.mock import patch

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
    def setUp(self):
        self.user = mixer.blend(User)
        self.img = create_test_image('test_logo.jpg', (500, 600))

    def test_model(self):
        user = mixer.blend(User, first_name='David', last_name='Padilla')
        assert user.is_premium is False, \
            'Normal user should not be premium by default'
        assert isinstance(user, User), 'Should be an instance of User'
        slug = 'david-padilla'
        assert user.get_absolute_url() == '/accounts/profile/{0}/{1}/'\
                                          .format(user.pk, slug)

    @patch('accounts.models.stripe')
    def test_superuser(self, mock_stripe):
        """Tests Superuser creation"""
        mock_stripe.Customer.create.return_value = {'id': '12345'}

        user = User.objects.create_superuser(
            email='tester@tester.com',
            password='P455w0rd'
        )
        assert user.is_superuser is True, 'User should be superuser'
        assert user.is_staff is True, 'Superuser should be staff'
        assert user.is_premium is True, 'Superuser should be premium'

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

    def test_superuser_invalid_premium(self):
        """
        Tests error exception when trying to create superuser with the
        is_premium attribute equals to false
        """
        with pytest.raises(ValueError,
                           match="Superuser must have is_premium=True."):
            User.objects.create_superuser(
                email='tester@tester.com',
                password='P455w0rd',
                is_premium=False,
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

    def test_active_subscription_property(self):
        """Tests the property to get the user's active_subscription"""
        plan = mixer.blend('accounts.Plan', plan_type='MONTHLY')
        user = mixer.blend(User)

        subscription = Subscription.objects.create(
            user=user,
            plan=plan,
            active=True
        )

        assert user.active_subscription == subscription, \
            "The user's active plan should be the free plan"

    def test_active_subscription_property_when_no_active_subscription(self):
        """
        Tests the property to get the user's active_subscription
        when there is no active subscription
        """
        user = mixer.blend(User)

        assert user.active_subscription is False, \
            "Should return False if there is no active subscription"

    def test_active_plan_property(self):
        """Tests the property to get the user's active_plan"""
        plan = mixer.blend('accounts.Plan')

        # automatically relates the free plan with the user
        user = mixer.blend(User)

        assert user.active_plan == plan, \
            "The user's active plan should be the free plan"

    def test_active_plan_property_when_no_active_subscription(self):
        """
        Tests the property to get the user's active_plan
        when there is no active subscription
        """
        user = mixer.blend(User)

        assert user.active_plan is False, \
            "Should return False if there is no active plan"

    def tearDown(self):
        """Method to make the image removal when necesary"""
        clean_test_files()


@patch('accounts.models.stripe')
def test_user_post_save_signal(mock_stripe):

    mock_stripe.Customer.create.return_value = {'id': '12345'}

    free_plan = Plan.objects.create(
        plan_type='FREE',
        price=0.00,
        stripe_plan_id=settings.STRIPE_FREE_ID
    )
    free_plan = Plan.objects.get(plan_type='FREE')
    user = User.objects.create_user(
        email='tester2@tester.com',
        password='P455w0rd'
    )
    assert user.subscriptions.get(active=True).plan == free_plan
    assert user.stripe_customer_id == '12345'


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
