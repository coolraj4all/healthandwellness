from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import PatientMedicalHistory, PatientSurgicalHistory, PatientMedication
from .serializers import PatientMedicalHistorySerializer, PatientSurgicalHistorySerializer, PatientMedicationSerializer

class PatientMedicalHistoryViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = PatientMedicalHistory.objects.all()
        serializer = PatientMedicalHistorySerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PatientMedicalHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            instance = PatientMedicalHistory.objects.get(pk=pk)
        except PatientMedicalHistory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PatientMedicalHistorySerializer(instance)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            instance = PatientMedicalHistory.objects.get(pk=pk)
        except PatientMedicalHistory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PatientMedicalHistorySerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            instance = PatientMedicalHistory.objects.get(pk=pk)
        except PatientMedicalHistory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PatientSurgicalHistoryViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = PatientSurgicalHistory.objects.all()
        serializer = PatientSurgicalHistorySerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PatientSurgicalHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            instance = PatientSurgicalHistory.objects.get(pk=pk)
        except PatientSurgicalHistory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PatientSurgicalHistorySerializer(instance)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            instance = PatientSurgicalHistory.objects.get(pk=pk)
        except PatientSurgicalHistory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PatientSurgicalHistorySerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            instance = PatientSurgicalHistory.objects.get(pk=pk)
        except PatientSurgicalHistory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PatientMedicationViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = PatientMedication.objects.all()
        serializer = PatientMedicationSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PatientMedicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            instance = PatientMedication.objects.get(pk=pk)
        except PatientMedication.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PatientMedicationSerializer(instance)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            instance = PatientMedication.objects.get(pk=pk)
        except PatientMedication.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PatientMedicationSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            instance = PatientMedication.objects.get(pk=pk)
        except PatientMedication.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


