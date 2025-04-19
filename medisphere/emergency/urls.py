# emergency/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('request/', views.emergency_request, name='emergency_request'),  # Emergency request page
]