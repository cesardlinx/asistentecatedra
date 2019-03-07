
from django.contrib import messages
from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (LoginView, PasswordChangeView,
                                       PasswordResetConfirmView,
                                       PasswordResetView)
from django.contrib.sites.shortcuts import get_current_site

from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from .helpers import send_confirmation_helper
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView
from django.views.generic.edit import CreateView

from .forms import (CustomPasswordChangeForm, CustomSetPasswordForm,
                    ProfileForm, SignupForm)
from .mixins import AnonymousRequiredMixin, CheckRecaptchaMixin
from .tokens import account_token_generator

User = get_user_model()


class SignupView(AnonymousRequiredMixin, CheckRecaptchaMixin, CreateView):
    """Vista para registro de usuarios"""
    form_class = SignupForm
    model = User
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
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
            send_confirmation_helper(user, domain)

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


@login_required
def send_confirmation_view(request):
    """
    Vista para enviar correo de confirmacion de email desde un
    usuario logeado
    """
    if not request.user.email_confirmed:
        domain = get_current_site(request).domain
        send_confirmation_helper(request.user, domain)
        previous_url = request.META.get('HTTP_REFERER')
        messages.success(
            request,
            'Un mensaje ha sido enviado a tu correo para que '
            'verifiques tu cuenta.'
        )
    else:
        messages.info(request, 'Su cuenta ya está verificada')
    return redirect(previous_url)


class CustomLoginView(AnonymousRequiredMixin, LoginView):
    """Vista para autenticación de usuarios"""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'reset_form': PasswordResetForm(),
        })
        return context


def unique_email_validator(request):
    """Validador remoto para verificar unicidad de correo"""
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


def exists_email_validator(request):
    """Validador remoto para verificar si existe un correo"""
    response_str = "false"
    if request.is_ajax():
        email = request.POST.get("email")
        if email:
            try:
                get_object_or_404(User, email=email)
            except Http404:
                response_str = "false"  # User doesn't exists
            else:
                response_str = "true"  # User already exists

    return HttpResponse("%s" % response_str)


def confirm_email(request, uidb64, token):
    """
    Vista llamada el momento de seguir el link provisto en el correo
    electrónico para confirmar el email
    """
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_token_generator.check_token(user, token):
        user.email_confirmed = True
        user.save()
        login(request, user)
        messages.success(request, 'Su correo ha sido confirmado exitosamente')
        if request.user.is_authenticated:
            return redirect('planificaciones')
        return redirect('login')
    else:
        messages.error(request, 'Error. El enlace no es válido o ha expirado.')
        return redirect('home')


class ProfileView(LoginRequiredMixin, UpdateView):
    """Vista para ver y actualzar la información de usuario"""
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
    html_email_template_name = 'accounts/password_reset_email.html',
    subject_template_name = 'accounts/password_reset_subject.txt'
    template_name = 'accounts/password_reset.html'

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # pragma: no cover
        context.update({  # pragma: no cover
            'reset_form': PasswordResetForm(),
        })
        return context  # pragma: no cover


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    """
    Vista usada para ir al formulario para cambiar contraseña desde el email.
    Luego de ingresar la nueva contraseña se enviará al usuario a la página
    principal de planificaciones ya autenticado.
    """
    form_class = CustomSetPasswordForm
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


class CustomPasswordChangeView(PasswordChangeView):
    """
    Vista usada para ir al formulario para cambiar contraseña desde el email.
    Luego de ingresar la nueva contraseña se enviará al usuario a la página
    principal de planificaciones ya autenticado.
    """
    form_class = CustomPasswordChangeForm
    success_url = reverse_lazy('planificaciones')
    template_name = 'accounts/password_change.html'

    def form_valid(self, form):
        """Method to add a success message"""
        messages.success(
            self.request,
            'Tu contraseña ha sido cambiada exitosamente.'
        )
        return super().form_valid(form)
