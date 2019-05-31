from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name="home"),
    path('biblioteca/', views.BibliotecaListView.as_view(), name="biblioteca"),
    path('ayuda/', views.AyudaListView.as_view(), name="ayuda"),
    path('premium/', views.PremiumTemplateView.as_view(), name="premium"),
    path('checkout/<int:plan_id>/', views.CheckoutView.as_view(),
         name="checkout"),
    path('cancel_subscription/', views.cancel_subscription_view,
         name="cancel_subscription"),
]
