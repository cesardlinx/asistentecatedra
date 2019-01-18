from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('biblioteca/', views.biblioteca, name="biblioteca"),
    path('ayuda/', views.ayuda, name="ayuda"),
    path('premium/', views.premium, name="premium"),
]
