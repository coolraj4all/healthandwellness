from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.shortcuts import redirect
from django.contrib.auth.views import PasswordResetView
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib import messages
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import (UserSerializer, PatientSerializer, 
                        DoctorSerializer, ReceptionistSerializer, UserTypeSerializer)
from .models import User, Patient, Doctor, Receptionist, UserTypes
from .forms import UserRegistrationForm, PatientForm, DoctorForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import ProfileEditForm, PasswordChangeCustomForm

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('accounts:home')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accounts:home')  # Redirect to a success page or home
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('accounts:home')  # Redirect to a success page or home

def profile(request):
    return render(request, 'accounts/profile.html')

def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(
                request=request,
                from_email='noreply@yourwebsite.com',
                email_template_name='accounts/password_reset_email.html',
                subject_template_name='accounts/password_reset_subject.txt'
            )
            messages.success(request, 'Password reset email has been sent.')
            return redirect('login')
    else:
        form = PasswordResetForm()
    return render(request, 'accounts/password_reset.html', {'form': form})

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('accounts:profile')
    else:
        form = ProfileEditForm(instance=request.user)
    return render(request, 'accounts/profile_edit.html', {'form': form})

@login_required
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeCustomForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('accounts:profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeCustomForm(request.user)
    return render(request, 'accounts/password_change.html', {'form': form})

def patient_list(request):
    search_query = request.GET.get('search', '')
    patient_list = Patient.objects.all()
    
    if search_query:
        patient_list = patient_list.filter(
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query)
        )
    
    paginator = Paginator(patient_list, 10)
    page_number = request.GET.get('page')
    patients = paginator.get_page(page_number)
    
    context = {
        'patients': patients,
        'search_query': search_query,
    }
    return render(request, 'accounts/patients/patient_list.html', context)

def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, 'accounts/patients/patient_detail.html', {'patient': patient})

def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save()
            return redirect('accounts:patient-detail', pk=patient.pk)
    else:
        form = PatientForm()
    return render(request, 'accounts/patients/patient_form.html', {'form': form, 'title': 'Add Patient'})

def patient_edit(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            patient = form.save()
            return redirect('accounts:patient-detail', pk=patient.pk)
    else:
        form = PatientForm(instance=patient)
    return render(request, 'accounts/patients/patient_form.html', {'form': form, 'title': 'Edit Patient'})

def doctor_list(request):
    doctor_list = Doctor.objects.all()
    paginator = Paginator(doctor_list, 10)  # Show 10 doctors per page
    page_number = request.GET.get('page')
    doctors = paginator.get_page(page_number)
    return render(request, 'accounts/doctors/doctor_list.html', {'doctors': doctors})

def doctor_detail(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    return render(request, 'accounts/doctors/doctor_detail.html', {'doctor': doctor})

def doctor_create(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            doctor = form.save()
            return redirect('accounts:doctor-detail', pk=doctor.pk)
    else:
        form = DoctorForm()
    return render(request, 'accounts/doctors/doctor_form.html', {'form': form, 'title': 'Add Doctor'})

def doctor_edit(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            doctor = form.save()
            return redirect('accounts:doctor-detail', pk=doctor.pk)
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'accounts/doctors/doctor_form.html', {'form': form, 'title': 'Edit Doctor'})

def doctor_delete(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('accounts:doctor-list')
    return render(request, 'accounts/doctors/doctor_confirm_delete.html', {'doctor': doctor})

def doctor_to_user(request, pk):
    if request.method == 'POST':
        doctor = get_object_or_404(Doctor, pk=pk)
        if doctor.is_user:
            messages.error(request, 'This doctor already has a user account.')
            return redirect('accounts:doctor-list')
        
        try:
            # Generate username from first name and last name
            username = f"{doctor.first_name.lower()}.{doctor.last_name.lower()}"
            # Generate a random password
            from django.utils.crypto import get_random_string
            password = get_random_string(length=12)
            
            # Convert doctor to user
            user = doctor.convert_to_user(username=username, password=password)
            
            messages.success(
                request,
                f'User account created successfully. Username: {username}, Password: {password}'
            )
        except Exception as e:
            messages.error(request, f'Error creating user account: {str(e)}')
        
        return redirect('accounts:doctor-list')
    return redirect('accounts:doctor-list')

@login_required
def user_list(request):
    if not request.user.user_type.user_type == 'Admin':
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('accounts:home')
    
    search_query = request.GET.get('search', '')
    user_list = User.objects.all()
    
    if search_query:
        user_list = user_list.filter(
            Q(username__icontains=search_query) |
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query)
        )
    
    paginator = Paginator(user_list, 10)
    page_number = request.GET.get('page')
    users = paginator.get_page(page_number)
    
    return render(request, 'accounts/users/user_list.html', {
        'users': users,
        'search_query': search_query
    })

@login_required
def change_user_password(request, user_id):
    if not request.user.user_type.user_type == 'Admin':
        messages.error(request, 'You do not have permission to perform this action.')
        return redirect('accounts:home')
    
    user = get_object_or_404(User, id=user_id)
    
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        if new_password:
            user.set_password(new_password)
            user.save()
            messages.success(request, f'Password changed successfully for user {user.username}')
        else:
            messages.error(request, 'Please provide a new password')
    
    return redirect('accounts:user-list')

class UserTypeViewSet(viewsets.ModelViewSet):
    queryset = UserTypes.objects.all()
    serializer_class = UserTypeSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


