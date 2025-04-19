# blood_donation/views.py
from django.shortcuts import render
from .models import BloodDonor

def blood_donor_list(request):
    donors = BloodDonor.objects.filter(available_for_donations=True)  # Get available donors
    return render(request, 'blood_donation/donor_list.html', {'donors': donors})