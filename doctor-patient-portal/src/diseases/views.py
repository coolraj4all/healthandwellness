from django.shortcuts import redirect, render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Disease, DiseaseCategory
from .serializers import DiseaseSerializer, DiseaseCategorySerializer
from .forms import DiseaseCategoryForm, DiseaseForm  # Add DiseaseForm here
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
        diseases_list = Disease.objects.all()
        search_query = request.GET.get('search', '')
        
        if search_query:
            diseases_list = diseases_list.filter(
                Q(name__icontains=search_query) |
                Q(scientific_name__icontains=search_query) |
                Q(description__icontains=search_query)
            )
            
        paginator = Paginator(diseases_list, 10)
        page = request.GET.get('page')
        diseases = paginator.get_page(page)
        return render(request, 'diseases/disease_list.html', {
            'diseases': diseases,
            'search_query': search_query
        })

    def create(self, request):
        if request.method == 'POST':
            form = DiseaseForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('diseases:disease-list')
            categories = DiseaseCategory.objects.all()
            return render(request, 'diseases/disease_form.html', {'form': form, 'categories': categories})
        else:
            form = DiseaseForm()
            categories = DiseaseCategory.objects.all()
            return render(request, 'diseases/disease_form.html', {'form': form, 'categories': categories})

    def retrieve(self, request, pk=None):
        disease = get_object_or_404(Disease, pk=pk)
        return render(request, 'diseases/disease_detail.html', {'disease': disease})

    def update(self, request, pk=None):
        disease = get_object_or_404(Disease, pk=pk)
        categories = DiseaseCategory.objects.all()  # Move this line here
        if request.method == 'POST':
            form = DiseaseForm(request.POST, instance=disease)
            if form.is_valid():
                form.save()
                return redirect('diseases:disease-list')
        else:
            form = DiseaseForm(instance=disease)
        return render(request, 'diseases/disease_form.html', {
            'form': form,
            'disease': disease,
            'categories': categories
        })

    def destroy(self, request, pk=None):
        disease = get_object_or_404(Disease, pk=pk)
        if request.method == 'POST':
            disease.delete()
            return redirect('diseases:disease-list')
        return render(request, 'diseases/disease_confirm_delete.html', {'disease': disease})
