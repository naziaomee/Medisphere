# doctors/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctor_list, name='doctor_list'),  
    path('general-medicine/', views.general_medicine_doctors, name='general_medicine_doctors'),
    path('neurologists/', views.neurologists, name='neurologists'),

]