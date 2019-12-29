from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name="home"),
    path('biblioteca/', views.BibliotecaListView.as_view(), name="biblioteca"),
    path('ayuda/', views.AyudaListView.as_view(), name="ayuda"),
    path('contacto/', views.ContactView.as_view(), name="contacto"),
    path('condiciones/', views.CondicionesTemplateView.as_view(),
         name="condiciones"),
    path('privacidad/', views.PrivacidadTemplateView.as_view(),
         name="privacidad"),
    path('cookies/', views.CookiesTemplateView.as_view(), name="cookies"),
]
