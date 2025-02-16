from django import forms
from .models import Brand, Manufacturer, Medicine

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'manufacturer', 'medicine']