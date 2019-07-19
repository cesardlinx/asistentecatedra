from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import redirect_to_login
from django.shortcuts import redirect


class UserIsPremiumMixin(UserPassesTestMixin):
    def test_func(self):
        # Checks whether the user is premium or not
        if self.request.user.is_authenticated:
            return self.request.user.is_premium
        else:
            return False

    def handle_no_permission(self):
        if self.raise_exception or self.request.user.is_authenticated:
            return redirect('planificaciones')
        return redirect_to_login(self.request.get_full_path(),
                                 self.get_login_url(),
                                 self.get_redirect_field_name())
