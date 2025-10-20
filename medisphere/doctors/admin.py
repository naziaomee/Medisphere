from django.contrib import admin
from .models import Prescription
from .models import AmbulanceRequest
from .models import (
    Product,
    Medicine,
    VitaminProduct,
    DentalProduct,
    Doctor,
    SurgicalProduct,
    BlogPost,
    Prescription,
    BloodRequest,
    AmbulanceRequest # add your blog model here
)

# Optional: Custom admin for BlogPost to show image preview
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'featured_image')  # show image in list
    readonly_fields = ('created_at',)
    search_fields = ('title', 'content')

admin.site.register(BlogPost, BlogPostAdmin)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'doctor', 'patient', 'date_created')
    list_filter = ('date_created',)


@admin.register(BloodRequest)
class BloodRequestAdmin(admin.ModelAdmin):
    list_display = ('blood_type', 'quantity', 'hospital_name', 'contact_info')
    search_fields = ('hospital_name', 'contact_info')
    list_filter = ('blood_type',)

@admin.register(AmbulanceRequest)
class AmbulanceRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'location', 'message', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'phone_number', 'location')

# Register other models
admin.site.register(Product)
admin.site.register(Medicine)
admin.site.register(VitaminProduct)
admin.site.register(DentalProduct)
admin.site.register(Doctor)
admin.site.register(SurgicalProduct)
admin.site.register(Prescription, PrescriptionAdmin)

