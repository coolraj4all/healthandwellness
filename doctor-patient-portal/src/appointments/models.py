from django.db import models
from accounts.models import Patient, Doctor

class Appointment(models.Model):
    APPOINTMENT_STATUS = (
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('no_show', 'No Show'),
    )

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctor_appointments')
    appointment_date = models.DateTimeField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=APPOINTMENT_STATUS, default='scheduled')
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def can_cancel(self):
        return self.status == 'scheduled'

    def cancel_appointment(self):
        if self.can_cancel():
            self.status = 'cancelled'
            self.save()
            return True
        return False

    class Meta:
        ordering = ['-appointment_date']