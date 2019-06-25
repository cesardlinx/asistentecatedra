import smtplib
import logging
import stripe
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.mail import BadHeaderError
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from accounts.mixins import (NotPerpetualNotPremiumUserRequiredMixin,
                             NotPerpetualPremiumUserRequiredMixin,
                             NotPremiumUserRequiredMixin)
from accounts.models import Plan, Subscription

from .helpers import send_subscription_emails, send_invoice_email
from .models import Libro, Pregunta

User = get_user_model()

# Get an instance of a logger
logger = logging.getLogger(__name__)

stripe.api_key = settings.STRIPE_SECRET_KEY
endpoint_secret = settings.STRIPE_WEBHOOKS_SECRET


class HomeTemplateView(TemplateView):
    """Vista principal de la aplicación"""
    template_name = 'asistente/home.html'


class BibliotecaListView(ListView):
    """Biblioteca"""
    model = Libro
    template_name = 'asistente/biblioteca.html'

    def get_context_data(self, **kwargs):
        return Libro.objects.get_libros_por_asignaturas()


class AyudaListView(ListView):
    """Ayuda"""
    template_name = 'asistente/ayuda.html'
    model = Pregunta
    context_object_name = 'preguntas'


class PremiumListView(NotPremiumUserRequiredMixin, ListView):
    """Vista de la pantalla para subscripción Premium"""
    model = Plan
    context_object_name = 'plans'
    template_name = 'asistente/premium.html'


class ChangePlanListView(NotPerpetualNotPremiumUserRequiredMixin,
                         ListView):
    """
    Vista que muestra los planes para que el usuario pueda cambiar de
    plan
    """
    model = Plan
    context_object_name = 'plans'
    template_name = 'asistente/change_plan.html'


class CheckoutView(NotPerpetualPremiumUserRequiredMixin, View):
    """Vista para la pantalla de pago"""
    def get(self, request, *args, **kwargs):
        plan_pk = kwargs['plan_id']
        plan_slug = kwargs['plan_slug']
        plan = get_object_or_404(Plan, pk=plan_pk, slug=plan_slug)
        return render(request, 'asistente/checkout.html', {'plan': plan})

    def post(self, request, *args, **kwargs):
        user = User.objects.get(pk=request.user.pk)
        plan_pk = kwargs['plan_id']
        plan_slug = kwargs['plan_slug']
        plan = get_object_or_404(Plan, pk=plan_pk, slug=plan_slug)

        token = request.POST.get('stripeToken')
        try:
            # Subscription creation
            Subscription.objects.create_subscription(
                user,
                plan,
                token
            )
        except stripe.error.CardError as e:
            logger.error('CardError: ' + e.user_message)
            messages.error(request, 'Error. La tarjeta de crédito ingresada '
                           'no es válida.')
            return render(request, 'asistente/checkout.html', {'plan': plan})
        except stripe.error.InvalidRequestError as e:
            # Invalid parameters were supplied to Stripe's API
            logger.error('InvalidRequestError: ' + e.user_message)
            messages.error(request, 'Error!. Parámetros inválidos.')
            return render(request, 'asistente/checkout.html', {'plan': plan})
        except stripe.error.APIConnectionError as e:
            # Network communication with Stripe failed
            logger.error('APIConnectionError: ' + e.user_message)
            messages.error(request, 'Ha ocurrido un error de comunicación. '
                           'Verifique su conexión.')
            return render(request, 'asistente/checkout.html', {'plan': plan})
        except stripe.error.StripeError as e:
            # Stripe generic error
            logger.error('StripeError: ' + e.user_message)
            messages.error(request, 'Ha ocurrido un error en el pago.')
            return render(request, 'asistente/checkout.html', {'plan': plan})
        except Exception as e:
            # Displays a very generic error to the user
            logger.error('Exception: ' + e.args[0])
            messages.error(request, 'Ha ocurrido un error con la peticion '
                           'realizada.')
            return render(request, 'asistente/checkout.html', {'plan': plan})

        messages.info(request, 'Su petición ha sido realizada con éxito. '
                               'revise su correo para verificar que se '
                               'realizado correctamente el pago.')
        return redirect(request.user.get_absolute_url())


