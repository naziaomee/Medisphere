from django.db import models

class BloodDonor(models.Model):
    objects = None
    name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)
    blood_type = models.CharField(max_length=3)
    available_for_donations = models.BooleanField(default=True)

    def _str_(self):
        return f"Donor: {self.name} ({self.blood_type})"