import requests
from django.conf import settings
from django.contrib.auth.mixins import AccessMixin, UserPassesTestMixin
from django.contrib.auth.views import redirect_to_login
from django.shortcuts import redirect

from accounts.models import Plan


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


class NotPremiumUserRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        try:
            return not self.request.user.is_premium
        except AttributeError:
            return True

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            return redirect('home')
        return redirect_to_login(
            self.request.get_full_path(),
            self.get_login_url(),
            self.get_redirect_field_name()
        )


class PremiumUserRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        try:
            return self.request.user.is_premium
        except AttributeError:
            return True

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            return redirect('home')
        return redirect_to_login(
            self.request.get_full_path(),
            self.get_login_url(),
            self.get_redirect_field_name()
        )


class NotPerpetualNotPremiumUserRequiredMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            # get if user is perpetual
            try:
                plan = Plan.objects.get(plan_type='PAGO ÚNICO')
                user_is_perpetual = self.request.user.is_premium and \
                    self.request.user.active_plan == plan
            except Plan.DoesNotExist:
                user_is_perpetual = False
            except Exception:
                user_is_perpetual = False

            if user_is_perpetual:
                # If user is perpetual
                return redirect('home')
            elif not self.request.user.is_premium:
                # If user is no premium
                return redirect('premium')
            else:
                # Give access
                return super().dispatch(request, *args, **kwargs)
        else:
            # Redirect to login
            return redirect_to_login(
                self.request.get_full_path(),
                self.get_login_url(),
                self.get_redirect_field_name()
            )


class NotPerpetualPremiumUserRequiredMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            # get if user is perpetual
            try:
                plan = Plan.objects.get(plan_type='PAGO ÚNICO')
                user_is_perpetual = self.request.user.is_premium and \
                    self.request.user.active_plan == plan
            except Plan.DoesNotExist:
                user_is_perpetual = False
            except Exception:
                user_is_perpetual = False

            if user_is_perpetual:
                # If user is perpetual
                return redirect('home')
            else:
                # Give access
                return super().dispatch(request, *args, **kwargs)
        else:
            # Redirect to login
            return redirect_to_login(
                self.request.get_full_path(),
                self.get_login_url(),
                self.get_redirect_field_name()
            )


