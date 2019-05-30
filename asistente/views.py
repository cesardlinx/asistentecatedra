import stripe
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from accounts.models import Plan, Subscription

from .helpers import delete_subscription_from_stripe
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


class PremiumTemplateView(TemplateView):
    """Vista de la pantalla para subscripción Premium"""
    template_name = 'asistente/premium.html'


class CheckoutView(LoginRequiredMixin, View):
    """Vista para la pantalla de pago"""
    def get(self, request, *args, **kwargs):
        return render(request, 'asistente/checkout.html')

    def post(self, request, *args, **kwargs):
        user = User.objects.get(pk=request.user.pk)
        plan_id = request.POST.get('plan_id')
        try:
            plan = get_object_or_404(Plan, pk=plan_id)
            token = request.POST.get('stripeToken')
            stripe_subscription = stripe.Subscription.create(
                customer=request.user.stripe_customer_id,
                items=[
                    {
                        'plan': plan.id
                    }
                ],
                source=token
            )

            # Deactivates the current active subscription if any
            try:
                active_subscription = Subscription.objects.get(active=True)
                delete_subscription_from_stripe(
                    active_subscription.stripe_subscription_id)

                active_subscription.active = False
                active_subscription.save()
            except Subscription.DoesNotExist:
                pass

            Subscription.objects.create(
                user=user,
                plan=plan,
                stripe_subscription_id=stripe_subscription.get('id'),
                active=True
            )

        except stripe.error.CardError:
            messages.error(request, 'Error. La tarjeta de crédito ingresada '
                           'no es válida.')
            return render(request, 'asistente/checkout.html')
        except ValueError:
            messages.error(request, 'Error. Los datos no son correctos o han '
                           'sido alterados.')
            return render(request, 'asistente/checkout.html')

        messages.success(request, 'Su transacción ha sido realizada con éxito')
        return redirect(request.user.get_absolute_url())


@login_required
def cancel_subscription_view(request):
    if request.method == 'POST':
        try:
            previous_subscription = Subscription.objects.get(
                pk=request.user.active_subscription.pk
            )
            delete_subscription_from_stripe(
                previous_subscription.stripe_subscription_id)
            previous_subscription.active = False
            previous_subscription.save()
        except Subscription.DoesNotExist:
            pass

        try:
            free_plan = Plan.objects.get(plan_type='FREE')
            Subscription.objects.create(
                plan=free_plan,
                user=request.user,
                active=True
            )
        except Plan.DoesNotExist:
            pass

        messages.success(request,
                         'Su subscripción ha sido cancelada con éxito')
        return redirect(request.user.get_absolute_url())
    else:
        return redirect(request.user.get_absolute_url())
