from django.shortcuts import redirect, render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Disease, DiseaseCategory
from .serializers import DiseaseSerializer, DiseaseCategorySerializer
from .forms import DiseaseCategoryForm
from django.core.paginator import Paginator
from django.db.models import Q

class DiseaseCategoryViewSet(viewsets.ViewSet):
    model = DiseaseCategory
    form_class = DiseaseCategoryForm
    
    def list(self, request):
        categories_list = DiseaseCategory.objects.all()
        search_query = request.GET.get('search', '')
        
        if search_query:
            categories_list = categories_list.filter(
                name__icontains=search_query
            )
            
        paginator = Paginator(categories_list, 10)
        page = request.GET.get('page')
        categories = paginator.get_page(page)
        return render(request, 'diseases/category_list.html', {
            'categories': categories,
            'search_query': search_query
        })

    def create(self, request):
        if request.method == 'POST':
            form = DiseaseCategoryForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('diseases:category-list')
        else:
            categories = DiseaseCategory.objects.all()
            form = DiseaseCategoryForm()
            context = {
                'form': form,
                'categories': categories
            }   
        return render(request, 'diseases/category_form.html', context)

    def retrieve(self, request, pk=None):
        category = get_object_or_404(DiseaseCategory, pk=pk)
        return render(request, 'diseases/category_detail.html', {'category': category})

    def update(self, request, pk=None):
        category = get_object_or_404(DiseaseCategory, pk=pk)
        if request.method == 'POST':
            form = DiseaseCategoryForm(request.POST, instance=category)
            if form.is_valid():
                form.save()
                return redirect('diseases:category-list')
        else:
            form = DiseaseCategoryForm(instance=category)
            categories = DiseaseCategory.objects.all()

        return render(request, 'diseases/category_form.html', {
            'form': form,
            'category': category,
            'categories': categories
        })

    def destroy(self, request, pk=None):
        category = get_object_or_404(DiseaseCategory, pk=pk)
        if request.method == 'POST':
            category.delete()
            return redirect('diseases:category-list')
        return render(request, 'diseases/category_confirm_delete.html', {'category': category})

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
