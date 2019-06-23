import pytest
from unittest.mock import patch, MagicMock
from accounts.models import Plan, Subscription
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory, TestCase
from django.urls import reverse
from mixer.backend.django import mixer
from stripe import error
from testfixtures import LogCapture

from asistente import views

pytestmark = pytest.mark.django_db

User = get_user_model()


class TestCancelSubscriptionView(TestCase):

    def setUp(self):
        customer_create_patch = patch('accounts.models.stripe.Customer.create')
        customer_modify_patch = patch('accounts.models.stripe.Customer.modify')
        subscription_create_patch = patch(
            'accounts.models.stripe.Subscription.create')
        subscription_retrieve_patch = patch(
            'accounts.models.stripe.Subscription.retrieve')
        self.customer_create = customer_create_patch.start()
        self.customer_modify = customer_modify_patch.start()
        self.subscription_create = subscription_create_patch.start()
        self.subscription_retrieve = subscription_retrieve_patch.start()

        self.customer_create.return_value = {'id': '12345'}

        self.subscription_mock = MagicMock(id='123456')
        self.subscription_mock.delete = MagicMock()
        self.subscription_retrieve.return_value = self.subscription_mock
        self.subscription_create.return_value = self.subscription_mock

        self.logger = LogCapture()

        self.user = User.objects.create_user(
            email='tester@tester.com',
            password='P455w0rd_testing',
            first_name='Juan',
            last_name='Perez'
        )

        self.free_plan = Plan.objects.get(plan_type='GRATIS')

        self.superuser = User.objects.create_superuser(
            username='david@webmaster.com',
            email='david@webmaster.com',
            password='P455w0rd_testing'
        )

        self.client.login(
            username=self.user.email,
            password='P455w0rd_testing'
        )

        self.url = reverse('cancel_subscription')

    def test_anonymous(self):
        """Tests the anonymous user can't call the view"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = views.cancel_subscription_view(request)

        assert response.status_code == 302, 'Should redirect to login'
        assert 'login' in response.url, \
            'An anonymous user should not access'

    def test_cant_access_through_get(self):
        """Tests the view can't be accessed by a get request"""
        request = RequestFactory().get('/')
        request.user = self.user
        response = views.cancel_subscription_view(request)

        assert response.status_code == 302, 'Should return a redirect'
        assert 'profile' in response.url, \
            'Should redirect to profile'

    def test_cancel_subscription_success(self):
        """
        Tests when a user can successfuly cancel his/her subscription and go
        back to the free plan
        """

        monthly_plan = mixer.blend('accounts.Plan', plan_type='MENSUAL')

        Subscription.objects.create_subscription(
            self.user,
            monthly_plan,
            '456789',
        )
        self.user.is_premium = True
        self.user.save()

        assert self.user.is_premium is True, 'User should be premium'

        response = self.client.post(self.url, {}, follow=True)

        self.user.refresh_from_db()

        assert 'INFO' in str(self.logger), 'Should return an success log'
        assert 'User subscription successfully cancelled' in str(self.logger),\
            'Should return a success log message'

        assert response.status_code == 200, 'Should be callable'
        assert self.user.is_premium is False, \
            'User should no longer be premium'
        # Should redirect to the user's profile
        self.assertRedirects(response, self.user.get_absolute_url())
        assert self.user.active_plan == self.free_plan, \
            "User's active plan should return to free plan"
        messages = list(response.context.get('messages'))
        assert len(messages) == 1, 'There should be a message'
        assert 'Su subscripción ha sido cancelada con éxito' \
            == messages[0].message
        assert 'alert-success' == messages[0].tags, \
            'There should be a success message'
        # Should delete from stripe
        self.subscription_mock.delete.assert_called_once_with()

    @patch('accounts.models.Subscription.created_date')
    @patch('accounts.models.Subscription.next_billing_date')
    def test_invalid_request_error(self,
                                   subscription_billing,
                                   subscription_date):
        """
        Test the raise of an  InvalidRequestError when a subscription
        cancellation is in progress
        """
        # Se parchea estos dos métodos de Subscription porque al final
        # retorna el template que correponde al perfil, el mismo que usa estos
        # dos métodos, el mismo que usa el método subscription_retrieve que
        # para este test también es un mock
        subscription_date.return_value = '05/05/2019'
        subscription_billing.return_value = '05/05/2019'

        self.subscription_retrieve.side_effect = error.\
            InvalidRequestError('error', 2)

        self.make_error_tests(
            'Error!. Parámetros inválidos.', 1, self.subscription_retrieve,
            'InvalidRequestError')
        assert self.user.is_premium is True, 'User should still be premium'

    @patch('accounts.models.Subscription.created_date')
    @patch('accounts.models.Subscription.next_billing_date')
    def test_api_connection_error(self,
                                  subscription_billing,
                                  subscription_date):
        """
        Test the raise of an  APIConnectionError when a subscription
        cancellation is in progress
        """
        subscription_date.return_value = '05/05/2019'
        subscription_billing.return_value = '05/05/2019'

        self.subscription_retrieve.side_effect = error.\
            APIConnectionError('error')

        self.make_error_tests(
            'Ha ocurrido un error de comunicaciones. Verifique su conexión.',
            1, self.subscription_retrieve, 'APIConnectionError')
        assert self.user.is_premium is True, 'User should still be premium'

    @patch('accounts.models.Subscription.created_date')
    @patch('accounts.models.Subscription.next_billing_date')
    def test_stripe_error(self,
                          subscription_billing,
                          subscription_date):
        """
        Test the raise of an StripeError when a subscription
        cancellation is in progress
        """
        subscription_date.return_value = '05/05/2019'
        subscription_billing.return_value = '05/05/2019'

        self.subscription_retrieve.side_effect = error.StripeError('error')

        self.make_error_tests(
            'Ha ocurrido un error al tratar de cancelar la subscripción.',
            1, self.subscription_retrieve, 'StripeError')
        assert self.user.is_premium is True, 'User should still be premium'

    @patch('accounts.models.Subscription.created_date')
    @patch('accounts.models.Subscription.next_billing_date')
    def test_generic_error(self,
                           subscription_billing,
                           subscription_date):
        """
        Test the raise of a generic Exception when a subscription
        cancellation is in progress
        """
        subscription_date.return_value = '05/05/2019'
        subscription_billing.return_value = '05/05/2019'

        self.subscription_retrieve.side_effect = Exception('error')

        self.make_error_tests(
            'Ha ocurrido un error con la peticion realizada.', 1,
            self.subscription_retrieve, 'Exception')

    def make_error_tests(self, error_message, number_of_messages,
                         subscription_retrieve, exception_message):
        """Auxiliary method for making error tests"""
        monthly_plan = mixer.blend('accounts.Plan', plan_type='MENSUAL')

        self.user.is_premium = True
        self.user.save()

        previous_subscription = Subscription.objects.create_subscription(
            self.user,
            monthly_plan,
            '456789',
        )

        response = self.client.post(self.url, {}, follow=True)
        self.user.refresh_from_db()

        assert 'ERROR' in str(self.logger), 'Should return an error log'
        assert exception_message in str(self.logger), \
            'Should return a Exception log'

        assert response.status_code == 200, 'Should be callable'
        # Should redirect to the user's profile
        self.assertRedirects(response, self.user.get_absolute_url())
        messages = list(response.context.get('messages'))
        assert len(messages) == number_of_messages, \
            'There should be a message'
        assert error_message == messages[0].message
        assert 'alert-danger' == messages[0].tags, \
            'There should be a error message'
        # Should attempt to delete from stripe
        subscription_retrieve.assert_called_once_with(
            previous_subscription.stripe_subscription_id)

    def tearDown(self):
        # stopping log capture
        self.logger.uninstall()
