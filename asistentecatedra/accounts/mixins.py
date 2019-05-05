import requests
from django.conf import settings
from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect


class CheckRecaptchaMixin:
    """
    Mixin that validates recaptcha v3 with the api, it adds the attribute
    recaptcha_is_valid to the view and sends a message of invalid recaptcha
    if recaptcha is not valid.
    We can use it with class based views
    """
    def get_recaptcha_response(self, data):
        recaptcha_api_response = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data=data
        )
        return recaptcha_api_response.json()

    def is_recaptcha_valid(self, request):
        recaptcha_client_response = self.request.POST.get(
            'g-recaptcha-response')

        if recaptcha_client_response:

            data = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_client_response
            }

            result = self.get_recaptcha_response(data)

            if result['success'] and result['score'] > 0.5:
                return True
            else:
                return False
        else:
            return False


class AnonymousRequiredMixin(AccessMixin):
    """Verify that the current user is not authenticated."""

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
