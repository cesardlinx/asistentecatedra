import smtplib

import stripe
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.mail import BadHeaderError
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from accounts.mixins import (NotPremiumUserRequiredMixin,
                             NotPerpetualPremiumUserRequiredMixin,
                             NotPerpetualNotPremiumUserRequiredMixin)
from accounts.models import Plan, Subscription

from .helpers import delete_subscription_from_stripe, send_subscription_emails
from .models import Libro, Pregunta

User = get_user_model()

stripe.api_key = settings.STRIPE_SECRET_KEY


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
        return render(request, 'asistente/checkout.html')

    def post(self, request, *args, **kwargs):
        user = User.objects.get(pk=request.user.pk)
        plan_pk = kwargs['plan_id']
        plan = get_object_or_404(Plan, pk=plan_pk)

        plan_id = plan.stripe_plan_id

        try:
            # Deactivates the current active subscription if any
            try:
                active_subscription = Subscription.objects.get(active=True)
                delete_subscription_from_stripe(
                    active_subscription.stripe_subscription_id)

                active_subscription.active = False
                active_subscription.save()
            except Subscription.DoesNotExist:
                pass
            except Exception:
                pass

            token = request.POST.get('stripeToken')

            if plan.plan_type == 'PAGO ÚNICO':
                # Stripe payment
                stripe_charge = stripe.Charge.create(
                    amount=plan.price,
                    currency='usd',
                    source=token,
                    description='Plan PERPETUAL | Asistente de Cátedra',
                )
                if stripe_charge:
                    with transaction.atomic():
                        # Database subscription creation
                        Subscription.objects.create(
                            user=user,
                            plan=plan,
                            stripe_charge_id=stripe_charge.get('id'),
                            active=True
                        )
                        # User is premium now
                        user.is_premium = True
                        user.save()
            else:
                # Stripe subscription creation
                stripe_subscription = stripe.Subscription.create(
                    customer=request.user.stripe_customer_id,
                    items=[
                        {
                            'plan': plan_id
                        }
                    ],
                    source=token
                )
                if stripe_subscription:
                    with transaction.atomic():
                        # Database subscription creation
                        Subscription.objects.create(
                            user=user,
                            plan=plan,
                            stripe_subscription_id=stripe_subscription.get(
                                'id'),
                            active=True
                        )
                        # User is premium now
                        user.is_premium = True
                        user.save()

            # email sending

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
            return render(request, 'asistente/checkout.html')
        except stripe.error.InvalidRequestError:
            # Invalid parameters were supplied to Stripe's API
            messages.error(request, 'Error!. Parámetros inválidos.')
            return render(request, 'asistente/checkout.html')
        except stripe.error.APIConnectionError:
            # Network communication with Stripe failed
            messages.error(request, 'Ha ocurrido un error de comunicación. '
                           'Verifique su conexión.')
            return render(request, 'asistente/checkout.html')
        except stripe.error.StripeError:
            # Stripe generic error
            messages.error(request, 'Ha ocurrido un error en el pago.')
            return render(request, 'asistente/checkout.html')
        except smtplib.SMTPException:
            messages.error(request,
                           'Ha ocurrido un error al tratar de enviar el '
                           'correo.')
        except Exception:
            # Displays a very generic error to the user
            messages.error(request, 'Ha ocurrido un error con la peticion '
                           'realizada.')
            return render(request, 'asistente/checkout.html')

        messages.success(request, 'Su transacción ha sido realizada con éxito')
        return redirect(request.user.get_absolute_url())


@login_required
def cancel_subscription_view(request):
    if request.method == 'POST':
        user = User.objects.get(pk=request.user.pk)
        # Delete previous subscription
        try:
            if user.active_subscription:
                previous_subscription = Subscription.objects.get(
                    pk=user.active_subscription.pk
                )
                delete_subscription_from_stripe(
                    previous_subscription.stripe_subscription_id)
                previous_subscription.active = False
                previous_subscription.save()
        except Subscription.DoesNotExist:
            pass
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

        # Subscribes to free plan
        try:
            free_plan = Plan.objects.get(plan_type='GRATIS')
            with transaction.atomic():
                Subscription.objects.create(
                    plan=free_plan,
                    user=user,
                    active=True
                )
                # User is no longer premium
                user.is_premium = False
                user.save()
        except Plan.DoesNotExist:
            pass
        except Exception:
            pass

        # email sending

        user_mail_subject = 'Asistente de Cátedra | CANCELACIÓN DE '\
                            'SUBSCRIPCIÓN'
        admin_mail_subject = 'Asistente de Cátedra | SUBSCRIPCIÓN CANCELADA'

        try:
            # Checks if there is a previous subscription
            plan = previous_subscription.plan
        except UnboundLocalError:
            plan = False
        except Exception:
            plan = False

        try:
            send_subscription_emails(
                user_mail_subject,
                admin_mail_subject,
                user,
                plan,
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
