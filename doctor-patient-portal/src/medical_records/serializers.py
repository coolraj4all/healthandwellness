from rest_framework import serializers
from .models import PatientMedicalHistory, PatientSurgicalHistory, PatientHealthDetails, PatientMedicineDetails

class PatientMedicalHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientMedicalHistory
        fields = '__all__'

class PatientSurgicalHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientSurgicalHistory
        fields = '__all__'

class PatientHealthDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientHealthDetails
        fields = '__all__'
