import smtplib
from unittest.mock import patch

import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.core import mail
from django.core.mail import BadHeaderError
from django.test import RequestFactory, TestCase
from django.urls import reverse
from mixer.backend.django import mixer
from stripe import error

from accounts.models import Subscription
from asistente import views
from asistente.tests.conftest import add_middleware_to_request

pytestmark = pytest.mark.django_db

User = get_user_model()


class TestCheckoutView(TestCase):
    def setUp(self):
        self.user = mixer.blend(User)
        self.request = RequestFactory().get('/')
        self.plan = mixer.blend('accounts.Plan', plan_type='ANUAL')

        self.mock_stripe = patch(
            'asistente.views.stripe.Subscription')
        self.stripe_subscription = self.mock_stripe.start()
        self.stripe_subscription.create.return_value = {'id': '123456'}

        self.url = reverse('checkout',
                           kwargs={
                               'plan_id': self.plan.pk,
                               'plan_slug': self.plan.slug
                            })

    def test_anonymous(self):
        """Tests that an anonymous user can't access the view"""
        self.request.user = AnonymousUser()
        response = views.CheckoutView.as_view()(self.request,
                                                plan_id=self.plan.pk,
                                                plan_slug=self.plan.slug)
        assert 'login' in response.url, 'Should not be callable by anonymous'

    def test_get(self):
        """Tests that the view can be callable by a user"""
        self.request.user = self.user
        response = views.CheckoutView.as_view()(self.request,
                                                plan_id=self.plan.pk,
                                                plan_slug=self.plan.slug)
        assert response.status_code == 200, \
            'Should be callable by the authenticated user'

    @patch('accounts.models.stripe', autospec=True)
    def test_success_subscription(self, mock_stripe):
        """Test when all data are valid for checkout"""
        mock_stripe.Customer.create.return_value = {'id': '12345'}

        user = User.objects.create_user(
            email='tester@tester.com',
            password='P455w0rd_testing',
            first_name='Juan',
            last_name='Pérez',
        )

        superuser = User.objects.create_superuser(
            username='david@webmaster.com',
            email='david@webmaster.com',
            password='P455w0rd_testing'
        )

        self.client.login(
            email=user.email,
            password='P455w0rd_testing'
        )

        assert user.is_premium is False, 'User should not be premium'

        response = self.client.post(self.url, {
            'stripeToken': 'some-token',
        }, follow=True)

        user.refresh_from_db()

        assert response.status_code == 200, 'Should be callable'
        assert user.is_premium is True, 'User should be premium'
        subscription = Subscription.objects.get(plan__plan_type='ANUAL')
        assert subscription.user == user, \
            'The user should be related with the subscription'
        assert subscription.stripe_subscription_id == '123456', \
            'The subscription should have an id'
        assert subscription.active is True, \
            'The subscription should be active'
        assert self.stripe_subscription.create.called is True, \
            'Stripe create subscription function called'
        user.refresh_from_db()
        assert user.active_plan == self.plan, \
            'The user now is subscripted to the plan'

        messages = list(response.context.get('messages'))
        assert len(messages) == 1, 'There should be a message'
        assert 'Su transacción ha sido realizada con éxito' \
            == messages[0].message
        assert 'alert-success' == messages[0].tags, \
            'There should be a success message'
        assert len(mail.outbox) == 2, 'Should send 2 mails'

        user_email = mail.outbox[0]
        admin_email = mail.outbox[1]

        assert user.first_name in user_email.body, \
            "Email body should contain user's first name"
        assert 'cancelada' not in user_email.body, \
            'Should not be a cancellation email'
        assert "Asistente de Cátedra | SUBSCRIPCIÓN" \
            in user_email.subject
        assert subscription.plan.plan_type in user_email.body, \
            "Plan type should be in email body"
        assert user.email in user_email.to, \
            "The user's email should be in email's field TO "

        assert user.email in admin_email.body, \
            "Email body should contain user's first name"
        assert 'cancelado' not in admin_email.body, \
            'Should not be a cancellation email'
        assert "Asistente de Cátedra | SUBSCRIPCIÓN AÑADIDA" \
            in admin_email.subject
        assert subscription.plan.plan_type in admin_email.body, \
            "Plan type should be in email body"
        assert superuser.email in admin_email.to, \
            "The admin email should be in email's field TO "

    @patch('accounts.models.stripe', autospec=True)
    @patch('asistente.views.stripe.Charge.create', autospec=True)
    def test_perpetual_subscription(self, mock_charge, mock_stripe):
        """Tests when a user decides to subscribe to the perpetual plan"""
        mock_stripe.Customer.create.return_value = {'id': '12345'}
        mock_charge.return_value = {'id': '1234567'}

        user = User.objects.create_user(
            email='tester@tester.com',
            password='P455w0rd_testing',
            first_name='Juan',
            last_name='Pérez',
        )

        superuser = User.objects.create_superuser(
            username='david@webmaster.com',
            email='david@webmaster.com',
            password='P455w0rd_testing'
        )

        self.client.login(
            email=user.email,
            password='P455w0rd_testing'
        )

        plan = mixer.blend('accounts.Plan', plan_type='PAGO ÚNICO')

        url = reverse('checkout',
                      kwargs={'plan_id': plan.pk, 'plan_slug': plan.slug})

        assert user.is_premium is False, 'User should not be premium'

        response = self.client.post(url, {
            'stripeToken': 'some-token',
        }, follow=True)

        user.refresh_from_db()

        assert response.status_code == 200, 'Should be callable'
        assert user.is_premium is True, 'User should be premium'
        subscription = Subscription.objects.get(plan__plan_type='PAGO ÚNICO')
        assert subscription.user == user, \
            'The user should be related with the subscription'
        assert subscription.stripe_charge_id == '1234567', \
            'The subscription should have an id'
        assert subscription.active is True, \
            'The subscription should be active'
        assert mock_charge.called is True, \
            'Stripe create charge function called'
        assert user.active_plan == plan, \
            'The user now is subscripted to the plan'

        messages = list(response.context.get('messages'))
        assert len(messages) == 1, 'There should be a message'
        assert 'Su transacción ha sido realizada con éxito' \
            == messages[0].message
        assert 'alert-success' == messages[0].tags, \
            'There should be a success message'
        assert len(mail.outbox) == 2, 'Should send 2 mails'

        user_email = mail.outbox[0]
        admin_email = mail.outbox[1]

        assert user.first_name in user_email.body, \
            "Email body should contain user's first name"
        assert 'cancelada' not in user_email.body, \
            'Should not be a cancellation email'
        assert "Asistente de Cátedra | SUBSCRIPCIÓN" \
            in user_email.subject
        assert subscription.plan.plan_type in user_email.body, \
            "Plan type should be in email body"
        assert user.email in user_email.to, \
            "The user's email should be in email's field TO "

        assert user.email in admin_email.body, \
            "Email body should contain user's first name"
        assert 'cancelado' not in admin_email.body, \
            'Should not be a cancellation email'
        assert "Asistente de Cátedra | SUBSCRIPCIÓN AÑADIDA" \
            in admin_email.subject
        assert subscription.plan.plan_type in admin_email.body, \
            "Plan type should be in email body"
        assert superuser.email in admin_email.to, \
            "The admin email should be in email's field TO "

    def test_invalid_card(self):
        """Test when an invalid card is entered (stripe CardError)"""
        mixer.blend('accounts.Plan')  # Free Plan

        self.stripe_subscription.create.side_effect = \
            error.CardError('Error', 2, 2)

        request = RequestFactory().post('/', {
            'stripeToken': 'some-token',
        })

        request.user = self.user
        request = add_middleware_to_request(request)
        response = views.CheckoutView.as_view()(request,
                                                plan_id=self.plan.pk,
                                                plan_slug=self.plan.slug)

        self.user.refresh_from_db()

        assert self.user.is_premium is False, 'User should not be premium'

        assert 'Error. La tarjeta de crédito ingresada no es válida.' in \
            str(response.content.decode("utf-8")
                ), 'A message should be displayed'

        assert 'alert-danger' in str(response.content), \
            'It should display an error message'

    @patch('asistente.views.delete_subscription_from_stripe', autospec=True)
    def test_change_subscription(self, mock_stripe_delete):
        """Tests an authenticated user can change his subscription"""

        monthly_plan = mixer.blend('accounts.Plan', plan_type='MENSUAL')

        previous_subscription = mixer.blend(
            'accounts.Subscription',
            plan=monthly_plan,
            user=self.user,
            stripe_subscription_id='456789',
            active=True
        )

        self.user.is_premium = True
        self.user.save()

        request = RequestFactory().post('/', {
            'stripeToken': 'some-token',
        })

        request.user = self.user
        request = add_middleware_to_request(request)
        assert self.user.is_premium is True, 'User should be premium'
        response = views.CheckoutView.as_view()(request,
                                                plan_id=self.plan.pk,
                                                plan_slug=self.plan.slug)
        self.user.refresh_from_db()

        assert response.status_code == 302, \
            'Response should send a redirection'
        assert self.user.is_premium is True, 'User should still being premium'
        assert self.user.subscriptions.filter(active=True).count() == 1
        active_subscription = self.user.subscriptions.get(active=True)
        assert active_subscription != previous_subscription
        assert self.user.active_plan == self.plan
        mock_stripe_delete.assert_called_once_with(
            previous_subscription.stripe_subscription_id)

    def test_change_subscription_when_no_previous_plan(self):
        """
        Tests a subscription change when there is no previous active plan
        """
        request = RequestFactory().post('/', {
            'stripeToken': 'some-token',
        })

        request.user = self.user
        request = add_middleware_to_request(request)
        assert self.user.is_premium is False, 'User should not be premium'
        response = views.CheckoutView.as_view()(request,
                                                plan_id=self.plan.pk,
                                                plan_slug=self.plan.slug)
        self.user.refresh_from_db()

        assert response.status_code == 302, \
            'Response should return an ok status'
        assert self.user.is_premium is True, 'User should be premium'
        assert self.user.subscriptions.filter(active=True).count() == 1
        assert self.user.active_plan == self.plan

    def test_invalid_request_error(self):
        """Test when Invalid parameters were supplied to Stripe's API"""
        self.stripe_subscription.create.side_effect = \
            error.InvalidRequestError('error', 2)

        self.make_error_tests(
            'Error!. Parámetros inválidos.')

    def test_api_connection_error(self):
        """Test when Network communication with Stripe failed"""
        self.stripe_subscription.create.side_effect = \
            error.APIConnectionError('error')

        self.make_error_tests(
            'Ha ocurrido un error de comunicación. Verifique su conexión.')

    def test_stripe_error(self):
        """Test when a generic stripe error occurs"""
        self.stripe_subscription.create.side_effect = \
            error.StripeError('error')

        self.make_error_tests(
            'Ha ocurrido un error en el pago.')

    def test_generic_error(self):
        """Tests when a not handled exception  is raised"""

        self.stripe_subscription.create.side_effect = Exception('error')

        self.make_error_tests(
            'Ha ocurrido un error con la peticion realizada.')

    def make_error_tests(self, error_message):
        mixer.blend('accounts.Plan')  # Free Plan

        request = RequestFactory().post('/', {
            'stripeToken': 'some-token',
        })

        request.user = self.user
        request = add_middleware_to_request(request)
        response = views.CheckoutView.as_view()(request,
                                                plan_id=self.plan.pk,
                                                plan_slug=self.plan.slug)
        self.user.refresh_from_db()

        assert self.user.is_premium is False, 'User should not be premium'

        assert error_message\
            in str(response.content.decode("utf-8")
                   ), 'A message should be displayed'

        assert 'alert-danger' in str(response.content), \
            'It should display an error message'

    @patch('asistente.views.send_subscription_emails', autospec=True)
    @patch('accounts.models.stripe', autospec=True)
    def test_smtp_error(self, mock_stripe, mock_emails):
        """Tests when a smtp error is raised when sending the emails"""

        mock_stripe.Customer.create.return_value = {'id': '12345'}
        mock_emails.side_effect = smtplib.SMTPException()

        user = User.objects.create_user(
            email='tester@tester.com',
            password='P455w0rd_testing',
            first_name='Juan',
            last_name='Pérez',
        )

        self.make_email_error_tests(
            'Ha ocurrido un error al tratar de enviar el correo.',
            user,
            mock_emails
        )

    @patch('asistente.views.send_subscription_emails', autospec=True)
    @patch('accounts.models.stripe', autospec=True)
    def test_badheader_error(self, mock_stripe, mock_emails):
        """Tests when a badheader error is raised when sending the emails"""

        mock_stripe.Customer.create.return_value = {'id': '12345'}
        mock_emails.side_effect = BadHeaderError()

        user = User.objects.create_user(
            email='tester@tester.com',
            password='P455w0rd_testing',
            first_name='Juan',
            last_name='Pérez',
        )

        self.make_email_error_tests(
            'Ha ocurrido un error al tratar de enviar el correo.',
            user,
            mock_emails
        )

    def make_email_error_tests(self, error_message, user, mock_emails):

        self.client.login(
            email=user.email,
            password='P455w0rd_testing'
        )

        response = self.client.post(self.url, {
            'stripeToken': 'some-token',
        }, follow=True)
        user.refresh_from_db()

        assert response.status_code == 200, 'Should be callable'
        assert user.is_premium is True, 'User should be premium'
        # Should redirect to the user's profile
        self.assertRedirects(response, user.get_absolute_url())
        messages = list(response.context.get('messages'))
        assert len(messages) == 2, \
            'There should be two messages'
        assert error_message == messages[0].message
        assert 'alert-danger' == messages[0].tags, \
            'There should be an error message'
        assert mock_emails.called is True, \
            'Should call the function to send the emails'
