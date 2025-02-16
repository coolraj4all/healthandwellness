from django import forms
from .models import Disease, DiseaseCategory

class DiseaseCategoryForm(forms.ModelForm):
    class Meta:
        model = DiseaseCategory
        fields = ['name', 'description', 'parent_category']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class DiseaseForm(forms.ModelForm):
    class Meta:
        model = Disease
        fields = [
            'name',
            'scientific_name',
            'description',
            'symptoms',
            'causes',
            'treatment',
            'category',
            'severity_level',
            'is_contagious',
            'incubation_period'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'symptoms': forms.Textarea(attrs={'rows': 4}),
            'causes': forms.Textarea(attrs={'rows': 4}),
            'treatment': forms.Textarea(attrs={'rows': 4}),
        }
