from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (PasswordChangeView,
                                       PasswordResetConfirmView,
                                       PasswordResetView)
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.utils.encoding import force_bytes, force_text
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views.generic import UpdateView
from django.views.generic.edit import CreateView

from .forms import ProfileForm, SignupForm
from .mixins import CheckRecaptchaMixin
from .tokens import account_token_generator

User = get_user_model()


class SignupView(CheckRecaptchaMixin, CreateView):
    form_class = SignupForm
    model = User
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        # import pdb; pdb.set_trace()
        if self.is_recaptcha_valid(self.request):

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
            login(self.request, user)
            messages.success(
                self.request,
                'Exito!, un mensaje ha sido enviado a tu correo para que '
                'verifiques tu cuenta.'
            )
            return redirect('planificaciones')
        else:
            messages.error(
                self.request,
                'reCAPTCHA no válido. Por favor intente de nuevo.'
            )
            # Regresar a la misma página
            return HttpResponseRedirect(self.request.path_info)


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
        login(request, user)
        return HttpResponse('Thank you for your email confirmation.')
    else:
        return HttpResponse('Activation link is invalid!')


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'accounts/profile.html'

    def form_valid(self, form):
        self.object = form.save()

        messages.success(
            self.request,
            'Sus datos han sido modificados con éxito.'
        )
        url = reverse('profile', kwargs={
            'pk': self.object.pk,
            'slug': self.object.slug
        })
        return redirect(url)


class CustomPasswordResetView(PasswordResetView):
    """
    Vista para reset de password que hereda de PasswordResetView para cambiar
    los métodos http aceptados a solo 'post'
    """
    http_method_names = ['post']
    success_url = reverse_lazy('login')
    email_template_name = 'accounts/password_reset_email.html',
    subject_template_name = 'accounts/password_reset_subject.txt'

    def form_valid(self, form):
        email = form.cleaned_data['email']
        users = list(form.get_users(email))
        if users:
            messages.success(
                self.request,
                'Un mensaje ha sido enviado a tu correo para que '
                'reestablezcas tu contraseña.'
            )
        else:
            messages.error(
                self.request,
                'La cuenta de correo que has escrito es incorrecta, verifica '
                'tus datos.'
            )
        return super().form_valid(form)


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    """
    Vista usada para ir al formulario para cambiar contraseña desde el email.
    Luego de ingresar la nueva contraseña se enviará al usuario a la página
    principal de planificaciones ya autenticado.
    """
    success_url = reverse_lazy('planificaciones')
    post_reset_login = True
    template_name = 'accounts/password_reset_confirm.html'

    def form_valid(self, form):
        """Method to add a success message"""
        messages.success(
            self.request,
            'Tu contraseña ha sido cambiada exitosamente.'
        )
        return super().form_valid(form)
