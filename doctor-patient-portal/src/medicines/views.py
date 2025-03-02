from django.http import JsonResponse
from django.shortcuts import render, redirect,get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.urls import reverse
from .models import Manufacturer, Medicine, Brand, MedicineRecommendation
from .serializers import ManufacturerSerializer, MedicineSerializer, BrandSerializer, MedicineRecommendationSerializer
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .form import BrandForm
from django.db.models import Q
from diseases.models import Disease

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

class ManufacturerListView(ListView):
    model = Manufacturer
    context_object_name = 'manufacturers'
    template_name = 'medicines/manufacturer_list.html'
    paginate_by = 10  # Add this line

    def get_queryset(self):
        queryset = Manufacturer.objects.all()
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        return context

class ManufacturerCreateView(CreateView):
    model = Manufacturer
    fields = ['name', 'description', 'website', 'country']
    template_name = 'medicines/manufacturer_form.html'
    success_url = reverse_lazy('medicines:manufacturer-list')

class ManufacturerUpdateView(UpdateView):
    model = Manufacturer
    fields = ['name', 'description', 'website', 'country']
    template_name = 'medicines/manufacturer_form.html'
    success_url = reverse_lazy('medicines:manufacturer-list')

class ManufacturerDetailView(DetailView):
    model = Manufacturer
    template_name = 'medicines/manufacturer_detail.html'

class ManufacturerDeleteView(DeleteView):
    model = Manufacturer
    template_name = 'medicines/manufacturer_confirm_delete.html'
    success_url = reverse_lazy('medicines:manufacturer-list')

class MedicineListView(ListView):
    model = Medicine
    context_object_name = 'medicines'
    template_name = 'medicines/medicine_list.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = Medicine.objects.all()
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        return context

class MedicineCreateView(CreateView):
    model = Medicine
    fields = ['name', 'generic_name', 'form', 'strength', 'description', 'composition', 
              'manufacturer', 'storage_instructions', 'side_effects', 'precautions', 
              'price', 'requires_prescription']
    template_name = 'medicines/medicine_form.html'
    success_url = reverse_lazy('medicines:medicine-list')

class MedicineUpdateView(UpdateView):
    model = Medicine
    fields = ['name', 'generic_name', 'form', 'strength', 'description', 'composition', 
              'manufacturer', 'storage_instructions', 'side_effects', 'precautions', 
              'price', 'requires_prescription']
    template_name = 'medicines/medicine_form.html'
    success_url = reverse_lazy('medicines:medicine-list')

class MedicineDetailView(DetailView):
    model = Medicine
    template_name = 'medicines/medicine_detail.html'

class MedicineDeleteView(DeleteView):
    model = Medicine
    template_name = 'medicines/medicine_confirm_delete.html'
    success_url = reverse_lazy('medicines:medicine-list')

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

class BrandListView(ListView):
    model = Brand
    context_object_name = 'brands'
    template_name = 'medicines/brand_list.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = Brand.objects.all()
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        return context

class BrandCreateView(CreateView):
    model = Brand
    form_class = BrandForm
    template_name = 'medicines/brand_form.html'
    success_url = reverse_lazy('medicines:brand-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['manufacturers'] = Manufacturer.objects.all()
        context['medicines'] = Medicine.objects.all()
        return context

class BrandUpdateView(UpdateView):
    model = Brand
    form_class = BrandForm
    template_name = 'medicines/brand_form.html'
    success_url = reverse_lazy('medicines:brand-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['manufacturers'] = Manufacturer.objects.all()
        context['medicines'] = Medicine.objects.all()
        return context

class BrandDetailView(DetailView):
    model = Brand
    template_name = 'medicines/brand_detail.html'

class BrandDeleteView(DeleteView):
    model = Brand
    template_name = 'medicines/brand_confirm_delete.html'
    success_url = reverse_lazy('medicines:brand-list')

class MedicineRecommendationListView(ListView):
    model = MedicineRecommendation
    context_object_name = 'recommendations'
    template_name = 'medicines/recommendation_list.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = MedicineRecommendation.objects.all()
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(
                Q(disease__name__icontains=search_query) |
                Q(medicine__name__icontains=search_query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        return context

class MedicineRecommendationCreateView(CreateView):
    model = MedicineRecommendation
    fields = ['disease', 'medicine', 'special_instructions', 'contraindications', 'effectiveness_rating']
    template_name = 'medicines/recommendation_form.html'
    success_url = reverse_lazy('medicines:recommendation-list')

class MedicineRecommendationUpdateView(UpdateView):
    model = MedicineRecommendation
    fields = ['disease', 'medicine', 'special_instructions', 'contraindications', 'effectiveness_rating']
    template_name = 'medicines/recommendation_form.html'
    success_url = reverse_lazy('medicines:recommendation-list')

class MedicineRecommendationDetailView(DetailView):
    model = MedicineRecommendation
    template_name = 'medicines/recommendation_detail.html'

class MedicineRecommendationDeleteView(DeleteView):
    model = MedicineRecommendation
    template_name = 'medicines/recommendation_confirm_delete.html'
    success_url = reverse_lazy('medicines:recommendation-list')

def search_medicines(request):
    search_query = request.GET.get('search', '')
    search_query = f"%{search_query}%"
    medicines_list = []
    
    if search_query:
        # Update the disease filter to use case-insensitive contains lookup
        # This is equivalent to SELECT * FROM public.diseases_disease where symptoms like '%Cough%'
        diseases = Disease.objects.filter(symptoms__icontains=search_query.strip('%'))
        
        # Get medicine recommendations for found diseases
        medicine_recommendations = MedicineRecommendation.objects.filter(
            disease__in=diseases
        ).select_related('disease')

        # Get medicines for found recommendations
        for recommendation in medicine_recommendations:
            medicines_list.append(recommendation.medicine)   
    # Convert medicines list to a list of dictionaries
    medicines_data = [
        {
            'id': medicine.id,
            'name': medicine.name,
            'form': medicine.form,
            'strength': medicine.strength,
            'composition': medicine.composition,
            'manufacturer': medicine.manufacturer.name  # Convert decimal to string for JSON
        }
        for medicine in medicines_list
    ]

    return JsonResponse({'medicines': medicines_data}, safe=False)
