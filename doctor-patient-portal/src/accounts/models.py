from django.db import models
from django.contrib.auth.models import AbstractUser
USER_TYPES = [
        ('Patient', 'Patient'), ('Doctor', 'Doctor'), ('Receptionist', 'Receptionist') ,('Admin', 'Admin'),
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
    BLOOD_GROUPS = [
        ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
        ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20, choices=GENDERS)
    phone = models.CharField(max_length=15)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)    
    date_of_birth = models.DateField()
    address = models.TextField()
    emergency_contact_name = models.CharField(max_length=100)
    emergency_contact_phone = models.CharField(max_length=15)
    is_user = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def convert_to_user(self, username, password):
        """
        Convert existing patient to a user account
        """
        if self.is_user:
            raise ValueError("Patient already has a user account")
        
        # Get or create patient user type
        patient_type, _ = UserTypes.objects.get_or_create(user_type='Patient')
        
        # Create new user
        user = User.objects.create_user(
            username=username,
            password=password,
            gender=self.gender,
            phone=self.phone,
            user_type=patient_type,
            first_name=self.first_name,
            last_name=self.last_name
        )
        
        # Link user to patient
        self.user = user
        self.is_user = True
        self.save()
        
        return user

    def __str__(self):
        return f"{self.user.username} - Patient"

class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20, choices=GENDERS)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    date_of_birth = models.DateField()
    emergency_contact_name = models.CharField(max_length=100)
    emergency_contact_phone = models.CharField(max_length=15)
    specialization = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50)
    is_user = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def convert_to_user(self, username, password):
        """
        Convert existing doctor to a user account
        """
        if self.is_user:
            raise ValueError("Doctor already has a user account")
        
        # Get or create doctor user type
        doctor_type, _ = UserTypes.objects.get_or_create(user_type='Doctor')
        
        # Create new user
        user = User.objects.create_user(
            username=username,
            password=password,
            gender=self.gender,
            phone=self.phone,
            user_type=doctor_type,
            first_name=self.first_name,
            last_name=self.last_name
        )
        
        # Link user to doctor
        self.user = user
        self.is_user = True
        self.save()
        
        return user

    def __str__(self):
        return f"{self.user.username} - Doctor"
    
class Receptionist(models.Model):    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20, choices=GENDERS)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    date_of_birth = models.DateField()
    emergency_contact_name = models.CharField(max_length=100)
    emergency_contact_phone = models.CharField(max_length=15)
    is_user = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def convert_to_user(self, username, password):
        """
        Convert existing receptionist to a user account
        """
        if self.is_user:
            raise ValueError("Receptionist already has a user account")
        
        # Get or create receptionist user type
        receptionist_type, _ = UserTypes.objects.get_or_create(user_type='Receptionist')
        
        # Create new user
        user = User.objects.create_user(
            username=username,
            password=password,
            gender=self.gender,
            phone=self.phone,
            user_type=receptionist_type,
            first_name=self.first_name,
            last_name=self.last_name
        )
        
        # Link user to receptionist
        self.user = user
        self.is_user = True
        self.save()
        
        return user

    def __str__(self):
        return f"{self.user.username} - Receptionist"