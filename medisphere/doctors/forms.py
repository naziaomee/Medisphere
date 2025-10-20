from django import forms
from .models import AmbulanceRequest
from .models import BlogPost
from .models import BloodRequest
from .models import Doctor
from .models import Prescription


class AmbulanceRequestForm(forms.ModelForm):
    class Meta:
        model = AmbulanceRequest
        fields = ["name", "phone_number", "location", "message"]


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title", "content", "featured_image"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "w-full p-3 border rounded-lg"}),
            "content": forms.Textarea(attrs={"class": "w-full p-3 border rounded-lg"}),
            "featured_image": forms.ClearableFileInput(attrs={"class": "w-full"}),
        }


class BloodRequestForm(forms.ModelForm):
    class Meta:
        model = BloodRequest
        fields = ["blood_type", "quantity", "hospital_name", "contact_info"]


class DoctorUpdateForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = [
            "name",
            "specialty",
            "bio",
            "medical_college",
            "appointment_time",
            "payment_method",
            "visit_fee",
            "image",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "specialty": forms.TextInput(attrs={"class": "form-control"}),
            "bio": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "medical_college": forms.TextInput(attrs={"class": "form-control"}),
            "appointment_time": forms.TextInput(attrs={"class": "form-control"}),
            "payment_method": forms.TextInput(attrs={"class": "form-control"}),
            "visit_fee": forms.NumberInput(attrs={"class": "form-control"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ["patient", "diagnosis", "medicines", "advice"]
        widgets = {
            "diagnosis": forms.Textarea(attrs={"rows": 3, "placeholder": "Enter diagnosis"}),
            "medicines": forms.Textarea(
                attrs={"rows": 4, "placeholder": "Medicine, Dosage, Frequency, Duration"}
            ),
            "advice": forms.Textarea(attrs={"rows": 2, "placeholder": "Additional advice"}),
        }


class PatientPrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ["symptoms", "age", "previous_records"]
        widgets = {
            "symptoms": forms.Textarea(attrs={"rows": 4, "placeholder": "Describe your symptoms"}),
            "previous_records": forms.Textarea(
                attrs={"rows": 3, "placeholder": "Previous medical history"}
            ),
            "age": forms.NumberInput(attrs={"placeholder": "Your age"}),
        }
