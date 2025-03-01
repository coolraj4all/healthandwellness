from django.db import models
from accounts.models import Patient
from appointments.models import Appointment
from medicines.models import Medicine

class PatientMedicalHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_histories')
    condition_name = models.CharField(max_length=200)
    diagnosis_date = models.DateField()
    current_status = models.CharField(max_length=100)
    treatment = models.TextField()
    notes = models.TextField(blank=True)

class PatientSurgicalHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='surgical_histories')
    surgery_name = models.CharField(max_length=200)
    surgery_date = models.DateField()
    hospital = models.CharField(max_length=200)
    surgeon = models.CharField(max_length=200)
    description = models.TextField()
    complications = models.TextField(blank=True)
    recovery_notes = models.TextField(blank=True)


class PatientHealthDetails(models.Model):
    DIET_CHOICES = [
        ('VEG', 'Vegetarian'),
        ('NON_VEG', 'Non-vegetarian'),
        ('VEGAN', 'Vegan'),
        ('OTHER', 'Other')
    ]
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, related_name='health_details')
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, related_name='appointment_details')
    height = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    bmi = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    allergies = models.TextField(blank=True,null=True)
    addictions = models.TextField(blank=True,null=True)
    diet = models.TextField(blank=True,choices=DIET_CHOICES,null=True)
    sleep_hours = models.DecimalField(max_digits=3, decimal_places=1,blank=True,null=True)
    comorbidities = models.TextField(blank=True,null=True)
    temperature = models.DecimalField(max_digits=5, decimal_places=2,blank=True,null=True)
    heart_rate = models.DecimalField(max_digits=5, decimal_places=2,blank=True,null=True)
    blood_pressure = models.CharField(max_length=20,blank=True,null=True)
    rr = models.DecimalField(max_digits=5, decimal_places=2,blank=True,null=True)
    spo2 = models.DecimalField(max_digits=5, decimal_places=2,blank=True,null=True)
    rs = models.CharField(max_length=20,blank=True,null=True)
    cvs = models.CharField(max_length=20,blank=True,null=True)
    p_a = models.CharField(max_length=20,blank=True,null=True)
    cns = models.CharField(max_length=20,blank=True,null=True)
    presenting_complaints = models.TextField(blank=True,null=True)
    provisional_diagnosis = models.TextField(blank=True,null=True)
    medicines = models.ManyToManyField(Medicine, through='PatientMedicineDetails', related_name='medicines')
    investigation_advice = models.TextField(blank=True,null=True)
    diet_advice = models.TextField(blank=True,null=True)
    follow_up_date = models.DateField(blank=True,null=True)


class PatientMedicineDetails(models.Model):
    patientHealthDetails = models.ForeignKey(PatientHealthDetails, on_delete=models.CASCADE, related_name='medicine_details')
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    dosage = models.CharField(max_length=100)
    morning_before_meal = models.BooleanField(default=False)
    morning_after_meal = models.BooleanField(default=False)
    afternoon_before_meal = models.BooleanField(default=False)
    afternoon_after_meal = models.BooleanField(default=False)
    evening_before_meal = models.BooleanField(default=False)
    evening_after_meal = models.BooleanField(default=False)
    night_before_meal = models.BooleanField(default=False)
    night_after_meal = models.BooleanField(default=False)
    days = models.PositiveIntegerField()


