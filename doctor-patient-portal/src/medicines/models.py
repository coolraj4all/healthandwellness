from django.db import models
from diseases.models import Disease

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Medicine(models.Model):
    FORM_CHOICES = [
        ('tablet', 'Tablet'),
        ('capsule', 'Capsule'),
        ('liquid', 'Liquid'),
        ('injection', 'Injection'),
        ('topical', 'Topical'),
        ('inhaler', 'Inhaler'),
        ('drops', 'Drops'),
    ]

    name = models.CharField(max_length=200)
    generic_name = models.CharField(max_length=200)
    form = models.CharField(max_length=20, choices=FORM_CHOICES)
    strength = models.CharField(max_length=50)  # e.g., "500mg", "10ml"
    description = models.TextField()
    composition = models.TextField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT)
    storage_instructions = models.TextField(blank=True)
    side_effects = models.TextField(blank=True)
    precautions = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    requires_prescription = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.strength})"

class Brand(models.Model):
    name = models.CharField(max_length=200)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name='brands')
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT)
    is_generic = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['name', 'manufacturer']

    def __str__(self):
        return f"{self.name} by {self.manufacturer.name}"
    
class MedicineRecommendation(models.Model):
   disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
   medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
   special_instructions = models.TextField(blank=True)
   contraindications = models.TextField(blank=True)
   effectiveness_rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   def __str__(self):
       return f"{self.disease} - {self.primary_medicine} ({self.recommendation_type})"