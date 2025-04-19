from django.db import models

class EmergencyRequest(models.Model):
    patient_name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)
    description = models.TextField()  # Description of the emergency
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Emergency Request by {self.patient_name}"