from django.core.management.base import BaseCommand
from diseases.models import DiseaseCategory

class Command(BaseCommand):
    help = 'Load initial disease categories'

    def handle(self, *args, **kwargs):
        categories = {
            'Infectious Diseases': {
                'subcategories': ['Bacterial Infections', 'Viral Infections', 'Fungal Infections', 'Parasitic Diseases']
            },
            'Cardiovascular Diseases': {
                'subcategories': ['Heart Diseases', 'Vascular Diseases', 'Blood Disorders']
            },
            'Respiratory Diseases': {
                'subcategories': ['Upper Respiratory', 'Lower Respiratory', 'Pleural Disorders']
            },
            'Neurological Disorders': {
                'subcategories': ['Brain Disorders', 'Spinal Cord Disorders', 'Nerve Diseases']
            },
            'Gastrointestinal Diseases': {
                'subcategories': ['Stomach Disorders', 'Intestinal Diseases', 'Liver Diseases']
            },
            'Endocrine Disorders': {
                'subcategories': ['Thyroid Disorders', 'Diabetes', 'Adrenal Disorders']
            },
            'Musculoskeletal Disorders': {
                'subcategories': ['Bone Diseases', 'Joint Disorders', 'Muscle Diseases']
            },
            'Mental Health Disorders': {
                'subcategories': ['Mood Disorders', 'Anxiety Disorders', 'Psychotic Disorders']
            }
        }

        for main_category, data in categories.items():
            parent = DiseaseCategory.objects.create(
                name=main_category,
                description=f'Category for {main_category.lower()}'
            )
            
            for subcategory in data['subcategories']:
                DiseaseCategory.objects.create(
                    name=subcategory,
                    description=f'Subcategory for {subcategory.lower()}',
                    parent_category=parent
                )

        self.stdout.write(self.style.SUCCESS('Successfully loaded disease categories'))