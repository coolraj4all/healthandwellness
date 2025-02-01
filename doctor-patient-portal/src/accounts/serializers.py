from rest_framework import serializers
from .models import User, Patient, Doctor, Receptionist, UserTypes

class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTypes
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'user_type', 'gender', 'phone']
        extra_kwargs = {'password': {'write_only': True}}

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class ReceptionistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receptionist
        fields = '__all__'
