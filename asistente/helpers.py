import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


def delete_subscription_from_stripe(subscription_id):
    subscription = stripe.Subscription.retrieve(subscription_id)
    subscription.delete()
