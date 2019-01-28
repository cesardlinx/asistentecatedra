from django.contrib.auth import get_user_model
from django.contrib.auth.views import auth_login
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.edit import CreateView

from .forms import SignupForm

User = get_user_model()


class SignupView(CreateView):
    form_class = SignupForm
    model = User
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
            user = form.save()
            user.save()

            # Authentication and Login
            auth_login(self.request, user)
            return redirect('planificaciones')


def unique_email_validator(request):
    response_str = "false"
    if request.is_ajax():
        email = request.POST.get("email")
        if email:
            try:
                get_object_or_404(User, email=email)
            except Http404:
                response_str = "true"  # User doesn't exists
            else:
                response_str = "false"  # User already exists

    return HttpResponse("%s" % response_str)
