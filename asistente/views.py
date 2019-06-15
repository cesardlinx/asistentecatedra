import smtplib

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

from .helpers import send_subscription_emails
from .models import Libro, Pregunta

User = get_user_model()

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
            with transaction.atomic():
                Subscription.objects.create_subscription(
                    user,
                    plan,
                    token
                )
                user.is_premium = True
                user.save()

            user_mail_subject = 'Asistente de Cátedra | SUBSCRIPCIÓN'
            admin_mail_subject = 'Asistente de Cátedra | SUBSCRIPCIÓN AÑADIDA'

            send_subscription_emails(
                user_mail_subject,
                admin_mail_subject,
                user,
                plan
            )

        except BadHeaderError:
            messages.error(request,
                           'Ha ocurrido un error al tratar de enviar el '
                           'correo.')
        except stripe.error.CardError:
            messages.error(request, 'Error. La tarjeta de crédito ingresada '
                           'no es válida.')
            return render(request, 'asistente/checkout.html', {'plan': plan})
        except stripe.error.InvalidRequestError:
            # Invalid parameters were supplied to Stripe's API
            messages.error(request, 'Error!. Parámetros inválidos.')
            return render(request, 'asistente/checkout.html', {'plan': plan})
        except stripe.error.APIConnectionError:
            # Network communication with Stripe failed
            messages.error(request, 'Ha ocurrido un error de comunicación. '
                           'Verifique su conexión.')
            return render(request, 'asistente/checkout.html', {'plan': plan})
        except stripe.error.StripeError:
            # Stripe generic error
            messages.error(request, 'Ha ocurrido un error en el pago.')
            return render(request, 'asistente/checkout.html', {'plan': plan})
        except smtplib.SMTPException:
            messages.error(request,
                           'Ha ocurrido un error al tratar de enviar el '
                           'correo.')
        except Exception:
            # Displays a very generic error to the user
            messages.error(request, 'Ha ocurrido un error con la peticion '
                           'realizada.')
            return render(request, 'asistente/checkout.html', {'plan': plan})

        messages.success(request, 'Su transacción ha sido realizada con éxito')
        return redirect(request.user.get_absolute_url())


@login_required
def cancel_subscription_view(request):
    if request.method == 'POST':
        user = User.objects.get(pk=request.user.pk)
        previous_plan = user.active_plan
        try:
            with transaction.atomic():
                user.cancel_active_subscription()
                # User is no longer premium
                user.is_premium = False
                user.save()

        except stripe.error.InvalidRequestError:
            # Invalid parameters were supplied to Stripe's API
            messages.error(request, 'Error!. Parámetros inválidos.')
            return redirect(user.get_absolute_url())
        except stripe.error.APIConnectionError:
            # Network communication with Stripe failed
            messages.error(request, 'Ha ocurrido un error de comunicaciones. '
                           'Verifique su conexión.')
            return redirect(user.get_absolute_url())
        except stripe.error.StripeError:
            # General Stripe Error
            messages.error(request, 'Ha ocurrido un error al tratar de '
                           'cancelar la subscripción.')
            return redirect(user.get_absolute_url())
        except Exception:
            # Display a very generic error to the user, and maybe send
            # yourself an email
            messages.error(request, 'Ha ocurrido un error con la peticion '
                           'realizada.')
            return redirect(user.get_absolute_url())

        # email sending

        user_mail_subject = 'Asistente de Cátedra | CANCELACIÓN DE '\
                            'SUBSCRIPCIÓN'
        admin_mail_subject = 'Asistente de Cátedra | SUBSCRIPCIÓN CANCELADA'

        try:
            send_subscription_emails(
                user_mail_subject,
                admin_mail_subject,
                user,
                previous_plan,
                cancel=True
            )
        except smtplib.SMTPException:
            messages.error(request,
                           'Ha ocurrido un error al tratar de enviar el '
                           'correo.')
        except BadHeaderError:
            messages.error(request,
                           'Ha ocurrido un error al tratar de enviar el '
                           'correo.')
        except Exception:

            messages.error(request,
                           'Ha ocurrido un error al tratar de enviar el '
                           'correo.')

        messages.success(request,
                         'Su subscripción ha sido cancelada con éxito')
        return redirect(user.get_absolute_url())
    else:
        return redirect(request.user.get_absolute_url())


@csrf_exempt
def stripe_webhooks_view(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        # Invalid signature
        return HttpResponse(status=400)

        # Handle the event
        # if event.type == 'payment_intent.succeeded'
        # payment_intent = event.data.object # contains a stripe.PaymentIntent
        # handle_payment_intent_succeeded(payment_intent)
        # elif event.type == 'payment_method.attached'
        # payment_method = event.data.object # contains a stripe.PaymentMethod
        # handle_payment_method_attached(payment_method)
        # ... handle other event types
        # else
        # Unexpected event type
        # return HttpResponse(status=400)
        # end

    return HttpResponse(status=200)
