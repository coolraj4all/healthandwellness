from django.shortcuts import render
from django.http import HttpResponse
from .models import Appointment
from django.views.generic import ListView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import AppointmentSerializer


class AppointmentViewSet(viewsets.ViewSet):
    def list(self, request):
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            appointment = Appointment.objects.get(pk=pk)
        except Appointment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            appointment = Appointment.objects.get(pk=pk)
        except Appointment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AppointmentSerializer(appointment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            appointment = Appointment.objects.get(pk=pk)
        except Appointment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# def appointment_list(request):
#     appointments = Appointment.objects.all()
#     return render(request, 'appointments/appointment_list.html', {'appointments': appointments})

# def appointment_detail(request, appointment_id):
#     appointment = Appointment.objects.get(id=appointment_id)
#     return render(request, 'appointments/appointment_detail.html', {'appointment': appointment})

# def create_appointment(request):
#     if request.method == 'POST':
#         # Logic to create an appointment
#         pass
#     return render(request, 'appointments/create_appointment.html')

# def update_appointment(request, appointment_id):
#     appointment = Appointment.objects.get(id=appointment_id)
#     if request.method == 'POST':
#         # Logic to update the appointment
#         pass
#     return render(request, 'appointments/update_appointment.html', {'appointment': appointment})

# def delete_appointment(request, appointment_id):
#     appointment = Appointment.objects.get(id=appointment_id)
#     if request.method == 'POST':
#         appointment.delete()
#         return HttpResponse('Appointment deleted.')
#     return render(request, 'appointments/delete_appointment.html', {'appointment': appointment})