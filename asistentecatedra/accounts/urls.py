from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

urlpatterns = [
     path('signup/', views.SignupView.as_view(), name='signup'),
     path('confirm-email/<uidb64>/<token>/',
          views.confirm_email,
          name='confirm_email'),
     path('ajax/unique_email_validator/',
          views.unique_email_validator,
          name='ajax_unique_email_validator'),
     path('login/',
          LoginView.as_view(template_name='accounts/login.html'),
          name='login'),
     path('logout/', LogoutView.as_view(), name='logout'),
     path('profile/<int:pk>/<slug:slug>/',
          views.ProfileView.as_view(),
          name='profile'),
     path('password_reset/',
          views.CustomPasswordResetView.as_view(),
          name='password_reset'),
     path('password_reset_confirm/<uidb64>/<token>/',
          views.CustomPasswordResetConfirmView.as_view(),
          name='password_reset_confirm'),
     path('password_change/',
          views.CustomPasswordChangeView.as_view(),
          name='password_change'),
]
