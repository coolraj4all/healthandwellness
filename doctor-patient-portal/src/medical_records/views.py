from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.views.generic import ListView
from .models import PatientMedicalHistory, PatientSurgicalHistory, PatientHealthDetails, PatientMedicineDetails
from .serializers import PatientMedicalHistorySerializer, PatientSurgicalHistorySerializer, PatientHealthDetailsSerializer
from accounts.models import Patient
from appointments.models import Appointment

class PatientMedicalHistoryViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = PatientMedicalHistory.objects.all()
        serializer = PatientMedicalHistorySerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PatientMedicalHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            instance = PatientMedicalHistory.objects.get(pk=pk)
        except PatientMedicalHistory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PatientMedicalHistorySerializer(instance)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            instance = PatientMedicalHistory.objects.get(pk=pk)
        except PatientMedicalHistory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PatientMedicalHistorySerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            instance = PatientMedicalHistory.objects.get(pk=pk)
        except PatientMedicalHistory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PatientSurgicalHistoryViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = PatientSurgicalHistory.objects.all()
        serializer = PatientSurgicalHistorySerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PatientSurgicalHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            instance = PatientSurgicalHistory.objects.get(pk=pk)
        except PatientSurgicalHistory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PatientSurgicalHistorySerializer(instance)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            instance = PatientSurgicalHistory.objects.get(pk=pk)
        except PatientSurgicalHistory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PatientSurgicalHistorySerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            instance = PatientSurgicalHistory.objects.get(pk=pk)
        except PatientSurgicalHistory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PatientMedicationViewSet(viewsets.ViewSet):
    template_name = 'medical_records/patient_health_list.html'
    form_template_name = 'medical_records/patient_health_form.html'

    def list(self, request):
        queryset = PatientHealthDetails.objects.all()
        return render(request, self.template_name, {
            'health_records': queryset
        })

    def create(self, request):
        if request.method == 'GET':
            # Get appointment and patient IDs from query parameters
            appointment_id = request.GET.get('appointment')
            patient_id = request.GET.get('patient')
            
            appointment = None
            patient = None
            
            if appointment_id:
                appointment = get_object_or_404(Appointment, id=appointment_id)
            if patient_id:
                patient = get_object_or_404(Patient, id=patient_id)
            health_record = PatientHealthDetails(
                patient=patient,
                appointment=appointment
            ) if patient or appointment else PatientHealthDetails()
            context = {
                'patients': Patient.objects.all(),
                'appointments': Appointment.objects.all(),
                'selected_appointment': appointment,
                'selected_patient': patient,
                'diet_choices': PatientHealthDetails.DIET_CHOICES,
                'health_record': health_record
                
            }
            return render(request, self.form_template_name, context)

        # For POST requests
        serializer = PatientHealthDetailsSerializer(data=request.POST,partial = True)
        if serializer.is_valid():
            record = serializer.save()
            return redirect('appointments:appointment-list')
        
        context = {
            'patients': Patient.objects.all(),
            'appointments': Appointment.objects.all(),
            'errors': serializer.errors,
            'form_data': request.POST  # Preserve form data on error
        }
        return render(request, self.form_template_name, context)

    def retrieve(self, request, pk=None):
        instance = get_object_or_404(PatientHealthDetails, pk=pk)
        return render(request, self.form_template_name, {
            'health_record': instance,
            'patients': Patient.objects.all(),
            'appointments': Appointment.objects.all(),
            'diet_choices': PatientHealthDetails.DIET_CHOICES
        })

    def update(self, request, pk=None):
        instance = get_object_or_404(PatientHealthDetails, pk=pk)
        
        if request.method == 'GET':
            return render(request, self.form_template_name, {
                'health_record': instance,
                'patients': Patient.objects.all(),
                'appointments': Appointment.objects.all(),
            })

        serializer = PatientHealthDetailsSerializer(instance, data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('appointments:appointment-list')
        
        context = {
            'health_record': instance,
            'patients': Patient.objects.all(),
            'appointments': Appointment.objects.all(),
            'errors': serializer.errors
        }
        return render(request, self.form_template_name, context)

    def destroy(self, request, pk=None):
        instance = get_object_or_404(PatientHealthDetails, pk=pk)
        instance.delete()
        return redirect('records:patient-health-list')


