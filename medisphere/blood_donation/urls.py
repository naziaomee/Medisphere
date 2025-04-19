# blood_donation/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('donors/', views.blood_donor_list, name='blood_donor_list'),  # List of blood donors
]