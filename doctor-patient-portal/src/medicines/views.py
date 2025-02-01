from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Manufacturer, Medicine, Brand, MedicineRecommendation
from .serializers import ManufacturerSerializer, MedicineSerializer, BrandSerializer, MedicineRecommendationSerializer

class ManufacturerViewSet(viewsets.ViewSet):
    def list(self, request):
        manufacturers = Manufacturer.objects.all()
        serializer = ManufacturerSerializer(manufacturers, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ManufacturerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            manufacturer = Manufacturer.objects.get(pk=pk)
        except Manufacturer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ManufacturerSerializer(manufacturer)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            manufacturer = Manufacturer.objects.get(pk=pk)
        except Manufacturer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ManufacturerSerializer(manufacturer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            manufacturer = Manufacturer.objects.get(pk=pk)
        except Manufacturer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        manufacturer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MedicineViewSet(viewsets.ViewSet):
    def list(self, request):
        medicines = Medicine.objects.all()
        serializer = MedicineSerializer(medicines, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = MedicineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            medicine = Medicine.objects.get(pk=pk)
        except Medicine.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MedicineSerializer(medicine)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            medicine = Medicine.objects.get(pk=pk)
        except Medicine.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MedicineSerializer(medicine, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            medicine = Medicine.objects.get(pk=pk)
        except Medicine.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        medicine.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BrandViewSet(viewsets.ViewSet):
    def list(self, request):
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            brand = Brand.objects.get(pk=pk)
        except Brand.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BrandSerializer(brand)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            brand = Brand.objects.get(pk=pk)
        except Brand.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BrandSerializer(brand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            brand = Brand.objects.get(pk=pk)
        except Brand.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        brand.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MedicineRecommendationViewSet(viewsets.ViewSet):
    def list(self, request):
        recommendations = MedicineRecommendation.objects.all()
        serializer = MedicineRecommendationSerializer(recommendations, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = MedicineRecommendationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            recommendation = MedicineRecommendation.objects.get(pk=pk)
        except MedicineRecommendation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MedicineRecommendationSerializer(recommendation)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            recommendation = MedicineRecommendation.objects.get(pk=pk)
        except MedicineRecommendation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MedicineRecommendationSerializer(recommendation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            recommendation = MedicineRecommendation.objects.get(pk=pk)
        except MedicineRecommendation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        recommendation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
