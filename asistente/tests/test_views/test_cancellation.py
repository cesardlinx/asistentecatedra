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

from asistente import views

pytestmark = pytest.mark.django_db

User = get_user_model()


class TestCancelSubscriptionView(TestCase):

    @patch('accounts.models.stripe', autospec=True)
    def setUp(self, mock_stripe):
        mock_stripe.Customer.create.return_value = {'id': '12345'}

        self.user = User.objects.create_user(
            email='tester@tester.com',
            password='P455w0rd_testing',
            first_name='Juan',
            last_name='Perez'
        )

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

    @patch('asistente.views.delete_subscription_from_stripe', autospec=True)
    def test_cancel_subscription_success(self, mock_delete):
        """Test when a user cancels his/her subscription successfully"""

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

        assert self.user.is_premium is True, 'User should be premium'

        free_plan = mixer.blend('accounts.Plan', plan_type='GRATIS')

        response = self.client.post(self.url, {}, follow=True)

        self.user.refresh_from_db()

        assert response.status_code == 200, 'Should be callable'
        assert self.user.is_premium is False, \
            'User should no longer be premium'
        # Should redirect to the user's profile
        self.assertRedirects(response, self.user.get_absolute_url())
        assert self.user.active_plan == free_plan, \
            "User's active plan should return to free plan"
        messages = list(response.context.get('messages'))
        assert len(messages) == 1, 'There should be a message'
        assert 'Su subscripción ha sido cancelada con éxito' \
            == messages[0].message
        assert 'alert-success' == messages[0].tags, \
            'There should be a success message'
        # Should delete from stripe
        mock_delete.assert_called_once_with(
            previous_subscription.stripe_subscription_id)

        assert len(mail.outbox) == 2, 'Should send 2 mails'

        user_email = mail.outbox[0]
        admin_email = mail.outbox[1]

        assert self.user.first_name in user_email.body, \
            "Email body should contain user's first name"
        assert 'cancelada' in user_email.body, \
            'Should be a cancellation email'
        assert "Asistente de Cátedra | CANCELACIÓN DE SUBSCRIPCIÓN" \
            in user_email.subject
        assert previous_subscription.plan.plan_type in user_email.body, \
            "Previous Plan type should be in email body"
        assert self.user.email in user_email.to, \
            "The user's email should be in email's field TO "

        assert self.user.email in admin_email.body, \
            "Email body should contain user's first name"
        assert 'cancelado' in admin_email.body, \
            'Should be a cancellation email'
        assert "Asistente de Cátedra | SUBSCRIPCIÓN CANCELADA" \
            in admin_email.subject
        assert previous_subscription.plan.plan_type in admin_email.body, \
            "Plan type should be in email body"
        assert self.superuser.email in admin_email.to, \
            "The admin email should be in email's field TO "

    @patch('asistente.views.delete_subscription_from_stripe', autospec=True)
    def test_cancel_success_when_no_active_subscription(self, mock_delete):
        """Test when for some reason a user has no active subscription"""

        free_plan = mixer.blend('accounts.Plan', plan_type='GRATIS')

        assert self.user.is_premium is False, 'User should not be premium'

        response = self.client.post(self.url, {}, follow=True)

        self.user.refresh_from_db()

        assert response.status_code == 200, 'Should be callable'
        assert self.user.is_premium is False, 'User should not be premium'
        # Should redirect to the user's profile
        self.assertRedirects(response, self.user.get_absolute_url())
        assert self.user.active_plan == free_plan, \
            "User's active plan should return the free plan"
        messages = list(response.context.get('messages'))
        assert len(messages) == 1, 'There should be a message'
        assert 'Su subscripción ha sido cancelada con éxito' \
            == messages[0].message
        assert 'alert-success' == messages[0].tags, \
            'There should be a success message'
        assert mock_delete.called is False, \
            'Should not call delete function from'

    @patch('asistente.views.delete_subscription_from_stripe', autospec=True)
    def test_cancel_success_if_no_free_plan(self, mock_delete):
        """Test when previously there is no free plan"""
        assert self.user.is_premium is False, 'User should not be premium'

        response = self.client.post(self.url, {}, follow=True)

        self.user.refresh_from_db()

        assert response.status_code == 200, 'Should be callable'
        assert self.user.is_premium is False, 'User should not be premium'
        # Should redirect to the user's profile
        self.assertRedirects(response, self.user.get_absolute_url())
        messages = list(response.context.get('messages'))
        assert len(messages) == 1, 'There should be a message'
        assert 'Su subscripción ha sido cancelada con éxito' \
            == messages[0].message
        assert 'alert-success' == messages[0].tags, \
            'There should be a success message'
        assert mock_delete.called is False, \
            'Should not call delete function from'

    @patch('asistente.views.delete_subscription_from_stripe', autospec=True)
    def test_invalid_request_error(self, mock_delete):
        """Test when Invalid parameters were supplied to Stripe's API"""
        mock_delete.side_effect = error.InvalidRequestError('error', 2)

        self.make_error_tests(
            'Error!. Parámetros inválidos.', 1, mock_delete)
        assert self.user.is_premium is True, 'User should still be premium'

    @patch('asistente.views.delete_subscription_from_stripe', autospec=True)
    def test_api_connection_error(self, mock_delete):
        """Test when Network communication with Stripe failed"""
        mock_delete.side_effect = error.APIConnectionError('error')

        self.make_error_tests(
            'Ha ocurrido un error de comunicaciones. Verifique su conexión.',
            1, mock_delete)
        assert self.user.is_premium is True, 'User should still be premium'

    @patch('asistente.views.delete_subscription_from_stripe', autospec=True)
    def test_stripe_error(self, mock_delete):
        """Test when a generic stripe error occurs"""
        mock_delete.side_effect = error.StripeError('error')

        self.make_error_tests(
            'Ha ocurrido un error al tratar de cancelar la subscripción.',
            1, mock_delete)
        assert self.user.is_premium is True, 'User should still be premium'

    @patch('asistente.views.delete_subscription_from_stripe', autospec=True)
    @patch('asistente.views.send_subscription_emails', autospec=True)
    def test_smtp_error(self, mock_emails, mock_delete):
        """Test when an smtp error occurs sending the emails"""
        mock_emails.side_effect = smtplib.SMTPException()

        self.make_error_tests(
            'Ha ocurrido un error al tratar de enviar el correo.',
            2, mock_delete)
        assert self.user.is_premium is False, 'User should not be premium'

    @patch('asistente.views.delete_subscription_from_stripe', autospec=True)
    @patch('asistente.views.send_subscription_emails', autospec=True)
    def test_badheader_error(self, mock_emails, mock_delete):
        """Test when a BadHeader error occurs sending the emails"""
        mock_emails.side_effect = BadHeaderError()

        self.make_error_tests(
            'Ha ocurrido un error al tratar de enviar el correo.',
            2, mock_delete)
        assert self.user.is_premium is False, 'User should not be premium'

    @patch('asistente.views.delete_subscription_from_stripe', autospec=True)
    @patch('asistente.views.send_subscription_emails', autospec=True)
    def test_general_error_email(self, mock_emails, mock_delete):
        """Test when a general error occurs sending the emails"""
        mock_emails.side_effect = Exception()

        self.make_error_tests(
            'Ha ocurrido un error al tratar de enviar el correo.',
            2, mock_delete)
        assert self.user.is_premium is False, 'User should not be premium'

    @patch('asistente.views.delete_subscription_from_stripe', autospec=True)
    def test_generic_error(self, mock_delete):
        """Tests when a not handled exception  is raised"""
        mock_delete.side_effect = Exception('error')

        self.make_error_tests(
            'Ha ocurrido un error con la peticion realizada.', 1, mock_delete)

    def make_error_tests(self, error_message, number_of_messages,
                         mock_delete):
        monthly_plan = mixer.blend('accounts.Plan', plan_type='MENSUAL')

        self.user.is_premium = True
        self.user.save()

        previous_subscription = mixer.blend(
            'accounts.Subscription',
            plan=monthly_plan,
            user=self.user,
            stripe_subscription_id='456789',
            active=True
        )
        mixer.blend('accounts.Subscription')

        response = self.client.post(self.url, {}, follow=True)

        self.user.refresh_from_db()

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
        mock_delete.assert_called_once_with(
            previous_subscription.stripe_subscription_id)
