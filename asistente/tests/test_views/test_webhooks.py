from unittest.mock import MagicMock, patch
from django.contrib.auth import get_user_model
from django.core import mail
from django.test import RequestFactory, TestCase
from mixer.backend.django import mixer
from testfixtures import LogCapture

from asistente.views import stripe_webhooks_view

User = get_user_model()


class TestWebhooksView(TestCase):
    @patch('accounts.models.stripe.Customer.create', autospec=True)
    def setUp(self, customer_create):
        event_webhooks = patch(
            'asistente.views.stripe.Webhook.construct_event')

        self.event = event_webhooks.start()

        self.logger = LogCapture()

        self.user = mixer.blend(
            User,
            email='tester@tester.com',
            password='P455w0rd_testing',
            first_name='Juan',
            last_name='Perez',
            stripe_customer_id='customer_id'
        )

        self.superuser = mixer.blend(
            User,
            username='david@webmaster.com',
            email='david@webmaster.com',
            password='P455w0rd_testing',
            is_superuser=True,
            is_staff=True,
        )

        self.request = RequestFactory()\
            .post('/',
                  data={'data': 'test'},
                  content_type='application/json',
                  HTTP_STRIPE_SIGNATURE='test_value')

    def test_subscription_created_event(self):
        # event mock
        event = MagicMock()
        event.type = 'customer.subscription.created'
        event.data.object.plan.nickname = 'MENSUAL'
        event.data.object.customer = 'customer_id'
        self.event.return_value = event

        response = stripe_webhooks_view(self.request)

        assert 'INFO' in str(self.logger), 'Should return an info log'
        assert event.type in str(self.logger), \
            'Should return a log with the plan type info'

        assert response.status_code == 200, \
            'Should return an status code of 200 to stripe'

        # Email sending
        assert len(mail.outbox) == 2, 'Should send 2 mails'

        user_email = mail.outbox[0]
        admin_email = mail.outbox[1]

        assert self.user.first_name in user_email.body, \
            "Email body should contain user's first name"
        assert 'cancelada' not in user_email.body, \
            'Should not be a cancellation email'
        assert "Asistente de Cátedra | SUBSCRIPCIÓN" \
            in user_email.subject
        assert 'Mensual' in user_email.body, \
            "Plan type should be in email body"
        assert self.user.email in user_email.to, \
            "The user's email should be in email's field TO "

        assert self.user.email in admin_email.body, \
            "Email body should contain user's first name"
        assert 'cancelado' not in admin_email.body, \
            'Should not be a cancellation email'
        assert "Asistente de Cátedra | SUBSCRIPCIÓN AÑADIDA" \
            in admin_email.subject
        assert 'Mensual' in admin_email.body, \
            "Plan type should be in email body"
        assert self.superuser.email in admin_email.to, \
            "The admin email should be in email's field TO "

    def test_invoice_payment_succeeded_event(self):
        # event mock
        event = MagicMock()
        event.type = 'invoice.payment_succeeded'
        event.data.object.lines.data[0].plan.nickname = 'MENSUAL'
        event.data.object.amount_paid = 499
        event.data.object.customer = 'customer_id'
        self.event.return_value = event

        request = RequestFactory().post('/',
                                        data={'data': 'test'},
                                        content_type='application/json',
                                        HTTP_STRIPE_SIGNATURE='test_value')
        response = stripe_webhooks_view(request)

        assert 'INFO' in str(self.logger), 'Should return an info log'
        assert event.type in str(self.logger), \
            'Should return a log with the plan type info'

        assert response.status_code == 200, \
            'Should return an status code of 200 to stripe'

        self.user.refresh_from_db()
        assert self.user.is_premium is True, 'User should be premium'

        # Email sending
        assert len(mail.outbox) == 1, 'Should send 1 email'

        user_email = mail.outbox[0]

        assert self.user.first_name in user_email.body, \
            "Email body should contain user's first name"
        assert "Asistente de Cátedra | PAGO DE SUBSCRIPCIÓN" \
            in user_email.subject
        assert 'Mensual' in user_email.body, \
            "Plan type should be in email body"
        assert self.user.email in user_email.to, \
            "The user's email should be in email's field TO "
        assert '4,99' in user_email.body, 'The amount should be in email'


    def test_invoice_payment_failed_event(self):
        # event mock
        event = MagicMock()
        event.type = 'invoice.payment_failed'
        event.data.object.lines.data[0].plan.nickname = 'MENSUAL'
        event.data.object.amount_paid = 499
        event.data.object.customer = 'customer_id'
        self.event.return_value = event

        self.user.is_premium = True
        self.user.save()

        request = RequestFactory().post('/',
                                        data={'data': 'test'},
                                        content_type='application/json',
                                        HTTP_STRIPE_SIGNATURE='test_value')
        response = stripe_webhooks_view(request)

        assert 'INFO' in str(self.logger), 'Should return an info log'
        assert event.type in str(self.logger), \
            'Should return a log with the plan type info'

        assert response.status_code == 200, \
            'Should return an status code of 200 to stripe'

        self.user.refresh_from_db()
        assert self.user.is_premium is False, 'User should not be premium'

        # Email sending
        assert len(mail.outbox) == 1, 'Should send 1 email'

        user_email = mail.outbox[0]

        assert self.user.first_name in user_email.body, \
            "Email body should contain user's first name"
        assert "Asistente de Cátedra | PAGO DE SUBSCRIPCIÓN FALLIDO" \
            in user_email.subject
        assert 'Mensual' in user_email.body, \
            "Plan type should be in email body"
        assert self.user.email in user_email.to, \
            "The user's email should be in email's field TO "

    def test_subscription_deleted_event(self):
        # event mock
        event = MagicMock()
        event.type = 'customer.subscription.deleted'
        event.data.object.plan.nickname = 'MENSUAL'
        event.data.object.customer = 'customer_id'
        self.event.return_value = event

        response = stripe_webhooks_view(self.request)

        assert 'INFO' in str(self.logger), 'Should return an info log'
        assert event.type in str(self.logger), \
            'Should return a log with the plan type info'

        assert response.status_code == 200, \
            'Should return an status code of 200 to stripe'

        # Email sending
        assert len(mail.outbox) == 2, 'Should send 2 mails'

        user_email = mail.outbox[0]
        admin_email = mail.outbox[1]

        assert self.user.first_name in user_email.body, \
            "Email body should contain user's first name"
        assert 'cancelada' in user_email.body, \
            'Should be a cancellation email'
        assert "Asistente de Cátedra | CANCELACIÓN DE SUBSCRIPCIÓN" \
            in user_email.subject
        assert 'Mensual' in user_email.body, \
            "Previous Plan type should be in email body"
        assert self.user.email in user_email.to, \
            "The user's email should be in email's field TO "

        assert self.user.email in admin_email.body, \
            "Email body should contain user's first name"
        assert 'cancelado' in admin_email.body, \
            'Should be a cancellation email'
        assert "Asistente de Cátedra | SUBSCRIPCIÓN CANCELADA" \
            in admin_email.subject
        assert 'Mensual' in admin_email.body, \
            "Plan type should be in email body"
        assert self.superuser.email in admin_email.to, \
            "The admin email should be in email's field TO "

    def test_charge_succeeded_event(self):
        # event mock
        event = MagicMock()
        event.type = 'charge.succeeded'
        event.data.object.description = 'PAGO ÚNICO'
        event.data.object.customer = 'customer_id'
        event.data.object.amount = 11976
        self.event.return_value = event

        response = stripe_webhooks_view(self.request)

        assert 'INFO' in str(self.logger), 'Should return an info log'
        assert event.type in str(self.logger), \
            'Should return a log with the plan type info'

        assert response.status_code == 200, \
            'Should return an status code of 200 to stripe'

        self.user.refresh_from_db()
        assert self.user.is_premium is True, 'User should be premium'

        # Email sending
        assert len(mail.outbox) == 3, 'Should send 3 emails'

        user_email = mail.outbox[0]
        admin_email = mail.outbox[1]
        invoice_email = mail.outbox[2]

        assert self.user.first_name in user_email.body, \
            "Email body should contain user's first name"
        assert "Asistente de Cátedra | SUBSCRIPCIÓN" \
            in user_email.subject
        assert 'Pago Único' in user_email.body, \
            "Previous Plan type should be in email body"
        assert self.user.email in user_email.to, \
            "The user's email should be in email's field TO "

        assert self.user.email in admin_email.body, \
            "Email body should contain user's first name"
        assert "Asistente de Cátedra | SUBSCRIPCIÓN AÑADIDA" \
            in admin_email.subject
        assert 'Pago Único' in admin_email.body, \
            "Plan type should be in email body"
        assert self.superuser.email in admin_email.to, \
            "The admin email should be in email's field TO "

        assert self.user.first_name in invoice_email.body, \
            "Email body should contain user's first name"
        assert "Asistente de Cátedra | PAGO DE SUBSCRIPCIÓN" \
            in invoice_email.subject
        assert 'Pago Único' in invoice_email.body, \
            "Plan type should be in email body"
        assert self.user.email in invoice_email.to, \
            "The user's email should be in email's field TO "
        assert '119,76' in invoice_email.body, 'The amount should be in email'

    def test_charge_failed_event(self):
        # event mock
        event = MagicMock()
        event.type = 'charge.failed'
        event.data.object.description = 'PAGO ÚNICO'
        event.data.object.customer = 'customer_id'
        event.data.object.amount = 11976
        self.event.return_value = event

        response = stripe_webhooks_view(self.request)

        assert 'INFO' in str(self.logger), 'Should return an info log'
        assert event.type in str(self.logger), \
            'Should return a log with the plan type info'

        assert response.status_code == 200, \
            'Should return an status code of 200 to stripe'

        self.user.refresh_from_db()
        assert self.user.is_premium is False, 'User should not be premium'

        # Email sending
        assert len(mail.outbox) == 1, 'Should send 1 email'

        user_email = mail.outbox[0]

        assert self.user.first_name in user_email.body, \
            "Email body should contain user's first name"
        assert "Asistente de Cátedra | PAGO DE SUBSCRIPCIÓN FALLIDO" \
            in user_email.subject
        assert 'Pago Único' in user_email.body, \
            "Plan type should be in email body"
        assert self.user.email in user_email.to, \
            "The user's email should be in email's field TO "

    def tearDown(self):
        # stopping log capture
        self.logger.uninstall()
