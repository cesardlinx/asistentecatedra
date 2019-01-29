from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('confirm-email/<uidb64>/<token>/', views.confirm_email,
         name='confirm_email'),
    path('ajax/unique_email_validator/', views.unique_email_validator,
         name='ajax_unique_email_validator'),
]
