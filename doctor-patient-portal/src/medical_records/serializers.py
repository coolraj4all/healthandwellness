from rest_framework import serializers
from .models import PatientMedicalHistory, PatientSurgicalHistory, PatientMedication

class PatientMedicalHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientMedicalHistory
        fields = '__all__'

class PatientSurgicalHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientSurgicalHistory
        fields = '__all__'

class PatientMedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientMedication
        fields = '__all__'
