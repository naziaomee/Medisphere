from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class AmbulanceRequest(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length=255)
    message = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request by {self.name} at {self.created_at}"
    

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    featured_image = models.ImageField(upload_to='blog_images/', blank=True, null=True)  # new image field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 

class Product(models.Model):
    name = models.CharField(max_length=100) 
    description = models.TextField() 
    price = models.DecimalField(max_digits=6, decimal_places=2)  
    image = models.ImageField(upload_to='products/', blank=True, null=True)  

    def __str__(self):
        return self.name
    

class Medicine(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='medicines/', blank=True, null=True)
    
    def __str__(self):
        return self.name

class SurgicalProduct(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='surgical_products/', blank=True, null=True)

    def __str__(self):
        return self.name


class VitaminProduct(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='vitamins/', null=True, blank=True)

    def __str__(self):
        return self.name

class DentalProduct(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='dental_products/', null=True, blank=True)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    medical_college = models.CharField(max_length=150, blank=True)
    appointment_time = models.CharField(max_length=100, blank=True)
    payment_method = models.CharField(max_length=100, default='bKash')
    visit_fee = models.IntegerField(default=1000)
    image = models.ImageField(upload_to='doctor_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class BloodRequest(models.Model):
    BLOOD_TYPES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    ]
    
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPES)
    quantity = models.IntegerField()
    hospital_name = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.blood_type} - {self.quantity} units'
    from django.db import models

class Doctor_Dash(models.Model):
    name = models.CharField(max_length=200)
    specialty = models.CharField(max_length=100)
    medical_college = models.CharField(max_length=200, default="Not Set")
    appointment_time = models.CharField(max_length=100, default="Not Set")
    payment_method = models.CharField(max_length=100, default="Not Set")
    visit_fee = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    bio = models.TextField(blank=True, default="Not Set")
    image = models.ImageField(upload_to='doctor_images/', blank=True, null=True)
    
    # ✅ FIXED EMAIL FIELD (removed unique=True and allowed blank/null)
    email = models.EmailField(blank=True, null=True)
    
    password = models.CharField(max_length=128)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    # --- NEW DYNAMIC NOTIFICATION PREFERENCE FIELDS ---
    receive_new_request_notif = models.BooleanField(default=True, help_text="Receive alerts for new prescription requests.")
    receive_appointment_reminder = models.BooleanField(default=True, help_text="Receive reminders for scheduled appointments.")
    receive_message_alerts = models.BooleanField(default=False, help_text="Receive alerts for direct patient messages.")
    receive_performance_report = models.BooleanField(default=True, help_text="Receive weekly performance reports.")
    # ----------------------------------------------------

    def __str__(self):
        return self.name

class Prescription(models.Model):
    doctor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="doctor_prescriptions"
    )
    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="patient_prescriptions"
    )
    symptoms = models.TextField(help_text="Patient describes their symptoms")
    age = models.PositiveIntegerField(default=0)
    previous_records = models.TextField(blank=True, null=True)
    diagnosis = models.TextField(blank=True, null=True)  # doctor fills
    medicines = models.TextField(
        help_text="List medicines with dosage, frequency, duration",
        blank=True,
        null=True
    )
    advice = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.doctor:
            return f"Prescription by {self.doctor} for {self.patient} on {self.date_created.date()}"
        else:
            return f"Prescription request by {self.patient} on {self.date_created.date()}"


# -----------------------
# Notifications
# -----------------------
class Notification(models.Model):
    doctor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notifications'
    )
    prescription = models.ForeignKey(
        Prescription,
        on_delete=models.CASCADE,
        related_name='notifications'
    )
    text = models.CharField(max_length=200)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.doctor.username}: {self.text}"