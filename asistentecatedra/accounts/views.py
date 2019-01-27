from django.contrib.auth import get_user_model
from django.contrib.auth.views import auth_login
from django.db import transaction
from django.shortcuts import redirect
from django.views.generic.edit import CreateView

from .forms import SignupForm
User = get_user_model()


class SignupView(CreateView):
    form_class = SignupForm
    model = User
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        with transaction.atomic():
            user = form.save()
            user.refresh_from_db()
            user.profile.institution = form.cleaned_data.get('institution')
            # user.profile.institution_logo = form.cleaned_data.get(
            #     'institution_logo')
            user.save()

            # Authentication and Login
            auth_login(self.request, user)
            return redirect('planificaciones')

