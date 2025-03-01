from django.core.management.base import BaseCommand
from medicines.models import Medicine, MedicineRecommendation
from diseases.models import Disease

class Command(BaseCommand):
    help = 'Load medicine recommendations data'

    def handle(self, *args, **kwargs):
        recommendations = {
            'Hypertension': {
                'first_line': ['Lisinopril', 'Amlodipine', 'Hydrochlorothiazide'],
                'second_line': ['Metoprolol', 'Losartan', 'Valsartan'],
                'alternative': ['Carvedilol', 'Ramipril', 'Atenolol'],
                'instructions': 'Start with lowest effective dose and titrate as needed',
                'contraindications': 'Monitor blood pressure and kidney function regularly',
                'effectiveness': 5,
                'evidence': 'HIGH'
            },
            'Heart Failure': {
                'first_line': ['Lisinopril', 'Carvedilol', 'Spironolactone'],
                'second_line': ['Metoprolol', 'Digoxin', 'Ramipril'],
                'alternative': ['Valsartan', 'Losartan'],
                'instructions': 'Regular monitoring of heart function required',
                'contraindications': 'Monitor kidney function and potassium levels',
                'effectiveness': 4,
                'evidence': 'HIGH'
            },
            'Coronary Artery Disease': {
                'first_line': ['Atorvastatin', 'Clopidogrel', 'Metoprolol'],
                'second_line': ['Rosuvastatin', 'Nitroglycerin', 'Amlodipine'],
                'alternative': ['Carvedilol', 'Ramipril'],
                'instructions': 'Regular lipid profile monitoring required',
                'contraindications': 'Monitor liver function with statins',
                'effectiveness': 5,
                'evidence': 'HIGH'
            },
            'Atrial Fibrillation': {
                'first_line': ['Warfarin', 'Metoprolol', 'Digoxin'],
                'second_line': ['Carvedilol', 'Atenolol'],
                'alternative': ['Amiodarone'],
                'instructions': 'Regular INR monitoring for warfarin',
                'contraindications': 'Watch for bleeding complications',
                'effectiveness': 4,
                'evidence': 'MODERATE'
            },
            'Asthma': {
                'first_line': ['Albuterol', 'Fluticasone', 'Montelukast'],
                'second_line': ['Budesonide', 'Theophylline'],
                'alternative': ['Cromolyn', 'Prednisone'],
                'instructions': 'Use rescue inhaler as needed',
                'contraindications': 'Monitor for signs of worsening asthma',
                'effectiveness': 4,
                'evidence': 'HIGH'
            },
            'COPD': {
                'first_line': ['Albuterol', 'Tiotropium', 'Fluticasone'],
                'second_line': ['Salmeterol', 'Ipratropium'],
                'alternative': ['Prednisone', 'Theophylline'],
                'instructions': 'Use rescue inhaler as needed',
                'contraindications': 'Monitor for signs of worsening COPD',
                'effectiveness': 4,
                'evidence': 'HIGH'
            },
            'Diabetes': {
                'first_line': ['Metformin', 'Gliclazide', 'Pioglitazone'],
                'second_line': ['Glibenclamide', 'Sitagliptin'],
                'alternative': ['Insulin', 'Acarbose'],
                'instructions': 'Monitor blood glucose levels regularly',
                'contraindications': 'Monitor kidney function and HbA1c',
                'effectiveness': 5,
                'evidence': 'HIGH'
            },
            'Thyroid Disorders': {
                'first_line': ['Levothyroxine'],
                'second_line': ['Methimazole'],
                'alternative': ['Liothyronine'],
                'instructions': 'Monitor TSH levels regularly',
                'contraindications': 'Monitor for signs of hyperthyroidism',
                'effectiveness': 5,
                'evidence': 'HIGH'
            },
            'Osteoporosis': {
                'first_line': ['Alendronate', 'Calcium', 'Vitamin D'],
                'second_line': ['Risedronate', 'Zoledronic Acid'],
                'alternative': ['Raloxifene', 'Teriparatide'],
                'instructions': 'Monitor bone density regularly',
                'contraindications': 'Monitor for signs of osteonecrosis',
                'effectiveness': 5,
                'evidence': 'HIGH'
            },
            'Depression': {
                'first_line': ['Fluoxetine', 'Sertraline', 'Citalopram'],
                'second_line': ['Venlafaxine', 'Mirtazapine'],
                'alternative': ['Bupropion', 'Duloxetine'],
                'instructions': 'Monitor for signs of worsening depression',
                'contraindications': 'Monitor for signs of serotonin syndrome',
                'effectiveness': 5,
                'evidence': 'HIGH'
            },
            'Anxiety Disorders': {
                'first_line': ['Alprazolam', 'Lorazepam', 'Buspirone'],
                'second_line': ['Clonazepam', 'Diazepam'],
                'alternative': ['Hydroxyzine', 'Pregabalin'],
                'instructions': 'Avoid long-term use of benzodiazepines',
                'contraindications': 'Monitor for signs of dependence',
                'effectiveness': 5,
                'evidence': 'HIGH'
            },
            'Migraine': {
                'first_line': ['Sumatriptan', 'Ibuprofen', 'Acetaminophen'],
                'second_line': ['Naproxen', 'Rizatriptan'],
                'alternative': ['Topiramate'],
                'instructions': 'Avoid overuse of painkillers',
                'contraindications': 'Monitor for signs of medication overuse headache',
                'effectiveness': 5,
                'evidence': 'HIGH'
            },  
            'Epilepsy': {
                'first_line': ['Carbamazepine', 'Valproate', 'Phenytoin'],
                'second_line': ['Lamotrigine', 'Levetiracetam'],
                'alternative': ['Topiramate', 'Gabapentin'],
                'instructions': 'Monitor for signs of drug toxicity',
                'contraindications': 'Monitor for signs of drug interactions',
                'effectiveness': 5,
                'evidence': 'HIGH'
            },
            'Schizophrenia': {
                'first_line': ['Risperidone', 'Olanzapine', 'Quetiapine'],
                'second_line': ['Aripiprazole', 'Ziprasidone'],
                'alternative': ['Clozapine', 'Haloperidol'],
                'instructions': 'Monitor for signs of extrapyramidal symptoms',
                'contraindications': 'Monitor for signs of metabolic syndrome',
                'effectiveness': 5,
                'evidence': 'HIGH'
            },
            'Bipolar Disorder': {
                'first_line': ['Lithium', 'Valproate', 'Lamotrigine'],
                'second_line': ['Carbamazepine', 'Olanzapine'],
                'alternative': ['Quetiapine', 'Risperidone'],
                'instructions': 'Monitor for signs of lithium toxicity',
                'contraindications': 'Monitor for signs of drug interactions',
                'effectiveness': 5,
                'evidence': 'HIGH'
            },
            'Alzheimer\'s Disease': {
                'first_line': ['Donepezil', 'Rivastigmine', 'Galantamine'],
                'second_line': ['Memantine'],
                'alternative': ['Rivastigmine Patch', 'Donepezil ODT'],
                'instructions': 'Monitor for signs of drug interactions',
                'contraindications': 'Monitor for signs of drug toxicity',
                'effectiveness': 5,
                'evidence': 'HIGH'
            },
            'Parkinson\'s Disease': {
                'first_line': ['Levodopa', 'Carbidopa', 'Entacapone'],
                'second_line': ['Pramipexole', 'Ropinirole'],
                'alternative': ['Selegiline', 'Amantadine'],
                'instructions': 'Monitor for signs of drug interactions',
                'contraindications': 'Monitor for signs of drug toxicity',
                'effectiveness': 5,
                'evidence': 'HIGH'
            },
            'HIV/AIDS': {
                'first_line': ['Tenofovir', 'Emtricitabine', 'Dolutegravir'],
                'second_line': ['Lamivudine', 'Efavirenz'],
                'alternative': ['Raltegravir', 'Darunavir'],
                'instructions': 'Monitor for signs of drug interactions',
                'contraindications': 'Monitor for signs of drug toxicity',
                'effectiveness': 5,
                'evidence': 'HIGH'
            },
            'Tuberculosis': {
                'first_line': ['Isoniazid', 'Rifampicin', 'Pyrazinamide'],
                'second_line': ['Ethambutol', 'Levofloxacin'],
                'alternative': ['Moxifloxacin', 'Linezolid'],
                'instructions': 'Monitor for signs of drug interactions',
                'contraindications': 'Monitor for signs of drug toxicity',
                'effectiveness': 5,
                'evidence': 'HIGH'
            },
            'Malaria': {
                'first_line': ['Chloroquine', 'Mefloquine', 'Doxycycline'],
                'second_line': ['Artemether', 'Lumefantrine'],
                'alternative': ['Atovaquone', 'Proguanil'],
                'instructions': 'Monitor for signs of drug interactions',
                'contraindications': 'Monitor for signs of drug toxicity',
                'effectiveness': 5,
                'evidence': 'HIGH'
            },
            'Cholera': {
                'first_line': ['Oral Rehydration Solution', 'Doxycycline', 'Azithromycin'],
                'second_line': ['Ciprofloxacin', 'Levofloxacin'],
                'alternative': ['Rifaximin', 'Erythromycin'],
                'instructions': 'Monitor for signs of dehydration',
                'contraindications': 'Monitor for signs of drug toxicity',
                'effectiveness': 5,
                'evidence': 'HIGH'
            },
            'Dengue Fever': {
                'first_line': ['Paracetamol', 'Oral Rehydration Solution'],
                'second_line': ['Ibuprofen', 'Naproxen'],
                'alternative': ['Aspirin', 'Doxycycline'],
                'instructions': 'Monitor for signs of bleeding',
                'contraindications': 'Monitor for signs of liver toxicity',
                'effectiveness': 5,
                'evidence': 'HIGH'
            },
            'Typhoid Fever': {
                'first_line': ['Ceftriaxone', 'Ciprofloxacin', 'Azithromycin'],
                'second_line': ['Levofloxacin', 'Cefixime'],
                'alternative': ['Chloramphenicol', 'Trimethoprim-Sulfamethoxazole'],
                'instructions': 'Monitor for signs of drug interactions',
                'contraindications': 'Monitor for signs of drug toxicity',
                'effectiveness': 5,
                'evidence': 'HIGH'
            },
            'Pneumonia': {
                'first_line': ['Amoxicillin', 'Azithromycin', 'Ceftriaxone'],
                'second_line': ['Levofloxacin', 'Cefuroxime'],
                'alternative': ['Clarithromycin', 'Doxycycline'],
                'instructions': 'Monitor for signs of drug interactions',
                'contraindications': 'Monitor for signs of drug toxicity',
                'effectiveness': 5,
                'evidence': 'HIGH'
            },
            'Urinary Tract Infection': {
                'first_line': ['Nitrofurantoin', 'Ciprofloxacin', 'Trimethoprim-Sulfamethoxazole'],
                'second_line': ['Levofloxacin', 'Cefixime'],
                'alternative': ['Ceftriaxone', 'Amoxicillin-Clavulanate'],
                'instructions': 'Monitor for signs of drug interactions',
                'contraindications': 'Monitor for signs of drug toxicity',
                'effectiveness': 5,
                'evidence': 'HIGH'
            },
            'Gastroenteritis': {
                'first_line': ['Oral Rehydration Solution', 'Loperamide', 'Ondansetron'],
                'second_line': ['Ciprofloxacin', 'Metronidazole'],
                'alternative': ['Azithromycin', 'Rifaximin'],
                'instructions': 'Monitor for signs of dehydration',
                'contraindications': 'Monitor for signs of drug toxicity',
                'effectiveness': 5,
                'evidence': 'HIGH'
            },
            'Hepatitis B': {
                'first_line': ['Tenofovir', 'Entecavir', 'Lamivudine'],
                'second_line': ['Adefovir', 'Telbivudine'],
                'alternative': ['Peginterferon', 'Emtricitabine'],
                'instructions': 'Monitor for signs of drug interactions',
                'contraindications': 'Monitor for signs of drug toxicity',
                'effectiveness': 5,
                'evidence': 'HIGH'
            },
            'Hepatitis C': {
                'first_line': ['Sofosbuvir', 'Ledipasvir', 'Ribavirin'],
                'second_line': ['Daclatasvir', 'Velpatasvir'],
                'alternative': ['Simeprevir', 'Grazoprevir'],
                'instructions': 'Monitor for signs of drug interactions',
                'contraindications': 'Monitor for signs of drug toxicity',
                'effectiveness': 5,
                'evidence': 'HIGH'
            },
        }

        for disease_name, data in recommendations.items():
            try:
                # Changed from get() to filter().first() to avoid MultipleObjectsReturned
                disease = Disease.objects.filter(name=disease_name).first()
                if not disease:
                    self.stdout.write(self.style.WARNING(f'Disease {disease_name} not found'))
                    continue

                # Create first line recommendations
                for med_name in data['first_line']:
                    try:
                        medicine = Medicine.objects.get(name=med_name)
                        MedicineRecommendation.objects.create(
                            disease=disease,
                            medicine=medicine,
                            recommendation_type='FIRST_LINE',
                            special_instructions=data['instructions'],
                            contraindications=data['contraindications'],
                            effectiveness_rating=data['effectiveness'],
                            evidence_level=data['evidence']
                        )
                    except Medicine.DoesNotExist:
                        self.stdout.write(self.style.WARNING(f'Medicine {med_name} not found'))

                # Create second line recommendations
                for med_name in data['second_line']:
                    try:
                        medicine = Medicine.objects.get(name=med_name)
                        MedicineRecommendation.objects.create(
                            disease=disease,
                            medicine=medicine,
                            recommendation_type='SECOND_LINE',
                            special_instructions=data['instructions'],
                            contraindications=data['contraindications'],
                            effectiveness_rating=data['effectiveness'] - 1,
                            evidence_level=data['evidence']
                        )
                    except Medicine.DoesNotExist:
                        self.stdout.write(self.style.WARNING(f'Medicine {med_name} not found'))

                # Create alternative recommendations
                for med_name in data['alternative']:
                    try:
                        medicine = Medicine.objects.get(name=med_name)
                        MedicineRecommendation.objects.create(
                            disease=disease,
                            medicine=medicine,
                            recommendation_type='ALTERNATIVE',
                            special_instructions=data['instructions'],
                            contraindications=data['contraindications'],
                            effectiveness_rating=data['effectiveness'] - 2,
                            evidence_level='MODERATE'
                        )
                    except Medicine.DoesNotExist:
                        self.stdout.write(self.style.WARNING(f'Medicine {med_name} not found'))

            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error processing {disease_name}: {str(e)}'))

        self.stdout.write(self.style.SUCCESS('Successfully loaded medicine recommendations'))
