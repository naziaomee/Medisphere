from django.shortcuts import render, redirect
from .models import Doctor
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .models import AmbulanceRequest 
from .forms import AmbulanceRequestForm
from django.shortcuts import get_object_or_404
from .forms import BlogPostForm 
from .models import BlogPost
from .models import Product
from .models import Medicine
from .models import SurgicalProduct
from .models import VitaminProduct
from .models import DentalProduct
from .forms import BloodRequestForm
from .models import Doctor_Dash
from .forms import DoctorUpdateForm
from .forms import PrescriptionForm
from .models import Prescription
from .forms import PatientPrescriptionForm
from .models import  Notification
from django.contrib.auth import get_user_model


User = get_user_model()



from django.contrib.auth.decorators import login_required



# Doctor views
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors/doctor_list.html', {'doctors': doctors})

#def general_medicine_doctors(request):
   # general_doctors = Doctor.objects.filter(specialization='General Medicine')
   # return render(request, 'doctors/general_medicine.html', {'doctors': general_doctors})

#ef neurologists(request):
    #neurologists = Doctor.objects.filter(specialization='Neurology')
    #return render(request, 'doctors/neurologists.html', {'doctors': neurologists})

def doctor_profile(request, doctor_id):
    try:
        doctor = Doctor.objects.get(id=doctor_id)
    except Doctor.DoesNotExist:
        return render(request, 'doctors/doctor_not_found.html', {'doctor_id': doctor_id})
    return render(request, 'doctors/doctor_profile.html', {'doctor': doctor})


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()

    return render(request, 'doctors/register.html', {'form': form})

# Login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Successful login → homepage
    else:
        form = AuthenticationForm()
    
    return render(request, 'doctors/login.html', {'form': form})


# Home
@login_required(login_url='login')  
def home(request):
    return render(request, 'doctors/home.html')
def ambulance_home(request):
    return render(request, 'doctors/ambulance-home.html',{'doctors' :ambulance_home})
def ambulance_request(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        location = request.POST.get('location')
        message = request.POST.get('message')
        urgency = request.POST.get('urgency')  # Get urgency level as well

        AmbulanceRequest.objects.create(
            name=name,
            phone_number=phone_number,
            location=location,
            message=message,
            urgency=urgency
        )
        return redirect('request_success') ##
    
    return render(request, 'doctors/ambulance-home.html')
def ambulance_form_handler(request):
    # Handle POST request (form submission)
    if request.method == "POST":
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        location = request.POST.get('location')
        message = request.POST.get('message')
        urgency = request.POST.get('urgency')  

        # Create the database entry
        AmbulanceRequest.objects.create(
            name=name,
            phone_number=phone_number,
            location=location,
            message=message,
            urgency=urgency
        )
        
        # Redirect to the success page
        return redirect('request_success')
    
    # Handle GET request (displaying the form)
    return render(request, 'doctors/ambulance-home.html')

def request_success(request):
    return render(request, 'doctors/request_success.html',{'doctors':request_success})
###########
def edit_blog_post(request, pk):
    post = BlogPost.objects.get(pk=pk)
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)  # request.FILES added
        if form.is_valid():
            form.save()
            return redirect('blog_list')  # or wherever you want
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'doctors/edit_blog.html', {'form': form})

@login_required
def health_care(request):
    posts = BlogPost.objects.all()

    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('health_care')
    else:
        form = BlogPostForm()

    return render(request, 'doctors/health_care.html', {'posts': posts, 'form': form})

@login_required
def update_blog(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)

    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('health_care')  # Redirect back to blog list
    else:
        form = BlogPostForm(instance=post)

    return render(request, 'doctors/edit_blog.html', {'form': form, 'post': post})

@login_required

def delete_blog(request, id):
    post = get_object_or_404(BlogPost, id=id)
    post.delete()
    return redirect('health_care')


def pharmacy_view(request):
    return render(request, 'doctors/pharmacy.html',{'doctors': pharmacy_view})

from django.shortcuts import render

def baby_care(request):
    return render(request, 'doctors/babycare.html',{'doctors':baby_care})

