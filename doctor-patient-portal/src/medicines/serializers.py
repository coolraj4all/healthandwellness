from rest_framework import serializers
from medicines.models import Medicine, Manufacturer, MedicineRecommendation, Brand

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'

class MedicineSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer(read_only=True)
    
    class Meta:
        model = Medicine
        fields = '__all__'

class MedicineRecommendationSerializer(serializers.ModelSerializer):
    medicine = MedicineSerializer(read_only=True)
    
    class Meta:
        model = MedicineRecommendation
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer(read_only=True)

    class Meta:
        model = Brand
        fields = '__all__'