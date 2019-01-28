from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('ajax/unique_email_validator/', views.unique_email_validator,
         name='ajax_unique_email_validator'),
]
