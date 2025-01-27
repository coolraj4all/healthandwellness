from django.db import models
from django.contrib.auth.models import AbstractUser

class UserTypes(models.Model):
    user_type = models.CharField(max_length=50)
    user_type_abbr = models.CharField(max_length=10)
    def __str__(self):
        return self.user_type   


class User(AbstractUser):
    # Additional fields for user information can be added here
    user_type = models.ForeignKey(UserTypes, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.username

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    BLOOD_GROUPS = [
        ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
        ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-'),
    ]
    
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
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

    def __str__(self):
        return f"{self.user.username} - Doctor"