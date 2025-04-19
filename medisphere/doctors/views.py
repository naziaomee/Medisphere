# doctors/views.py
from django.shortcuts import render
from .models import Doctor

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors/doctor_list.html', {'doctors': doctors})

def general_medicine_doctors(request):
    general_doctors = Doctor.objects.filter(specialization='General Medicine')
    return render(request, 'doctors/general_medicine.html', {'doctors': general_doctors})
def neurologists(request):
    neurologists = Doctor.objects.filter(specialization='Neurology')
    return render(request, 'doctors/neurologists.html', {'doctors': neurologists})