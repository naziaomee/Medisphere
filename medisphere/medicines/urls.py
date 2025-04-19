# medicines/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.medicine_list, name='medicine_list'),  # List of medicines
]