from io import BytesIO
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.views.generic import ListView
from .models import PatientMedicalHistory, PatientSurgicalHistory, PatientHealthDetails, PatientMedicineDetails
from .serializers import PatientMedicalHistorySerializer, PatientSurgicalHistorySerializer, PatientHealthDetailsSerializer
from accounts.models import Patient
from appointments.models import Appointment
from medicines.models import Medicine
from django.urls import reverse
from django.shortcuts import get_object_or_404
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm, mm, inch
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from datetime import datetime
from rest_framework.decorators import action
from medical_records.utils import generate_prescription_pdf

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
    
    @action(detail=True, methods=['get'])
    def generate_pdf(self, request, pk=None):
        """
        Generate and return a prescription PDF for the specified health record.
        """
        health_record = get_object_or_404(PatientHealthDetails, pk=pk)
        
        # Generate the PDF
        pdf_content = generate_prescription_pdf(health_record)
        
        # Create the HTTP response with PDF content
        response = HttpResponse(pdf_content, content_type='application/pdf')
        
        # Set the Content-Disposition header to make the browser download the file
        patient_name = f"{health_record.patient.first_name}_{health_record.patient.last_name}" if hasattr(health_record.patient, 'first_name') else "patient"
        appointment_date = health_record.appointment.appointment_date.strftime('%Y%m%d') if hasattr(health_record.appointment, 'appointment_date') else "date"
        filename = f"prescription_{patient_name}_{appointment_date}.pdf"
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        
        return response

class PatientMedicineDetailsViewSet(viewsets.ViewSet):
    template_name = 'medical_records/medicine_details_list.html'
    form_template_name = 'medical_records/medicine_details_form.html'

    def list(self, request):
        health_record_id = request.GET.get('health_record')
        if health_record_id:
            queryset = PatientMedicineDetails.objects.filter(patientHealthDetails_id=health_record_id)
        else:
            queryset = PatientMedicineDetails.objects.all()
        return render(request, self.template_name, {
            'medicine_details': queryset,
            'health_record_id': health_record_id
        })

    def create(self, request):
        if request.method == 'GET':
            health_record_id = request.GET.get('health_record')
            health_record = get_object_or_404(PatientHealthDetails, id=health_record_id)
            context = {
                'health_record': health_record,
                'medicines': Medicine.objects.all(),
            }
            return render(request, self.form_template_name, context)

        # Handle multiple medicine forms
        health_record_id = request.POST.get('health_record')
        created_records = []
        
        # Group form fields by medicine
        medicine_forms = {}
        for key, value in request.POST.items():
            if key == 'csrfmiddlewaretoken' or key == 'health_record':
                continue
            # Split the field name to get the base name and form number
            parts = key.split('_')
            if len(parts) > 1 and parts[-1].isdigit():
                form_num = parts[-1]
                base_name = '_'.join(parts[:-1])
            else:
                form_num = '0'
                base_name = key
                
            if form_num not in medicine_forms:
                medicine_forms[form_num] = {}
            medicine_forms[form_num][base_name] = value

        # Create medicine details for each form
        for form_data in medicine_forms.values():
            if not form_data.get('medicine'):  # Skip if no medicine selected
                continue
                
            medicine_details = PatientMedicineDetails(
                patientHealthDetails_id=health_record_id,
                medicine_id=form_data.get('medicine'),
                dosage=form_data.get('dosage'),
                morning_before_meal=form_data.get('morning_before_meal') == 'on',
                morning_after_meal=form_data.get('morning_after_meal') == 'on',
                afternoon_before_meal=form_data.get('afternoon_before_meal') == 'on',
                afternoon_after_meal=form_data.get('afternoon_after_meal') == 'on',
                evening_before_meal=form_data.get('evening_before_meal') == 'on',
                evening_after_meal=form_data.get('evening_after_meal') == 'on',
                night_before_meal=form_data.get('night_before_meal') == 'on',
                night_after_meal=form_data.get('night_after_meal') == 'on',
                days=form_data.get('days')
            )
            medicine_details.save()
            created_records.append(medicine_details)

        # After creating all medicine details
        base_url = reverse('records:patient-health-update', kwargs={'pk': health_record_id})
        return redirect(f'{base_url}')

    def update(self, request, pk=None):
        instance = get_object_or_404(PatientMedicineDetails, pk=pk)
        
        if request.method == 'GET':
            context = {
                'medicine_detail': instance,
                'medicines': Medicine.objects.all(),
                'health_record': instance.patientHealthDetails
            }
            return render(request, self.form_template_name, context)

        instance.medicine_id = request.POST.get('medicine')
        instance.dosage = request.POST.get('dosage')
        instance.morning_before_meal = request.POST.get('morning_before_meal') == 'on'
        instance.morning_after_meal = request.POST.get('morning_after_meal') == 'on'
        instance.afternoon_before_meal = request.POST.get('afternoon_before_meal') == 'on'
        instance.afternoon_after_meal = request.POST.get('afternoon_after_meal') == 'on'
        instance.evening_before_meal = request.POST.get('evening_before_meal') == 'on'
        instance.evening_after_meal = request.POST.get('evening_after_meal') == 'on'
        instance.night_before_meal = request.POST.get('night_before_meal') == 'on'
        instance.night_after_meal = request.POST.get('night_after_meal') == 'on'
        instance.days = request.POST.get('days')
        instance.save()
        
        base_url = reverse('records:medicine-details-list')
        return redirect(f'{base_url}?health_record={instance.patientHealthDetails_id}')

    def destroy(self, request, pk=None):
        instance = get_object_or_404(PatientMedicineDetails, pk=pk)
        health_record_id = instance.patientHealthDetails_id
        instance.delete()
        base_url = reverse('records:medicine-details-list')
        return redirect(f'{base_url}?health_record={health_record_id}')


