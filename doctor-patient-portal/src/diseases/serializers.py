from rest_framework import serializers
from .models import Disease, DiseaseCategory


class DiseaseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DiseaseCategory
        fields = '__all__'

class DiseaseSerializer(serializers.ModelSerializer):
    category = DiseaseCategorySerializer(read_only=True)
    
    class Meta:
        model = Disease
        fields = '__all__'