from django.contrib.auth import get_user_model
import stripe
from django.conf import settings
from django.core import mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

stripe.api_key = settings.STRIPE_SECRET_KEY
User = get_user_model()


def delete_subscription_from_stripe(subscription_id):
    """Deletes subscriptions from stripe"""
    subscription = stripe.Subscription.retrieve(subscription_id)
    subscription.delete()


def send_subscription_emails(user_mail_subject, admin_mail_subject,
                             user, plan, cancel=False):
    """
    Send subscription email to user and to admins
    if cancel=True then there is a cancel subscription email
    """
    connection = mail.get_connection()   # Use default email connection

    # User email sending

    user_email_html = render_to_string(
        'asistente/subscription_email.html',
        {
            'user': user,
            'plan': plan,
            'cancel': cancel
        }
    )
    user_email_body = strip_tags(user_email_html)
    user_email = EmailMultiAlternatives(
        user_mail_subject, user_email_body, to=[user.email]
    )

    # Admins email sending
    admins = User.objects.filter(is_superuser=True, is_staff=True)
    admins_emails = [admin.email for admin in admins]

    admin_email_html = render_to_string(
        'asistente/subscription_admin_email.html',
        {
            'user': user,
            'plan': plan,
            'cancel': cancel
        }
    )
    admin_email_body = strip_tags(admin_email_html)
    admin_email = EmailMultiAlternatives(
        admin_mail_subject, admin_email_body, to=admins_emails
    )

    connection.send_messages([user_email, admin_email])
