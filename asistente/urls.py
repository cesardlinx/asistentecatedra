from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name="home"),
    path('biblioteca/', views.BibliotecaListView.as_view(), name="biblioteca"),
    path('ayuda/', views.AyudaListView.as_view(), name="ayuda"),
    path('premium/', views.PremiumListView.as_view(), name="premium"),
    path('contacto/', views.ContactView.as_view(), name="contacto"),
    path('condiciones/', views.CondicionesTemplateView.as_view(),
         name="condiciones"),
    path('privacidad/', views.PrivacidadTemplateView.as_view(),
         name="privacidad"),
    path('cookies/', views.CookiesTemplateView.as_view(), name="cookies"),
    path('checkout/<int:plan_id>/<slug:plan_slug>/',
         views.CheckoutView.as_view(), name="checkout"),
    path('cancel_subscription/', views.cancel_subscription_view,
         name="cancel_subscription"),
    path('cambiar_plan/', views.ChangePlanListView.as_view(),
         name="change_plan"),
    path('stripe_webhooks/', views.stripe_webhooks_view,
         name="stripe_webhooks"),
]