@login_required
def cancel_subscription_view(request):
    if request.method == 'POST':
        user = User.objects.get(pk=request.user.pk)
        try:
            with transaction.atomic():
                # Cancel subscription
                user.cancel_active_subscription()
                # User is no longer premium
                user.is_premium = False
                user.save()

        except stripe.error.InvalidRequestError as e:
            # Invalid parameters were supplied to Stripe's API
            logger.error('InvalidRequestError: ' + e.user_message)
            messages.error(request, 'Error!. Parámetros inválidos.')
            return redirect(user.get_absolute_url())
        except stripe.error.APIConnectionError as e:
            # Network communication with Stripe failed
            logger.error('APIConnectionError: ' + e.user_message)
            messages.error(request, 'Ha ocurrido un error de comunicaciones. '
                           'Verifique su conexión.')
            return redirect(user.get_absolute_url())
        except stripe.error.StripeError as e:
            # General Stripe Error
            logger.error('StripeError: ' + e.user_message)
            messages.error(request, 'Ha ocurrido un error al tratar de '
                           'cancelar la subscripción.')
            return redirect(user.get_absolute_url())
        except Exception as e:
            # Display a very generic error to the user, and maybe send
            # yourself an email
            logger.error('Exception: ' + e.args[0])
            messages.error(request, 'Ha ocurrido un error con la peticion '
                           'realizada.')
            return redirect(user.get_absolute_url())

        logger.info('User subscription successfully cancelled')
        messages.success(request,
                         'Su subscripción ha sido cancelada con éxito')
        return redirect(user.get_absolute_url())
    else:
        return redirect(request.user.get_absolute_url())


