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