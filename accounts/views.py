
import logging
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
                    ProfileForm, SignupForm, PhotoForm)
from .mixins import AnonymousRequiredMixin, CheckRecaptchaMixin
from .tokens import account_token_generator

User = get_user_model()

# Get an instance of a logger
logger = logging.getLogger(__name__)


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

            if user.pk:
                # Email sending
                domain = get_current_site(self.request).domain
                send_confirmation_helper(user, domain)

                # Authentication and Login
                login(self.request, user)
                messages.success(
                    self.request,
                    'Exito!, un email ha sido enviado a tu correo para que '
                    'verifiques tu cuenta.'
                )
                logger.info('Confirmation email sent to {}'.format(user.email))
                return redirect('planificaciones')
            else:
                messages.error(
                    self.request,
                    'Error!, un error ha ocurrido al intentar guardar usuario'
                )
                return redirect('signup')
        else:
            messages.error(
                self.request,
                'reCAPTCHA no válido. Por favor intente de nuevo recargando '
                'la página.'
            )
            logger.error('reCAPTCHA invalid error.')
            # Regresar a la misma página
            return HttpResponseRedirect(self.request.path_info)


@login_required
def send_confirmation_view(request):
    """
    Vista para enviar correo de confirmacion de email desde un
    usuario logeado
    """
    if request.method == 'GET':
        if not request.user.email_confirmed:
            domain = get_current_site(request).domain
            send_confirmation_helper(request.user, domain)
            messages.success(
                request,
                'Un mensaje ha sido enviado a tu correo para que '
                'verifiques tu cuenta.'
            )
            logger.info('Confirmation email sent to {}'.format(
                request.user.email))
        else:
            messages.info(request, 'Su cuenta ya está verificada')
        return redirect('profile', pk=request.user.pk, slug=request.user.slug)
    else:
        return HttpResponse(status=405)


class CustomLoginView(AnonymousRequiredMixin, LoginView):
    """Vista para autenticación de usuarios"""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'reset_form': PasswordResetForm(),
        })
        return context

    def form_valid(self, form):
        email = form.cleaned_data.get('username')
        logger.info('User {} has logged in successfuly.'.format(email))
        return super().form_valid(form)

    def form_invalid(self, form):
        email = form.cleaned_data.get('username')
        logger.error('There has been a failed login.'.format(email))
        return super().form_invalid(form)


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
    """Validador remoto para verificar si existe ya el email de un usuario"""
    if request.method == 'POST':
        response_str = 'false'
        if request.is_ajax():
            email = request.POST.get('email')
            if email:
                try:
                    get_object_or_404(User, email=email)
                except Http404:
                    response_str = 'false'  # User doesn't exists
                else:
                    response_str = 'true'  # User already exists

        return HttpResponse('{}'.format(response_str))
    else:
        return HttpResponse(status=405)


def confirm_email_view(request, uidb64, token):
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
        logger.info('Email address: {} successfuly confirmed.'.format(
            user.email))
        return redirect('planificaciones')
    else:
        messages.error(request, 'Error. El enlace no es válido o ha expirado.')
        logger.error("Email address can't be confirmed.")
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
        logger.info('User {} has updated his data successfuly.'.format(
            self.object.email))
        url = reverse('profile', kwargs={
            'pk': self.object.pk,
            'slug': self.object.slug
        })
        return redirect(url)

    def photo_form(self):
        """Adds photo form to view variable in template"""
        return PhotoForm()


@login_required
def photo_upload_view(request):
    """Adds a photo to the authenticated user"""
    if request.method == 'POST':
        user = get_object_or_404(User, pk=request.user.pk)
        form = PhotoForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
        else:
            messages.error(
                request,
                'Ha ocurrido un error al intentar subir la foto.'
            )
        return redirect('profile',
                        pk=request.user.pk, slug=request.user.slug)
    else:
        return HttpResponse(status=405)


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
            logger.info(
                'A reset password email has been sent to the email {}.'
                .format(email))
        else:
            messages.error(
                self.request,
                'La cuenta de correo que has escrito es incorrecta, verifica '
                'tus datos.'
            )
            logger.error(
                'Wrong user email in a reset pasword email request.')
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
        logger.info('The user {} has successfuly changed his password.'
                    .format(self.request.user.email))
        return super().form_valid(form)
