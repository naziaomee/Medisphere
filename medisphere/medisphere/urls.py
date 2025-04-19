# medisphere/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('doctors/', include('doctors.urls')),  # Doctors page
    path('emergency/', include('emergency.urls')),  # Emergency request page
    path('blood_donation/', include('blood_donation.urls')),  # Blood donation page
    path('blog/', include('blog.urls')),  # Blog page
    path('medicines/', include('medicines.urls')),  # Medicines page
]