from django.contrib import admin
from . import settings
from django.urls import path, include
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('doctors/', include('doctors.urls')),  # Doctors page
    path('emergency/', include('emergency.urls')),  # Emergency request page
    path('blood_donation/', include('blood_donation.urls')),  # Blood donation page
    path('blog/', include('blog.urls')),  # Blog page
    #path('medicines/', include('medicines.urls')),  # Medicines page
    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
