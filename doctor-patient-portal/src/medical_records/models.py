from django.db import models
from accounts.models import Patient

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

class PatientMedication(models.Model):
    FREQUENCY_CHOICES = [
        ('ONCE', 'Once daily'),
        ('TWICE', 'Twice daily'),
        ('THRICE', 'Thrice daily'),
        ('FOUR', 'Four times daily'),
        ('AS_NEEDED', 'As needed'),
        ('OTHER', 'Other')
    ]
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medications')
    name = models.CharField(max_length=200)
    dosage = models.CharField(max_length=100)
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    prescribing_doctor = models.CharField(max_length=200)
    reason = models.TextField()
    side_effects = models.TextField(blank=True)
    notes = models.TextField(blank=True)