from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import auth_login
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views.generic.edit import CreateView

from .forms import SignupForm
from .tokens import account_token_generator

User = get_user_model()


class SignupView(CreateView):
    form_class = SignupForm
    model = User
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
            # User save
            user = form.save()
            user.save()

            # Setting username
            leading_part_of_email = user.email.split('@', 1)[0]
            derived_username = '{}_{}'.format(leading_part_of_email, user.pk)
            user.username = derived_username
            user.save()

            # Email sending
            domain = get_current_site(self.request).domain
            protocol = settings.PROTOCOL
            mail_subject = 'Asistente de Cátedra | '\
                           'Confirmar Correo Electrónico'
            self.uid = urlsafe_base64_encode(force_bytes(user.pk)).decode()
            self.token = account_token_generator.make_token(user)
            html_email_body = render_to_string('accounts/confirm_email.html', {
                'user': user,
                'protocol': protocol,
                'domain': domain,
                'uid': self.uid,
                'token': self.token,
            })
            text_email_body = strip_tags(html_email_body)
            to_email = form.cleaned_data.get('email')

            email = EmailMultiAlternatives(
                mail_subject, text_email_body, to=[to_email])
            email.attach_alternative(html_email_body, "text/html")
            email.send()

            # Authentication and Login
            auth_login(self.request, user)
            return redirect('planificaciones')

    def get_context_data(self, **kwargs):
        """Sends uid and token in context for testing"""
        context = super().get_context_data(**kwargs)
        try:
            context['uid'] = self.uid
            context['token'] = self.token
        except AttributeError:
            pass
        return context


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


def confirm_email(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_token_generator.check_token(user, token):
        user.email_confirmed = True
        user.save()
        auth_login(request, user)
        return HttpResponse('Thank you for your email confirmation.')
    else:
        return HttpResponse('Activation link is invalid!')
