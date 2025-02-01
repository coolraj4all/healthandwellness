from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Disease, DiseaseCategory
from .serializers import DiseaseSerializer, DiseaseCategorySerializer

class DiseaseCategoryViewSet(viewsets.ViewSet):
    def list(self, request):
        categories = DiseaseCategory.objects.all()
        serializer = DiseaseCategorySerializer(categories, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = DiseaseCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            category = DiseaseCategory.objects.get(pk=pk)
        except DiseaseCategory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DiseaseCategorySerializer(category)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            category = DiseaseCategory.objects.get(pk=pk)
        except DiseaseCategory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DiseaseCategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            category = DiseaseCategory.objects.get(pk=pk)
        except DiseaseCategory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DiseaseViewSet(viewsets.ViewSet):
    def list(self, request):
        diseases = Disease.objects.all()
        serializer = DiseaseSerializer(diseases, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = DiseaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            disease = Disease.objects.get(pk=pk)
        except Disease.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DiseaseSerializer(disease)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            disease = Disease.objects.get(pk=pk)
        except Disease.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DiseaseSerializer(disease, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            disease = Disease.objects.get(pk=pk)
        except Disease.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        disease.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
