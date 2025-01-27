from django.core.management.base import BaseCommand
from diseases.models import Disease, DiseaseCategory

class Command(BaseCommand):
   help = 'Load infectious diseases data'

   def handle(self, *args, **kwargs):
       
       diseases = {
           'Bacterial Infections': [
               {
                   'name': 'Tuberculosis',
                   'scientific_name': 'Mycobacterium tuberculosis',
                   'description': 'Bacterial infection primarily affecting the lungs',
                   'symptoms': 'Persistent cough, chest pain, fever, fatigue, weight loss',
                   'causes': 'Caused by Mycobacterium tuberculosis bacteria spread through air',
                   'treatment': 'Long-term antibiotics, typically 6-9 months',
                   'severity_level': 3,
                   'is_contagious': True,
                   'incubation_period': '2-12 weeks'
               },
               {
                   'name': 'Strep Throat',
                   'scientific_name': 'Streptococcal pharyngitis',
                   'description': 'Bacterial infection causing throat inflammation',
                   'symptoms': 'Sore throat, fever, swollen lymph nodes',
                   'causes': 'Group A Streptococcus bacteria',
                   'treatment': 'Antibiotics, usually penicillin or amoxicillin',
                   'severity_level': 2,
                   'is_contagious': True,
                   'incubation_period': '2-5 days'
               }
           ],
           'Viral Infections': [
               {
                   'name': 'Influenza',
                   'scientific_name': 'Influenza virus infection',
                   'description': 'Viral infection affecting respiratory tract',
                   'symptoms': 'Fever, cough, body aches, fatigue',
                   'causes': 'Influenza A or B viruses',
                   'treatment': 'Rest, fluids, antiviral medications if severe',
                   'severity_level': 2,
                   'is_contagious': True,
                   'incubation_period': '1-4 days'
               },
                {
                     'name': 'HIV/AIDS',
                     'scientific_name': 'Human immunodeficiency virus infection',
                     'description': 'Viral infection affecting immune system',
                     'symptoms': 'Flu-like symptoms, fatigue, weight loss, opportunistic infections',
                     'causes': 'HIV transmitted through blood, sexual contact, or mother-to-child',
                     'treatment': 'Antiretroviral therapy to manage HIV, no cure',
                     'severity_level': 4,
                     'is_contagious': True,
                     'incubation_period': 'Variable'
                },
                {
                     'name': 'COVID-19',
                     'scientific_name': 'SARS-CoV-2 infection',
                     'description': 'Respiratory illness caused by novel coronavirus',
                     'symptoms': 'Fever, cough, shortness of breath, loss of taste or smell',
                     'causes': 'SARS-CoV-2 virus transmitted through respiratory droplets',
                     'treatment': 'Supportive care, oxygen therapy, antiviral medications',
                     'severity_level': 4,
                     'is_contagious': True,
                     'incubation_period': '2-14 days'
                },
                {
                     'name': 'Hepatitis C',
                     'scientific_name': 'HCV infection',
                     'description': 'Viral infection causing liver inflammation',
                     'symptoms': 'Fatigue, jaundice, abdominal pain',
                     'causes': 'Hepatitis C virus transmitted through blood or body fluids',
                     'treatment': 'Antiviral medications, liver transplant',
                     'severity_level': 3,
                     'is_contagious': True,
                     'incubation_period': '2 weeks to 6 months'
                },
                {
                     'name': 'Herpes Simplex',
                     'scientific_name': 'HSV infection',
                     'description': 'Viral infection causing cold sores or genital sores',
                     'symptoms': 'Painful blisters, itching, flu-like symptoms',
                     'causes': 'Herpes simplex virus type 1 or 2',
                     'treatment': 'Antiviral medications to manage outbreaks',
                     'severity_level': 2,
                     'is_contagious': True,
                     'incubation_period': '2-12 days'
                }
           ],
           'Fungal Infections': [
               {
                   'name': 'Candidiasis',
                   'scientific_name': 'Candida albicans infection',
                   'description': 'Fungal infection affecting various body parts',
                   'symptoms': 'Rash, itching, white patches',
                   'causes': 'Overgrowth of Candida fungi',
                   'treatment': 'Antifungal medications',
                   'severity_level': 1,
                   'is_contagious': False,
                   'incubation_period': 'Variable'
               }
           ],
           'Parasitic Diseases': [
               {
                   'name': 'Malaria',
                   'scientific_name': 'Plasmodium infection',
                   'description': 'Parasitic infection affecting red blood cells',
                   'symptoms': 'Fever, chills, sweating, headache',
                   'causes': 'Plasmodium parasites transmitted by mosquitoes',
                   'treatment': 'Antimalarial medications',
                   'severity_level': 4,
                   'is_contagious': False,
                   'incubation_period': '7-30 days'
               }
           ],
           'Heart Diseases': [
               {
                   'name': 'Coronary Artery Disease',
                   'scientific_name': 'Atherosclerotic heart disease',
                   'description': 'Buildup of plaque in coronary arteries',
                   'symptoms': 'Chest pain, shortness of breath, fatigue, irregular heartbeat',
                   'causes': 'Atherosclerosis, high blood pressure, high cholesterol',
                   'treatment': 'Medications, lifestyle changes, possible surgery',
                   'severity_level': 3,
                   'is_contagious': False,
                   'incubation_period': 'Develops over years'
               },
               {
                   'name': 'Heart Failure',
                   'scientific_name': 'Cardiac failure',
                   'description': 'Heart cannot pump blood effectively',
                   'symptoms': 'Shortness of breath, fatigue, swelling in legs',
                   'causes': 'Coronary artery disease, high blood pressure, previous heart attack',
                   'treatment': 'Medications, lifestyle changes, devices, surgery',
                   'severity_level': 4,
                   'is_contagious': False,
                   'incubation_period': 'Progressive condition'
               }
           ],
           'Vascular Diseases': [
               {
                   'name': 'Deep Vein Thrombosis',
                   'scientific_name': 'DVT',
                   'description': 'Blood clot in deep vein, usually in legs',
                   'symptoms': 'Leg pain, swelling, warmth, redness',
                   'causes': 'Immobility, surgery, pregnancy, genetics',
                   'treatment': 'Blood thinners, compression stockings',
                   'severity_level': 3,
                   'is_contagious': False,
                   'incubation_period': 'Hours to days'
               }
           ],
           'Blood Disorders': [
               {
                   'name': 'Anemia',
                   'scientific_name': 'Iron deficiency anemia',
                   'description': 'Low red blood cell count or hemoglobin',
                   'symptoms': 'Fatigue, weakness, shortness of breath, pale skin',
                   'causes': 'Iron deficiency, blood loss, poor absorption',
                   'treatment': 'Iron supplements, dietary changes',
                   'severity_level': 2,
                   'is_contagious': False,
                   'incubation_period': 'Develops gradually'
               }
           ],
              'Upper Respiratory': [
                {
                     'name': 'Common Cold',
                        'scientific_name': 'Viral upper respiratory infection',
                        'description': 'Mild viral infection affecting nose and throat',
                        'symptoms': 'Runny nose, sneezing, sore throat',
                        'causes': 'Rhinovirus, coronavirus, other viruses',
                        'treatment': 'Rest, fluids, over-the-counter medications',
                        'severity_level': 1,
                        'is_contagious': True,
                        'incubation_period': '1-3 days'
                }
            ],
            'Lower Respiratory': [
                {
                    'name': 'Pneumonia',
                    'scientific_name': 'Bacterial or viral lung infection',
                    'description': 'Inflammation of lung tissue',
                    'symptoms': 'Cough, fever, chest pain, difficulty breathing',
                    'causes': 'Bacteria, viruses, fungi',
                    'treatment': 'Antibiotics, antivirals, oxygen therapy',
                    'severity_level': 3,
                    'is_contagious': True,
                    'incubation_period': '1-3 days'
                }
            ],  
            'Pleural Disorders': [
                {
                    'name': 'Pleurisy',
                    'scientific_name': 'Pleuritis',
                    'description': 'Inflammation of pleura surrounding lungs',
                    'symptoms': 'Chest pain, cough, shortness of breath',
                    'causes': 'Viral infections, pneumonia, autoimmune conditions',
                    'treatment': 'Pain relief, treat underlying cause',
                    'severity_level': 2,
                    'is_contagious': False,
                    'incubation_period': 'Variable'
                }
            ],
            'Brain Disorders': [
                {
                    'name': 'Alzheimer\'s Disease',
                    'scientific_name': 'Alzheimer\'s',
                    'description': 'Progressive brain disorder affecting memory and thinking',
                    'symptoms': 'Memory loss, confusion, mood changes',
                    'causes': 'Genetics, age, brain changes',
                    'treatment': 'Medications, therapy, support',
                    'severity_level': 4,
                    'is_contagious': False,
                    'incubation_period': 'Develops over years'
                }
            ],
            'Spinal Cord Disorders': [
                {
                    'name': 'Spinal Stenosis',
                    'scientific_name': 'Narrowing of spinal canal',
                    'description': 'Compression of spinal cord or nerves',
                    'symptoms': 'Back pain, numbness, weakness, leg pain',
                    'causes': 'Aging, arthritis, spinal injuries',
                    'treatment': 'Physical therapy, medications, surgery',
                    'severity_level': 3,
                    'is_contagious': False,
                    'incubation_period': 'Develops over years'
                }
            ],
            'Nerve Diseases': [
                {
                    'name': 'Multiple Sclerosis',
                    'scientific_name': 'MS',
                    'description': 'Autoimmune disease affecting nerves in brain and spinal cord',
                    'symptoms': 'Numbness, weakness, vision problems, fatigue',
                    'causes': 'Autoimmune response, genetics, environment',
                    'treatment': 'Medications, therapy, lifestyle changes',
                    'severity_level': 3,
                    'is_contagious': False,
                    'incubation_period': 'Variable'
                }
            ],
            'Stomach Disorders': [
                {
                    'name': 'Gastritis',
                    'scientific_name': 'Stomach inflammation',
                    'description': 'Inflammation of stomach lining',
                    'symptoms': 'Stomach pain, bloating, nausea, vomiting',
                    'causes': 'H. pylori infection, NSAIDs, alcohol',
                    'treatment': 'Antibiotics, acid reducers, dietary changes',
                    'severity_level': 2,
                    'is_contagious': False,
                    'incubation_period': 'Variable'
                }
            ],
            'Intestinal Diseases': [
                {
                    'name': 'Irritable Bowel Syndrome',
                    'scientific_name': 'IBS',
                    'description': 'Functional disorder of digestive system',
                    'symptoms': 'Abdominal pain, bloating, diarrhea, constipation',
                    'causes': 'Unknown, triggers like food, stress',
                    'treatment': 'Dietary changes, stress management, medications',
                    'severity_level': 2,
                    'is_contagious': False,
                    'incubation_period': 'Variable'
                }
            ],
            'Liver Diseases': [
                {
                    'name': 'Hepatitis B',
                    'scientific_name': 'HBV infection',
                    'description': 'Viral infection causing liver inflammation',
                    'symptoms': 'Fatigue, jaundice, abdominal pain',
                    'causes': 'Hepatitis B virus transmitted through blood or body fluids',
                    'treatment': 'Antiviral medications, liver transplant',
                    'severity_level': 3,
                    'is_contagious': True,
                    'incubation_period': '6 weeks to 6 months'
                }
            ],
            'Thyroid Disorders': [
                {
                    'name': 'Hypothyroidism',
                    'scientific_name': 'Underactive thyroid',
                    'description': 'Low thyroid hormone levels',
                    'symptoms': 'Fatigue, weight gain, cold intolerance, depression',
                    'causes': 'Autoimmune disease, thyroid surgery, radiation',
                    'treatment': 'Thyroid hormone replacement',
                    'severity_level': 2,
                    'is_contagious': False,
                    'incubation_period': 'Variable'
                }
            ],
            'Diabetes': [
                {
                    'name': 'Type 2 Diabetes',
                    'scientific_name': 'Insulin resistance diabetes',
                    'description': 'Chronic condition affecting blood sugar levels',
                    'symptoms': 'Increased thirst, frequent urination, fatigue',
                    'causes': 'Genetics, lifestyle factors, obesity',
                    'treatment': 'Diet, exercise, medications, insulin',
                    'severity_level': 3,
                    'is_contagious': False,
                    'incubation_period': 'Develops gradually'
                }
            ],
            'Adrenal Disorders': [
                {
                    'name': 'Addison\'s Disease',
                    'scientific_name': 'Adrenal insufficiency',
                    'description': 'Adrenal glands do not produce enough hormones',
                    'symptoms': 'Fatigue, weight loss, low blood pressure',
                    'causes': 'Autoimmune disease, infections, cancer',
                    'treatment': 'Hormone replacement therapy',
                    'severity_level': 3,
                    'is_contagious': False,
                    'incubation_period': 'Variable'
                }
            ],
            'Bone Diseases': [
                {
                    'name': 'Osteoporosis',
                    'scientific_name': 'Bone density loss',
                    'description': 'Weak, brittle bones prone to fractures',
                    'symptoms': 'Back pain, height loss, fractures',
                    'causes': 'Aging, hormonal changes, genetics',
                    'treatment': 'Medications, calcium, vitamin D, exercise',
                    'severity_level': 2,
                    'is_contagious': False,
                    'incubation_period': 'Develops over years'
                }
            ],
            'Joint Disorders': [
                {
                    'name': 'Osteoarthritis',
                    'scientific_name': 'Degenerative joint disease',
                    'description': 'Wearing down of joint cartilage',
                    'symptoms': 'Joint pain, stiffness, swelling',
                    'causes': 'Aging, joint injury, obesity',
                    'treatment': 'Pain relief, exercise, weight loss',
                    'severity_level': 2,
                    'is_contagious': False,
                    'incubation_period': 'Develops over years'
                }
            ],
            'Muscle Diseases': [
                {
                    'name': 'Muscular Dystrophy',
                    'scientific_name': 'MD',
                    'description': 'Inherited muscle-weakening disease',
                    'symptoms': 'Muscle weakness, loss of muscle mass',
                    'causes': 'Genetic mutations affecting muscle proteins',
                    'treatment': 'Physical therapy, assistive devices',
                    'severity_level': 4,
                    'is_contagious': False,
                    'incubation_period': 'Variable'
                }
            ],
            'Mood Disorders': [
                {
                    'name': 'Depression',
                    'scientific_name': 'Major depressive disorder',
                    'description': 'Persistent sadness, loss of interest',
                    'symptoms': 'Low mood, fatigue, sleep problems',
                    'causes': 'Genetics, brain chemistry, life events',
                    'treatment': 'Therapy, medications, lifestyle changes',
                    'severity_level': 2,
                    'is_contagious': False,
                    'incubation_period': 'Variable'
                }
            ],
            'Anxiety Disorders': [
                {
                    'name': 'Generalized Anxiety Disorder',
                    'scientific_name': 'GAD',
                    'description': 'Excessive worry and anxiety',
                    'symptoms': 'Restlessness, irritability, muscle tension',
                    'causes': 'Genetics, brain chemistry, stress',
                    'treatment': 'Therapy, medications, lifestyle changes',
                    'severity_level': 2,
                    'is_contagious': False,
                    'incubation_period': 'Variable'
                }
            ],
            'Psychotic Disorders': [
                {
                    'name': 'Schizophrenia',
                    'scientific_name': 'Schizophrenia spectrum disorder',
                    'description': 'Chronic brain disorder affecting thoughts and behavior',
                    'symptoms': 'Hallucinations, delusions, disorganized thinking',
                    'causes': 'Genetics, brain chemistry, environment',
                    'treatment': 'Medications, therapy, support',
                    'severity_level': 4,
                    'is_contagious': False,
                    'incubation_period': 'Variable'
                }
            ],

            'Cardiovascular Diseases': [
                {
                    'name': 'Coronary Artery Disease',
                    'scientific_name': 'Atherosclerotic heart disease',
                    'description': 'Buildup of plaque in coronary arteries',
                    'symptoms': 'Chest pain, shortness of breath, fatigue, irregular heartbeat',
                    'causes': 'Atherosclerosis, high blood pressure, high cholesterol',
                    'treatment': 'Medications, lifestyle changes, possible surgery',
                    'severity_level': 3,
                    'is_contagious': False,
                    'incubation_period': 'Develops over years'
                },
                {
                    'name': 'Heart Failure',
                    'scientific_name': 'Cardiac failure',
                    'description': 'Heart cannot pump blood effectively',
                    'symptoms': 'Shortness of breath, fatigue, swelling in legs',
                    'causes': 'Coronary artery disease, high blood pressure, previous heart attack',
                    'treatment': 'Medications, lifestyle changes, devices, surgery',
                    'severity_level': 4,
                    'is_contagious': False,
                    'incubation_period': 'Progressive condition'
                }  ,
                {
                    'name': 'Arrhythmia',
                    'scientific_name': 'Irregular heartbeat',
                    'description': 'Abnormal heart rhythm',
                    'symptoms': 'Palpitations, dizziness, chest pain',
                    'causes': 'Heart disease, high blood pressure, diabetes',
                    'treatment': 'Medications, devices, surgery',
                    'severity_level': 3,
                    'is_contagious': False,
                    'incubation_period': 'Variable'
                },
                {
                    'name': 'Peripheral Artery Disease',
                    'scientific_name': 'PAD',
                    'description': 'Narrowing of peripheral arteries',
                    'symptoms': 'Leg pain, cramps, slow wound healing',
                    'causes': 'Atherosclerosis, diabetes, smoking',
                    'treatment': 'Medications, lifestyle changes, surgery',
                    'severity_level': 3,
                    'is_contagious': False,
                    'incubation_period': 'Develops over years'
                },
                {
                    'name': 'Rheumatic Heart Disease',
                    'scientific_name': 'RHD',
                    'description': 'Heart damage from rheumatic fever',
                    'symptoms': 'Heart murmur, chest pain, fatigue',
                    'causes': 'Untreated strep throat or scarlet fever',
                    'treatment': 'Medications, surgery',
                    'severity_level': 3,
                    'is_contagious': False,
                    'incubation_period': 'Variable'
                },
                {
                    'name': 'Heart Valve Disease',
                    'scientific_name': 'Valvular heart disease',
                    'description': 'Malfunction of heart valves',
                    'symptoms': 'Shortness of breath, chest pain, fatigue',
                    'causes': 'Congenital defects, infections, aging',
                    'treatment': 'Medications, surgery',
                    'severity_level': 3,
                    'is_contagious': False,
                    'incubation_period': 'Variable'
                },
                {
                    'name': 'Cardiomyopathy',
                    'scientific_name': 'Heart muscle disease',
                    'description': 'Weakening of heart muscle',
                    'symptoms': 'Fatigue, swelling, shortness of breath',
                    'causes': 'Genetics, infections, toxins',
                    'treatment': 'Medications, devices, surgery',
                    'severity_level': 3,
                    'is_contagious': False,
                    'incubation_period': 'Variable'
                },
                {
                    'name': 'Hypertension',
                    'scientific_name': 'High blood pressure',
                    'description': 'Elevated blood pressure levels',
                    'symptoms': 'Often no symptoms, headaches, nosebleeds',
                    'causes': 'Genetics, diet, lifestyle factors',
                    'treatment': 'Lifestyle changes, medications',
                    'severity_level': 2,
                    'is_contagious': False,
                    'incubation_period': 'Develops gradually'
                },
                {
                    'name': 'Stroke',
                    'scientific_name': 'Cerebrovascular accident',
                    'description': 'Brain damage from lack of blood flow',
                    'symptoms': 'Sudden weakness, speech problems, vision changes',
                    'causes': 'Blood clot or bleeding in brain',
                    'treatment': 'Clot-busting drugs, surgery, rehabilitation',
                    'severity_level': 4,
                    'is_contagious': False,
                    'incubation_period': 'Variable'
                },
                {
                    'name': 'Aneurysm',
                    'scientific_name': 'Aortic aneurysm',
                    'description': 'Weakened blood vessel wall bulging',
                    'symptoms': 'Pain, pulsating mass, dizziness',
                    'causes': 'Atherosclerosis, high blood pressure, genetics',
                    'treatment': 'Monitoring, surgery',
                    'severity_level': 3,
                    'is_contagious': False,
                    'incubation_period': 'Variable'
                },
                {
                    'name': 'Heart Attack',
                    'scientific_name': 'Myocardial infarction',
                    'description': 'Blockage of blood flow to heart muscle',
                    'symptoms': 'Chest pain, shortness of breath, nausea',
                    'causes': 'Coronary artery blockage',
                    'treatment': 'Clot-busting drugs, angioplasty, surgery',
                    'severity_level': 4,
                    'is_contagious': False,
                    'incubation_period': 'Variable'
                }
            ]


       }

       for category_name, diseases in diseases.items():
           category = DiseaseCategory.objects.get(name=category_name)
           
           for disease_data in diseases:
               Disease.objects.create(
                   category=category,
                   **disease_data
               )

       self.stdout.write(self.style.SUCCESS('Successfully loaded infectious diseases'))