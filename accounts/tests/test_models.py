import os
from unittest.mock import patch, MagicMock
import pytest
from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from mixer.backend.django import mixer

from accounts.models import Plan, Subscription

from .conftest import clean_test_files, create_test_image

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

    def test_get_absoulte_url(self):
        plan = mixer.blend('accounts.Plan')
        assert plan.get_absolute_url() is None
        plan = mixer.blend('accounts.Plan', plan_type='MENSUAL')
        assert plan.get_absolute_url() == \
            reverse('checkout',
                    kwargs={'plan_id': plan.pk, 'plan_slug': plan.slug}), \
            'Should return an url to checkout'

    def test_slug_creation(self):
        plan = mixer.blend('accounts.Plan', plan_type='PAGO ÚNICO')
        assert plan.slug == 'pago-unico', \
            'The slug should be formed by the plan type'


class TestUser(TestCase):
    """Tests del modelo de usuario"""
    def setUp(self):
        self.user = mixer.blend(User)
        self.free_plan = Plan.objects.get(plan_type='GRATIS')
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
        plan = mixer.blend('accounts.Plan', plan_type='MENSUAL')

        subscription = Subscription.objects.create_subscription(
            user=self.user,
            plan=plan,
        )

        self.user.refresh_from_db()

        assert self.user.active_subscription == subscription, \
            "The user's active plan should be the free plan"

    def test_active_subscription_property_when_no_active_subscription(self):
        """
        Tests the property to get the user's active_subscription
        when there is no active subscription
        """
        assert self.user.active_subscription.plan == self.free_plan, \
            "The user should be subscripted to free plan"

    def test_active_plan_property(self):
        """Tests the property to get the user's active_plan"""

        assert self.user.active_plan == self.free_plan, \
            "The user's active plan should be the free plan"

    @patch('accounts.models.stripe.Customer.modify')
    @patch('accounts.models.stripe.Subscription.create')
    @patch('accounts.models.stripe.Subscription.retrieve')
    def test_cancel_active_subscription(self,
                                        subscription_retrieve,
                                        subscription_create,
                                        customer_modify):
        subscription_mock = MagicMock(id='123456')
        subscription_mock.delete = MagicMock()
        subscription_retrieve.return_value = subscription_mock
        subscription_create.return_value = subscription_mock

        user = mixer.blend(User)

        monthly_plan = mixer.blend('accounts.Plan', plan_type='MENSUAL')
        yearly_plan = mixer.blend('accounts.Plan', plan_type='ANUAL')

        monthly_sub = Subscription.objects.create_subscription(
            user,
            monthly_plan,
            '123456'
        )

        yearly_sub = Subscription.objects.create_subscription(
            user,
            yearly_plan,
            '123456'
        )

        user.cancel_active_subscription()

        yearly_sub.refresh_from_db()
        monthly_sub.refresh_from_db()
        user_subscription = user.active_subscription

        assert user_subscription.plan == self.free_plan, \
            'Now the active plan should be the free one'
        assert yearly_sub.active is False, \
            'Other subscriptions should not be active'
        assert monthly_sub.active is False, \
            'Other subscriptions should not be active'
        assert subscription_mock.delete.call_count == 2, \
            'Should delete previous subscription from stripe'

    def tearDown(self):
        """Method to make the image removal when necesary"""
        clean_test_files()


@patch('accounts.models.stripe')
def test_user_post_save_signal(mock_stripe):

    mock_stripe.Customer.create.return_value = {'id': '12345'}

    user = User.objects.create_user(
        email='tester2@tester.com',
        password='P455w0rd'
    )
    free_plan = Plan.objects.get(plan_type='GRATIS')

    assert user.subscriptions.get(active=True).plan == free_plan
    assert user.stripe_customer_id == '12345'


class TestSubscription:
    """Tests del modelo de Subscription"""
    @patch('accounts.models.stripe.Subscription.create')
    def test_model(self, stripe_subscription):
        subscription_mock = MagicMock(id='123456')
        stripe_subscription.return_value = subscription_mock

        user = mixer.blend(User)
        plan = mixer.blend('accounts.Plan', plan_type='MENSUAL')
        subscription = Subscription(
            user=user,
            plan=plan,
        )
        subscription.save('123456')
        assert isinstance(subscription, Subscription), \
            'Should be an instance of Subscription'
        assert isinstance(subscription.user, User)
        assert str(subscription) == subscription.user.username, \
            "The string representation should be the plan's type"
        assert subscription._meta.db_table == 'subscripciones', \
            'The table should be named "subscripciones"'
        assert subscription._meta.verbose_name_plural == \
            'subscripciones', 'The plural name should be "subscripciones"'

    @patch('accounts.models.stripe.Customer.modify')
    @patch('accounts.models.stripe.Subscription.create')
    @patch('accounts.models.stripe.Subscription.retrieve')
    def test_subscription_creation(self,
                                   subscription_retrieve,
                                   subscription_create,
                                   customer_modify):

        subscription_mock = MagicMock(id='123456')
        subscription_mock.delete = MagicMock()
        subscription_create.return_value = subscription_mock
        subscription_retrieve.return_value = subscription_mock

        monthly_plan = mixer.blend('accounts.Plan', plan_type='MENSUAL')
        yearly_plan = mixer.blend('accounts.Plan', plan_type='ANUAL')
        another_user = mixer.blend(User, username='cesardlinx')
        user = mixer.blend(User)

        some_subscription = Subscription.objects.create_subscription(
            another_user,
            yearly_plan,
            '123456'
        )

        old_subscription = Subscription.objects.create_subscription(
            user,
            monthly_plan,
            '456789'
        )

        new_subscription = Subscription.objects.create_subscription(
            user,
            yearly_plan,
            '456789'
        )

        old_subscription.refresh_from_db()
        some_subscription.refresh_from_db()
        new_subscription.refresh_from_db()

        active_subscriptions = Subscription.objects.filter(user=user,
                                                           active=True)

        assert len(active_subscriptions) == 1, \
            'There should be only one active subscription for that user'
        assert new_subscription.user == user, \
            'The user should own the new subscription'
        assert new_subscription.plan == yearly_plan, \
            'The new subscription has the actual plan'
        assert new_subscription.active is True, \
            'The new subscription is the active one'
        assert old_subscription.active is False, \
            'The old subscription should not be active'
        assert some_subscription.active is True, \
            'Others subscriptions should remain intact'
        # should delete previous subscription from stripe
        subscription_mock.delete.assert_called_once_with()

    @patch('accounts.models.stripe.Charge.create')
    @patch('accounts.models.stripe.Customer.modify')
    @patch('accounts.models.stripe.Subscription.create')
    @patch('accounts.models.stripe.Subscription.retrieve')
    def test_perpetual_subscription_creation(self,
                                             subscription_retrieve,
                                             subscription_create,
                                             customer_modify,
                                             charge_create):

        mock = MagicMock(id='123456')
        mock.delete = MagicMock()
        subscription_create.return_value = mock
        subscription_retrieve.return_value = mock
        charge_create.return_value = mock

        monthly_plan = mixer.blend('accounts.Plan', plan_type='MENSUAL')
        perpetual_plan = mixer.blend('accounts.Plan', plan_type='PAGO ÚNICO')
        another_user = mixer.blend(User, username='cesardlinx')
        user = mixer.blend(User)

        some_subscription = Subscription.objects.create_subscription(
            another_user,
            monthly_plan,
            '123456'
        )

        old_subscription = Subscription.objects.create_subscription(
            user,
            monthly_plan,
            '456789'
        )

        new_subscription = Subscription.objects.create_subscription(
            user,
            perpetual_plan,
            '456789'
        )

        old_subscription.refresh_from_db()
        some_subscription.refresh_from_db()
        new_subscription.refresh_from_db()

        active_subscriptions = Subscription.objects.filter(user=user,
                                                           active=True)

        assert len(active_subscriptions) == 1, \
            'There should be only one active subscription for that user'
        assert new_subscription.user == user, \
            'The user should own the new subscription'
        assert new_subscription.plan == perpetual_plan, \
            'The new subscription has the perpetual plan'
        assert new_subscription.active is True, \
            'The new subscription is the active one'
        assert old_subscription.active is False, \
            'The old subscription should not be active'
        assert some_subscription.active is True, \
            'Others subscriptions should remain intact'

    def test_free_subscription_creation(self):

        plan = mixer.blend('accounts.Plan', plan_type='GRATIS')
        user = mixer.blend(User)

        Subscription.objects.create_subscription(
            user,
            plan,
        )

        active_subscriptions = Subscription.objects.filter(active=True)

        new_subscription = Subscription.objects.get(user=user, active=True)

        assert len(active_subscriptions) == 1, \
            'There should be only one active subscription'
        assert new_subscription.user == user, \
            'The user should own the new subscription'
        assert new_subscription.plan == plan, \
            'The new subscription has the free plan'

    @patch('accounts.models.stripe.Customer.modify')
    @patch('accounts.models.stripe.Subscription.create')
    @patch('accounts.models.stripe.Subscription.retrieve')
    def test_cancel_subscription(self,
                                 subscription_retrieve,
                                 subscription_create,
                                 customer_modify):
        subscription_mock = MagicMock(id='123456')
        subscription_mock.delete = MagicMock()
        subscription_retrieve.return_value = subscription_mock
        subscription_create.return_value = subscription_mock

        plan = mixer.blend('accounts.Plan', plan_type='MENSUAL')
        user = mixer.blend(User)

        subscription = Subscription(
            user=user,
            plan=plan,
            stripe_subscription_id='123456'
        )
        subscription.save()

        subscription.cancel_subscription()

        assert subscription.active is False, \
            'subscription should not be active'
        subscription_mock.delete.call_count == 1, \
            'Should call delete once in stripe'

    def test_created_parameter(self):
        # TODO: Compĺete tests for created parameter
        pass

    def test_next_billing_date_parameter(self):
        # TODO: Compĺete tests for next_billing_date parameter
        pass