@csrf_exempt
def stripe_webhooks_view(request):
    """Handles Stripe events for sending emails"""
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        # constuct event
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        logger.error('ValueError: ' + e.args[0])
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        logger.error('SignatureVerificationError: ' +
                     e.user_message)
        # Invalid signature
        return HttpResponse(status=400)

    logger.info('Stripe event received: ' + event.type)

    # getting the user
    stripe_customer_id = event.data.object.customer
    user = User.objects.get(stripe_customer_id=stripe_customer_id)

    # Handle the event
    if event.type == 'customer.subscription.created':
        # Cuando se ha creado exitosamente la subscripción
        plan = event.data.object.plan.nickname

        try:
            user_mail_subject = 'Asistente de Cátedra | SUBSCRIPCIÓN'
            admin_mail_subject = 'Asistente de Cátedra | SUBSCRIPCIÓN '\
                'AÑADIDA'

            send_subscription_emails(
                user_mail_subject,
                admin_mail_subject,
                user,
                plan
            )
        except BadHeaderError as e:
            logger.error('BadHeaderError: ' + e.args[0])
            return HttpResponse(status=400)
        except smtplib.SMTPException as e:
            logger.error('SMTPException: ' + e.args[0])
            return HttpResponse(status=400)

    elif event.type == 'invoice.payment_succeeded':
        # Cuando el pago es exitoso
        amount_paid = event.data.object.amount_paid / 100
        plan = event.data.object.lines.data[0].plan.nickname

        user_mail_subject = 'Asistente de Cátedra | PAGO DE '\
            'SUBSCRIPCIÓN'

        # el usuario es premium solo si el pago es exitoso
        user.is_premium = True
        user.save()

        try:
            # Envío del email
            send_invoice_email(
                user_mail_subject,
                user,
                plan,
                amount_paid,
            )
        except BadHeaderError as e:
            logger.error('BadHeaderError: ' + e.args[0])
            return HttpResponse(status=400)
        except smtplib.SMTPException as e:
            logger.error('SMTPException: ' + e.args[0])
            return HttpResponse(status=400)

    elif event.type == 'invoice.payment_failed':
        # Cuando falla el pago
        amount_paid = event.data.object.amount_paid / 100
        plan = event.data.object.lines.data[0].plan.nickname

        user_mail_subject = 'Asistente de Cátedra | PAGO DE '\
            'SUBSCRIPCIÓN FALLIDO'
        try:
            # Envío del email
            send_invoice_email(
                user_mail_subject,
                user,
                plan,
                amount_paid,
                success=False
            )
        except BadHeaderError as e:
            logger.error('BadHeaderError: ' + e.args[0])
            return HttpResponse(status=400)
        except smtplib.SMTPException as e:
            logger.error('SMTPException: ' + e.args[0])
            return HttpResponse(status=400)
        finally:
            try:
                with transaction.atomic():
                    # cancela la subscripción por falta de pago
                    user.cancel_active_subscription()
                    user.is_premium = False
                    user.save()
            except stripe.error.StripeError as e:
                logger.error('StripeError: ' + e.args[0])
                return HttpResponse(status=400)
            except Exception as e:
                logger.error('Exception: ' + e.args[0])
                return HttpResponse(status=400)

    elif event.type == 'customer.subscription.deleted':
        """Cuando el usuario cancela su subscripción"""
        plan = event.data.object.plan.nickname

        user_mail_subject = 'Asistente de Cátedra | CANCELACIÓN DE '\
            'SUBSCRIPCIÓN'
        admin_mail_subject = 'Asistente de Cátedra | SUBSCRIPCIÓN '\
            'CANCELADA'
        try:
            # Envío de emails
            send_subscription_emails(
                user_mail_subject,
                admin_mail_subject,
                user,
                plan,
                cancel=True
            )
        except BadHeaderError as e:
            logger.error('BadHeaderError: ' + e.args[0])
            return HttpResponse(status=400)
        except smtplib.SMTPException as e:
            logger.error('SMTPException: ' + e.args[0])
            return HttpResponse(status=400)

    elif event.type == 'charge.succeeded':
        """Cuando se subscribe al plan PAGO ÚNICO"""
        plan = 'PAGO ÚNICO'
        charge_description = event.data.object.description
        amount_paid = event.data.object.amount / 100

        if plan in charge_description:
            user_mail_subject = 'Asistente de Cátedra | SUBSCRIPCIÓN'
            admin_mail_subject = 'Asistente de Cátedra | SUBSCRIPCIÓN '\
                'AÑADIDA'
            user_mail_subject_payment = 'Asistente de Cátedra | PAGO DE '\
                'SUBSCRIPCIÓN'

            user.is_premium = True
            user.save()

            try:
                # envío de email
                send_subscription_emails(
                    user_mail_subject,
                    admin_mail_subject,
                    user,
                    plan
                )
                send_invoice_email(
                    user_mail_subject_payment,
                    user,
                    plan,
                    amount_paid,
                )
            except BadHeaderError as e:
                logger.error('BadHeaderError: ' + e.args[0])
                return HttpResponse(status=400)
            except smtplib.SMTPException as e:
                logger.error('SMTPException: ' + e.args[0])
                return HttpResponse(status=400)

    elif event.type == 'charge.failed':
        """Cuando falla el pago al tratar de subscribirse al plan PAGO ÚNICO"""
        plan = 'PAGO ÚNICO'
        charge_description = event.data.object.description
        amount_paid = event.data.object.amount

        if plan in charge_description:
            user_mail_subject = 'Asistente de Cátedra | PAGO DE '\
                'SUBSCRIPCIÓN FALLIDO'
            try:
                # Envío del email
                send_invoice_email(
                    user_mail_subject,
                    user,
                    plan,
                    amount_paid,
                    success=False
                )
            except BadHeaderError as e:
                logger.error('BadHeaderError: ' + e.args[0])
                return HttpResponse(status=400)
            except smtplib.SMTPException as e:
                logger.error('SMTPException: ' + e.args[0])
                return HttpResponse(status=400)

    return HttpResponse(status=200)
