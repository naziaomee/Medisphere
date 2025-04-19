# emergency/views.py
from django.shortcuts import render, redirect
from .models import EmergencyRequest

def emergency_request(request):
    if request.method == 'POST':
        patient_name = request.POST['patient_name']
        contact_number = request.POST['contact_number']
        description = request.POST['description']
        
        # Save the emergency request to the database
        EmergencyRequest.objects.create(
            patient_name=patient_name,
            contact_number=contact_number,
            description=description,
        )
        return redirect('home')  # Redirect to home page after submission
    return render(request, 'emergency/emergency_form.html')