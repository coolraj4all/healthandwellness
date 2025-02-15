from datetime import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import Appointment
from accounts.models import Doctor, Patient
from django.contrib import messages
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import AppointmentSerializer
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

class AppointmentListView(LoginRequiredMixin, ListView):
    model = Appointment
    template_name = 'appointments/appointment_list.html'
    context_object_name = 'appointments'

    def get_queryset(self):
        return Appointment.objects.all().order_by('appointment_date')

class AppointmentCreateView(LoginRequiredMixin, CreateView):
    model = Appointment
    template_name = 'appointments/appointment_form.html'
    fields = ['doctor', 'appointment_date', 'reason', 'patient']
    success_url = reverse_lazy('appointments:appointment-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Book New Appointment'
        context['doctors'] = Doctor.objects.all()
        
        # Show patient field only for staff/doctor users
        if hasattr(self.request.user, 'doctor') or self.request.user.is_staff:
            context['show_patient_field'] = True
            context['patients'] = Patient.objects.all().order_by('user__first_name', 'user__last_name')
        elif hasattr(self.request.user, 'patient'):
            context['selected_patient'] = self.request.user.patient
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        if not (hasattr(self.request.user, 'doctor') or self.request.user.is_staff):
            # Hide patient field for regular users
            if 'patient' in form.fields:
                del form.fields['patient']
        return form

    def form_valid(self, form):
        if not (hasattr(self.request.user, 'doctor') or self.request.user.is_staff):
            # For regular users, set patient to their associated patient
            form.instance.patient = self.request.user.patient
        form.instance.status = 'scheduled'
        return super().form_valid(form)

class AppointmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Appointment
    template_name = 'appointments/appointment_form.html'
    fields = ['doctor', 'appointment_date', 'reason']
    success_url = reverse_lazy('appointments:appointment-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Edit Appointment'
        context['doctors'] = Doctor.objects.all()
        
        if hasattr(self.request.user, 'doctor') or self.request.user.is_staff:
            context['show_patient_field'] = True
            context['patients'] = Patient.objects.all().order_by('user__first_name', 'user__last_name')
        context['selected_patient'] = self.object.patient
        return context

    def get_queryset(self):
        queryset = Appointment.objects.filter(status='scheduled')
        if hasattr(self.request.user, 'patient'):
            # Filter by user's patient
            return queryset.filter(patient=self.request.user.patient)
        elif hasattr(self.request.user, 'doctor'):
            # Doctors can edit their appointments
            return queryset.filter(doctor=self.request.user.doctor)
        elif self.request.user.is_staff:
            # Staff can edit all appointments
            return queryset
        return Appointment.objects.none()

class AppointmentDetailView(LoginRequiredMixin, DetailView):
    model = Appointment
    template_name = 'appointments/appointment_detail.html'
    context_object_name = 'appointment'

    def get_queryset(self):
        queryset = Appointment.objects.all()
        if hasattr(self.request.user, 'patient'):
            # Show only user's patient appointments
            return queryset.filter(patient=self.request.user.patient)
        elif hasattr(self.request.user, 'doctor'):
            # Show doctor's appointments
            return queryset.filter(doctor=self.request.user.doctor)
        elif self.request.user.is_staff:
            # Staff can view all appointments
            return queryset
        return Appointment.objects.none()

class PatientAppointmentsView(LoginRequiredMixin, ListView):
    model = Appointment
    template_name = 'appointments/patient_appointments.html'
    context_object_name = 'appointments'

    def get_queryset(self):
        patient_id = self.kwargs.get('patient_id')
        if hasattr(self.request.user, 'doctor') or self.request.user.is_staff:
            return Appointment.objects.filter(patient_id=patient_id).order_by('-appointment_date')
        return Appointment.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        patient = get_object_or_404(Patient, id=self.kwargs.get('patient_id'))
        context['patient'] = patient
        return context

class PatientAppointmentCreateView(LoginRequiredMixin, CreateView):
    model = Appointment
    template_name = 'appointments/appointment_form.html'
    fields = ['patient', 'doctor', 'appointment_date', 'reason']
    
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.patient = get_object_or_404(Patient, id=self.kwargs['patient_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_patient_field'] = True
        context['patients'] = [self.patient]
        context['selected_patient'] = self.patient
        context['doctors'] = Doctor.objects.all()
        return context

    def form_valid(self, form):
        form.instance.status = 'scheduled'
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('appointments:patient-appointments', kwargs={'patient_id': self.patient.id})

class PatientAppointmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Appointment
    template_name = 'appointments/appointment_form.html'
    fields = ['doctor', 'appointment_date', 'reason']
    
    def dispatch(self, request, *args, **kwargs):
        if not (request.user.is_staff or hasattr(request.user, 'doctor')):
            return redirect('appointments:appointment-list')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('appointments:patient-appointments', 
                          kwargs={'patient_id': self.object.patient.id})
class PatientAppointmentDetailView(LoginRequiredMixin, DetailView):
    model = Appointment
    template_name = 'appointments/appointment_detail.html'
    context_object_name = 'appointment'

    def get_queryset(self):
        queryset = Appointment.objects.all()
        if hasattr(self.request.user, 'doctor') or self.request.user.is_staff:
            return queryset
        return queryset.filter(patient=self.request.user.patient)
    
def cancel_appointment(request, pk):
    # Update cancel_appointment view to handle staff/doctor cancellations
    if request.method == 'POST':
        if hasattr(request.user, 'patient'):
            appointment = get_object_or_404(Appointment, pk=pk, patient=request.user.patient)
        elif hasattr(request.user, 'doctor') or request.user.is_staff:
            appointment = get_object_or_404(Appointment, pk=pk)
        else:
            return JsonResponse({'status': 'error', 'message': 'Unauthorized'}, status=403)

        if appointment.cancel_appointment():
            messages.success(request, 'Appointment cancelled successfully.')
            return redirect('appointments:appointment-list')
        return JsonResponse({'status': 'error', 'message': 'Unable to cancel appointment'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

class DoctorAppointmentsView(LoginRequiredMixin, ListView):
    model = Appointment
    template_name = 'appointments/doctor_appointments.html'
    context_object_name = 'appointments'

    def get_queryset(self):
        doctor_id = self.kwargs.get('doctor_id')
        if self.request.user.is_staff or hasattr(self.request.user, 'doctor'):
            return Appointment.objects.filter(doctor_id=doctor_id).order_by('-appointment_date')
        return Appointment.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['doctor'] = get_object_or_404(Doctor, id=self.kwargs.get('doctor_id'))
        return context


