from django.contrib import admin
from .models import PatientMedicalHistory, PatientMedication, PatientSurgicalHistory

admin.site.register(PatientMedicalHistory)
admin.site.register(PatientMedication)
admin.site.register(PatientSurgicalHistory)