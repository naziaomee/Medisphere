from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Doctor views
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctor/<int:doctor_id>/', views.doctor_profile, name='doctor_profile'),

    # Authentication
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    
    # Home
    path('home/', views.home, name='home'),
    
    # Ambulance
    path('ambulance/', views.ambulance_home, name='ambulance_home'),
    path('request_success/', views.request_success, name='request_success'),
    # Health & Blog
    path('health/', views.health_care, name='health_care'),
    path('health/delete/<int:id>/', views.delete_blog, name='delete_blog'),
    path('health/update/<int:id>/', views.update_blog, name='update_blog'),
    
    # Pharmacy
    path('pharmacy/', views.pharmacy_view, name='pharmacy'),
    path('babycare/', views.baby_care, name='babycare'),
    
    # Products
    path('products/', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    
    # Medicines
    path('medicines/', views.medicine_list, name='medicine_list'),
    path('medicine/<int:medicine_id>/', views.medicine_detail, name='medicine_detail'),
    
    # Surgical
    path('surgical/', views.surgical_list, name='surgical_list'),
    path('surgical/<int:pk>/', views.surgical_detail, name='surgical_detail'),
    
    # Vitamins
    path('vitamins/', views.vitamins_list, name='vitamins'),
    path('vitamins/<int:pk>/', views.vitamins_detail, name='vitamins_detail'),
    
    # Dental
    path('dental/', views.dental_products, name='dental_products'),
    path('dental/<int:pk>/', views.dental_detail, name='dental_detail'),
    
    # General Medicine
    path('general_medicine/', views.general_medicine, name='general_medicine'),
    
    # Neurologists
    path('neurologists/', views.neurologist_list, name='neurologists'),
    path('neurologist/<int:doctor_id>/', views.neurologist_profile, name='neurologist_profile'),
    
    # Smile Experts / Dental Surgeon
    path('smile-experts/', views.smile_experts_list, name='smile_experts_list'),
    path('smile-experts/<int:doctor_id>/', views.smile_expert_profile, name='smile_expert_profile'),
    
    # Dermatologists
    path('dermatologists/', views.dermatologist_list, name='dermatologist_list'),
    path('dermatologists/<int:id>/', views.dermatologist_profile, name='dermatologist_profile'),
    
    # Blood Request
    path('blood-request/', views.blood_request, name='blood_request'),
    path('blood-request-success/', views.blood_request_success, name='blood_request_success'),
    #doctor_home
    path('register_doc/', views.register_doctor, name='register_doctor'),
    path('login_doctor/', views.login_doctor, name='doctor_login'),
    # Doctor Dashboard
    path('doctor_dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('prescription/', views.create_prescription, name='create_prescription'),
    path("patient_prescription/", views.patient_prescriptions, name="patient_prescriptions"),
    path("request_prescription/", views.request_prescription, name="request_prescription"),
    path('request_sucess/', views.request_success, name='request_sucess'),
    path('notification/read/<int:pk>/', views.mark_notification_read, name='mark_notification_read')
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
