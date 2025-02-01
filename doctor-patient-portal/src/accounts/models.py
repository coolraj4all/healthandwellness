from django.db import models
from django.contrib.auth.models import AbstractUser
USER_TYPES = [
        ('Patient', 'Patient'), ('Doctor', 'Doctor'), ('Reciptionist', 'Reciptionist'),
    ]
GENDERS = [
        ('Male','Male'), ('Female','Female'), ('Other','Other')
    ]
class UserTypes(models.Model):
    user_type = models.CharField(max_length=50, choices=USER_TYPES)
    def __str__(self):
        return self.user_type   


class User(AbstractUser):
    # Additional fields for user information can be added here
    user_type = models.ForeignKey(UserTypes, on_delete=models.CASCADE, default=None, null=True)
    gender = models.CharField(max_length=20, choices=GENDERS)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.username

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    BLOOD_GROUPS = [
        ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
        ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-'),
    ]
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)    
    date_of_birth = models.DateField()
    address = models.TextField()
    emergency_contact_name = models.CharField(max_length=100)
    emergency_contact_phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - Patient"

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - Doctor"
    
class Reciptionist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    emergency_contact_name = models.CharField(max_length=100)
    emergency_contact_phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - Reciptionist"