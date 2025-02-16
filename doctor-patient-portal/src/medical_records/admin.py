from django.contrib import admin
from .models import PatientMedicalHistory, PatientHealthDetails, PatientSurgicalHistory

admin.site.register(PatientMedicalHistory)
admin.site.register(PatientHealthDetails)
admin.site.register(PatientSurgicalHistory)