def product_list(request):
   
    query = request.GET.get('q')

   
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()


    return render(request, 'doctors/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)  
    return render(request, 'doctors/product_details.html', {'product': product})
# views.py
def medicine_list(request):
    medicines = Medicine.objects.all()
    return render(request, 'doctors/medicine_list.html', {'medicines': medicines})

def medicine_detail(request, medicine_id):
    medicine = get_object_or_404(Medicine, id=medicine_id)
    added_to_cart = False

    if request.method == 'POST':
        # You can extend this later to actually add to session or database
        added_to_cart = True

    return render(request, 'doctors/medicine_detail.html', {
        'medicine': medicine,
        'added_to_cart': added_to_cart
    })


def surgical_list(request):
    products = SurgicalProduct.objects.all()
    return render(request, 'doctors/surgical.html', {'products': products})

def surgical_detail(request, pk):
    product = get_object_or_404(SurgicalProduct, pk=pk)
    added_to_cart = False

    if request.method == 'POST':
        added_to_cart = True  # simple flag, no messages module

    return render(request, 'doctors/surgical_detail.html', {
        'product': product,
        'added_to_cart': added_to_cart,
    })


def vitamins_list(request):
    products = VitaminProduct.objects.all()
    return render(request, 'doctors/vitamins.html', {'products': products})

def vitamins_detail(request, pk):
    product = get_object_or_404(VitaminProduct, pk=pk)
    added_to_cart = False

    if request.method == 'POST':
        added_to_cart = True  

    return render(request, 'doctors/vitamins_detail.html', {
        'product': product,
        'added_to_cart': added_to_cart
    })


def dental_products(request):
    dental_products = DentalProduct.objects.all()  
    return render(request, 'doctors/dental.html', {'dental_products': dental_products})

def dental_detail(request, pk):
    product = get_object_or_404(DentalProduct, pk=pk)
    return render(request, 'doctors/dental_detail.html', {'product': product})

def general_medicine(request):
    doctors = Doctor.objects.filter(specialty='General Medicine')
    return render(request, 'doctors/general_medicine.html',{'doctors':doctors})
   

def doctor_profile(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    return render(request, 'doctors/profile.html', {'doctor': doctor})


def doctor_profile(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    appointment_booked = False

    if request.method == 'POST':
        # Here, you can later save this appointment to DB if needed
        appointment_booked = True

    return render(request, 'doctors/profile.html', {
        'doctor': doctor,
        'appointment_booked': appointment_booked
    })


def neurologist_list(request):
    doctors = Doctor.objects.filter(specialty='Neurologist')
    return render(request, 'doctors/neurologist.html', {'doctors': doctors})

def neurologist_profile(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    return render(request, 'doctors/neurologist_profile.html', {'doctor': doctor})


def smile_experts_list(request):
    doctors = Doctor.objects.filter(specialty='Dental Surgeon')
    return render(request, 'doctors/smile_experts.html', {'doctors': doctors})


# Inside your view function
def smile_expert_profile(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)

    appointment_success = False
    if request.method == 'POST':
        # Handle the booking logic here
        appointment_success = True  # Set to True once booked

    context = {
        'doctor': doctor,
        'appointment_success': appointment_success,
    }
    return render(request, 'doctors/smile_expert_profile.html', context)

def dermatologist_list(request):
    dermatologists = Doctor.objects.filter(specialty='Dermatology')
    return render(request, 'doctors/dermatologist_list.html', {'dermatologists': dermatologists})

def dermatologist_profile(request, id):
    dermatologist = get_object_or_404(Doctor, id=id)  
    appointment_success = False  
    if request.method == "POST":
       
        appointment_success = True 
    return render(request, 'dermatologists/DProfile.html', {
        'dermatologist': dermatologist,
        'appointment_success': appointment_success
    })


def blood_request(request):
    if request.method == "POST":
        form = BloodRequestForm(request.POST)
        if form.is_valid():
            
            form.save()

            return redirect('blood_request_success')
    else:
        form = BloodRequestForm()

    return render(request, 'doctors/blood_request.html', {'form': form})

def blood_request_success(request):
    return render(request, 'doctors/blood_request_success.html')



def register_doctor(request):
    if request.method == 'POST':
        # Collect data from POST
        name = request.POST.get('name')
        specialty = request.POST.get('specialization')
        medical_college = request.POST.get('bdmc')
        email = request.POST.get('email')
        password = request.POST.get('password')  

       
        doctor = Doctor.objects.create(
            name=name,
            specialty=specialty,
            medical_college=medical_college
        )
        doctor_dash = Doctor_Dash.objects.create(
            name=name,
            specialty=specialty,
            medical_college=medical_college,
            email=email,
            password=password  # Consider hashing with make_password()
        )

        # Redirect to login page or dashboard
        return redirect('login')  # replace 'login' with your URL name

    return render(request, 'doctors/register_as_doc.html')

def login_doctor(request):
    error = ''
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate Django user (username = email)
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)  # ✅ logs in the user session
            return redirect('doctor_dashboard')
        else:
            error = "Invalid Email or Password"

    return render(request, 'doctors/login_doctor.html', {'error': error})

@login_required
def doctor_dashboard(request):
    # Safely get the Doctor_Dash profile or create one if it doesn't exist
    try:
        doctor_profile = Doctor_Dash.objects.get(user=request.user)
    except Doctor_Dash.DoesNotExist:
        # Create a profile with default settings
        doctor_profile = Doctor_Dash.objects.create(user=request.user)

    # --- 1. Handle Notification Settings Submission ---
    if request.method == 'POST':
        # Check if the POST request is specifically for saving settings
        # The HTML form will include a hidden field: <input type="hidden" name="action" value="save_settings">
        if request.POST.get('action') == 'save_settings':
            
            # Checkbox logic: A checkbox input is only present in request.POST if it was checked.
            # We explicitly check for existence to set the boolean fields.
            doctor_profile.receive_new_request_notif = 'new_request' in request.POST
            doctor_profile.receive_appointment_reminder = 'appointment_reminder' in request.POST
            doctor_profile.receive_message_alerts = 'message_alerts' in request.POST
            doctor_profile.receive_performance_report = 'performance_report' in request.POST
            
            doctor_profile.save()
            
            # Optional: Add Django success message here if used
            # messages.success(request, "Notification preferences saved successfully.")
            
            # Redirect to the same view to prevent form re-submission
            return redirect('doctor_dashboard')

    # --- 2. Retrieve Dashboard Data ---
    notifications = Notification.objects.filter(
        doctor=request.user,
        is_read=False
    ).order_by('-created_at')

    context = {
        'doctor': doctor_profile,
        'notifications': notifications,
        # 'doctor_profile' is now consistently passed as 'doctor' for settings and profile display
    }
    return render(request, 'doctors/doc_dash.html', context)


# -------------------------------
# Patient requests a prescription
@login_required
def request_prescription(request):
    if request.method == 'POST':
        form = PatientPrescriptionForm(request.POST)
        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.patient = request.user
            prescription.save()

            # Determine doctor to notify
            if prescription.doctor:
                doctor_user = prescription.doctor
            else:
                doctor_dash = Doctor_Dash.objects.first()
                if doctor_dash and hasattr(doctor_dash, 'user'):
                    doctor_user = doctor_dash.user
                else:
                    doctor_user = None

            # Create notification
            if doctor_user:
                Notification.objects.create(
                    doctor=doctor_user,
                    prescription=prescription,
                    text=f"{request.user.username} requested a prescription."
                )

            return redirect('request_sucess')
    else:
        form = PatientPrescriptionForm()

    return render(request, 'doctors/request_prescription.html', {'form': form})


# -------------------------------
# Request Success Page
@login_required
def request_success(request):
    return render(request, 'doctors/request_sucess.html')


# -------------------------------
# Doctor creates prescription manually or responds to request
@login_required
def create_prescription(request, prescription_id=None):
    if prescription_id:
        # Responding to existing patient request
        prescription = get_object_or_404(Prescription, id=prescription_id)
        if request.method == 'POST':
            form = PrescriptionForm(request.POST, instance=prescription)
            if form.is_valid():
                prescription = form.save(commit=False)
                prescription.doctor = request.user
                prescription.save()

                Notification.objects.create(
                    doctor=request.user,
                    prescription=prescription,
                    text=f"Prescription for {prescription.patient.username} is ready."
                )

                return redirect('doctor_dashboard')
        else:
            form = PrescriptionForm(instance=prescription)

        return render(request, 'doctors/prescription.html', {'form': form, 'prescription': prescription})

    else:
        # Creating a new prescription manually
        if request.method == 'POST':
            form = PrescriptionForm(request.POST)
            if form.is_valid():
                prescription = form.save(commit=False)
                prescription.doctor = request.user
                prescription.save()
                return redirect('doctor_dashboard')
        else:
            form = PrescriptionForm()

        return render(request, 'doctors/prescription.html', {'form': form})


# -------------------------------
# List of patient prescriptions
@login_required
def patient_prescriptions(request):
    prescriptions = Prescription.objects.filter(patient=request.user)
    return render(request, "doctors/request_prescriptions.html", {"prescriptions": prescriptions})


# -------------------------------
# Mark notification as read
@login_required
def mark_notification_read(request, pk):
    note = get_object_or_404(Notification, pk=pk, doctor=request.user)
    note.is_read = True
    note.save()
    return redirect('doctor_dashboard')