import smtplib
from unittest.mock import MagicMock, patch
from django.contrib.auth import get_user_model
from django.core import mail
from django.core.mail import BadHeaderError
from django.test import RequestFactory, TestCase
from mixer.backend.django import mixer
from testfixtures import LogCapture
from stripe.error import SignatureVerificationError, StripeError
from asistente.views import stripe_webhooks_view

User = get_user_model()


class TestWebhooksViewsErrors(TestCase):
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

    def test_construct_event_value_error(self):
        """Test when there is a ValueError when constucting the event"""
        self.event.side_effect = ValueError('Error')
        self.make_error_tests('ValueError')

    def test_construct_event_signature_error(self):
        """
        Test when there is a SignatureVerificationError
        when constucting the event
        """
        self.event.side_effect = SignatureVerificationError(
            'Error', 'HTTP_STRIPE_SIGNATURE')
        self.make_error_tests('SignatureVerificationError')

    @patch('asistente.views.send_subscription_emails')
    def test_subscription_created_badheader_error(self, subscription_emails):
        """
        Test when there is a BadHeaderError while sending emails after
        getting a subscription created event
        """
        # event mock
        event = MagicMock()
        event.type = 'customer.subscription.created'
        event.data.object.plan.nickname = 'MENSUAL'
        event.data.object.customer = 'customer_id'
        self.event.return_value = event

        subscription_emails.side_effect = BadHeaderError('Error')

        self.make_email_error_tests('BadHeaderError')

    @patch('asistente.views.send_subscription_emails')
    def test_subscription_created_smtp_error(self, subscription_emails):
        """
        Test when there is a SMTPException while sending emails after
        getting a subscription created event
        """
        # event mock
        event = MagicMock()
        event.type = 'customer.subscription.created'
        event.data.object.plan.nickname = 'MENSUAL'
        event.data.object.customer = 'customer_id'
        self.event.return_value = event

        subscription_emails.side_effect = smtplib.SMTPException('Error')

        self.make_email_error_tests('SMTPException')

    @patch('asistente.views.send_invoice_email')
    def test_invoice_payment_succeeded_badheader_error(self, invoice_emails):
        """
        Test when there is a BadHeaderError while sending emails after
        getting an invoice payment succeeded event
        """
        # event mock
        event = MagicMock()
        event.type = 'invoice.payment_succeeded'
        event.data.object.lines.data[0].plan.nickname = 'MENSUAL'
        event.data.object.amount_paid = 499
        event.data.object.charge = 'ch-123456'
        event.data.object.customer = 'customer_id'
        self.event.return_value = event

        invoice_emails.side_effect = BadHeaderError('Error')

        self.make_email_error_tests('BadHeaderError')

        self.user.refresh_from_db()
        assert self.user.is_premium is True, 'User should be premium'
        assert self.user.active_subscription.stripe_charge_id == 'ch-123456', \
            'Active subscriptions should have the last charge id'

    @patch('asistente.views.send_invoice_email')
    def test_invoice_payment_succeeded_smtp_error(self, invoice_emails):
        """
        Test when there is a SMTPException while sending emails after
        getting an invoice payment succeeded event
        """
        # event mock
        event = MagicMock()
        event.type = 'invoice.payment_succeeded'
        event.data.object.lines.data[0].plan.nickname = 'MENSUAL'
        event.data.object.amount_paid = 499
        event.data.object.charge = 'ch-123456'
        event.data.object.customer = 'customer_id'
        self.event.return_value = event

        invoice_emails.side_effect = smtplib.SMTPException('Error')

        self.make_email_error_tests('SMTPException')

        self.user.refresh_from_db()
        assert self.user.is_premium is True, 'User should be premium'
        assert self.user.active_subscription.stripe_charge_id == 'ch-123456', \
            'Active subscriptions should have the last charge id'

    @patch('accounts.models.stripe.Refund.create')
    @patch('accounts.models.stripe.Subscription.retrieve')
    @patch('asistente.views.send_invoice_email')
    def test_invoice_payment_failed_badheader_error(self, invoice_emails,
                                                    subscription_retrieve,
                                                    refund_create):
        """
        Test when there is a BadHeaderError while sending emails after
        getting an invoice payment failed event
        """
        subscription_mock = MagicMock(
            id='123456', current_period_start=1564617600,
            current_period_end=1567296000)
        subscription_mock.delete = MagicMock()
        subscription_retrieve.return_value = subscription_mock

        # event mock
        event = MagicMock()
        event.type = 'invoice.payment_failed'
        event.data.object.lines.data[0].plan.nickname = 'MENSUAL'
        event.data.object.amount_paid = 499
        event.data.object.customer = 'customer_id'
        self.event.return_value = event

        invoice_emails.side_effect = BadHeaderError('Error')

        self.user.is_premium = True
        self.user.save()

        self.make_email_error_tests('BadHeaderError')

        self.user.refresh_from_db()
        assert self.user.is_premium is False, 'User should not be premium'

    @patch('accounts.models.stripe.Refund.create')
    @patch('accounts.models.stripe.Subscription.retrieve')
    @patch('asistente.views.send_invoice_email')
    def test_invoice_payment_failed_smtp_error(self, invoice_emails,
                                               subscription_retrieve,
                                               refund_create):
        """
        Test when there is a SMTPException while sending emails after
        getting an invoice payment failed event
        """
        subscription_mock = MagicMock(
            id='123456', current_period_start=1564617600,
            current_period_end=1567296000)
        subscription_mock.delete = MagicMock()
        subscription_retrieve.return_value = subscription_mock

        # event mock
        event = MagicMock()
        event.type = 'invoice.payment_failed'
        event.data.object.lines.data[0].plan.nickname = 'MENSUAL'
        event.data.object.amount_paid = 499
        event.data.object.customer = 'customer_id'
        self.event.return_value = event

        invoice_emails.side_effect = smtplib.SMTPException('Error')

        self.user.is_premium = True
        self.user.save()

        self.make_email_error_tests('SMTPException')

        self.user.refresh_from_db()
        assert self.user.is_premium is False, 'User should not be premium'

    @patch('asistente.views.transaction.atomic')
    def test_invoice_payment_failed_stripe_error(self, cancel_subscription):
        """
        Test when there is a StripeError while cancelling subscription after
        getting an invoice payment failed event
        """
        # event mock
        event = MagicMock()
        event.type = 'invoice.payment_failed'
        event.data.object.lines.data[0].plan.nickname = 'MENSUAL'
        event.data.object.amount_paid = 499
        event.data.object.customer = 'customer_id'
        self.event.return_value = event

        cancel_subscription.side_effect = StripeError('Error')

        self.make_error_tests('StripeError')

    @patch('asistente.views.transaction.atomic')
    def test_invoice_payment_failed_generic_error(self, cancel_subscription):
        """
        Test when there is a generic Exception while cancelling subscription
        after getting an invoice payment failed event
        """
        # event mock
        event = MagicMock()
        event.type = 'invoice.payment_failed'
        event.data.object.lines.data[0].plan.nickname = 'MENSUAL'
        event.data.object.amount_paid = 499
        event.data.object.customer = 'customer_id'
        self.event.return_value = event

        cancel_subscription.side_effect = Exception('Error')

        self.make_error_tests('Exception')

    @patch('asistente.views.send_subscription_emails')
    def test_subscription_deleted_badheader_error(self, subscription_emails):
        """
        Test when there is a BadHeaderError while sending emails after
        getting a subscription deleted event
        """
        # event mock
        event = MagicMock()
        event.type = 'customer.subscription.deleted'
        event.data.object.plan.nickname = 'MENSUAL'
        event.data.object.customer = 'customer_id'
        self.event.return_value = event

        subscription_emails.side_effect = BadHeaderError('Error')

        self.make_email_error_tests('BadHeaderError')

    @patch('asistente.views.send_subscription_emails')
    def test_subscription_deleted_smtp_error(self, subscription_emails):
        """
        Test when there is a SMTPException while sending emails after
        getting a subscription deleted event
        """
        # event mock
        event = MagicMock()
        event.type = 'customer.subscription.deleted'
        event.data.object.plan.nickname = 'MENSUAL'
        event.data.object.customer = 'customer_id'
        self.event.return_value = event

        subscription_emails.side_effect = smtplib.SMTPException('Error')

        self.make_email_error_tests('SMTPException')

    @patch('asistente.views.send_subscription_emails')
    def test_charge_succeeded_badheader_error(self, subscription_emails):
        """
        Test when there is a BadHeaderError while sending emails after
        getting a charge succeeded event
        """
        # event mock
        event = MagicMock()
        event.type = 'charge.succeeded'
        event.data.object.description = 'PAGO ÚNICO'
        event.data.object.customer = 'customer_id'
        self.event.return_value = event

        subscription_emails.side_effect = BadHeaderError('Error')

        self.make_email_error_tests('BadHeaderError')

    @patch('asistente.views.send_subscription_emails')
    def test_charge_succeeded_smtp_error(self, subscription_emails):
        """
        Test when there is a SMTPException while sending emails after
        getting a charge succeeded event
        """
        # event mock
        event = MagicMock()
        event.type = 'charge.succeeded'
        event.data.object.description = 'PAGO ÚNICO'
        event.data.object.customer = 'customer_id'
        self.event.return_value = event

        subscription_emails.side_effect = smtplib.SMTPException('Error')

        self.make_email_error_tests('SMTPException')

    @patch('asistente.views.send_invoice_email')
    def test_charge_failed_badheader_error(self, subscription_emails):
        """
        Test when there is a BadHeaderError while sending emails after
        getting a charge failed event
        """
        # event mock
        event = MagicMock()
        event.type = 'charge.failed'
        event.data.object.description = 'PAGO ÚNICO'
        event.data.object.customer = 'customer_id'
        event.data.object.amount = 11976
        self.event.return_value = event

        subscription_emails.side_effect = BadHeaderError('Error')

        self.make_email_error_tests('BadHeaderError')

    @patch('asistente.views.send_invoice_email')
    def test_charge_failed_smtp_error(self, subscription_emails):
        """
        Test when there is a SMTPException while sending emails after
        getting a charge failed event
        """
        # event mock
        event = MagicMock()
        event.type = 'charge.failed'
        event.data.object.description = 'PAGO ÚNICO'
        event.data.object.customer = 'customer_id'
        event.data.object.amount = 11976
        self.event.return_value = event

        subscription_emails.side_effect = smtplib.SMTPException('Error')

        self.make_email_error_tests('SMTPException')

    @patch('asistente.views.send_refund_email')
    def test_charge_refunded_badheader_error(self, subscription_emails):
        """
        Test when there is a BadHeaderError while sending emails after
        getting a charge refunded event
        """
        # event mock
        event = MagicMock()
        event.type = 'charge.refunded'
        event.data.object.customer = 'customer_id'
        event.data.object.amount = 5972
        event.data.object.source.brand = 'Visa'
        event.data.object.source.last4 = 2024
        self.event.return_value = event

        subscription_emails.side_effect = BadHeaderError('Error')

        self.make_email_error_tests('BadHeaderError')

    @patch('asistente.views.send_refund_email')
    def test_charge_refunded_smtp_error(self, subscription_emails):
        """
        Test when there is a SMTPException while sending emails after
        getting a charge refunded event
        """
        # event mock
        event = MagicMock()
        event.type = 'charge.refunded'
        event.data.object.customer = 'customer_id'
        event.data.object.amount = 5972
        event.data.object.source.brand = 'Visa'
        event.data.object.source.last4 = 2024
        self.event.return_value = event

        subscription_emails.side_effect = smtplib.SMTPException('Error')

        self.make_email_error_tests('SMTPException')

    def make_email_error_tests(self, error_type):
        """Auxiliary method for making email related error tests"""

        self.make_error_tests(error_type)
        # Email sending
        assert len(mail.outbox) == 0, 'Should send no email'

    def make_error_tests(self, error_type):
        """Auxiliary method for making error tests"""
        response = stripe_webhooks_view(self.request)

        assert response.status_code == 400, \
            'Should return a 400 status code to stripe'

        # Logs
        assert 'ERROR' in str(self.logger), 'Should return an ERROR log'
        assert error_type in str(self.logger), \
            'Should return a log with the error type info'

    def tearDown(self):
        # stopping log capture
        self.logger.uninstall()
