from django import forms
from .models import DiseaseCategory

class DiseaseCategoryForm(forms.ModelForm):
    class Meta:
        model = DiseaseCategory
        fields = ['name', 'description', 'parent_category']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }
