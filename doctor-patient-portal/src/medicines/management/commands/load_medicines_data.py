from django.core.management.base import BaseCommand
from medicines.models import Manufacturer, Brand, Medicine, MedicineRecommendation
from diseases.models import Disease

class Command(BaseCommand):
    help = 'Load cardiovascular diseases data'

    def handle(self, *args, **kwargs):
        # Create manufacturers
        manufacturers = {
            'novartis': Manufacturer.objects.create(
                name='Novartis',
                description='Swiss multinational pharmaceutical company',
                website='https://www.novartis.com',
                country='Switzerland'
            ),
            'pfizer': Manufacturer.objects.create(
                name='Pfizer',
                description='American multinational pharmaceutical corporation',
                website='https://www.pfizer.com',
                country='United States'
            ),
            'astrazeneca': Manufacturer.objects.create(
                name='AstraZeneca',
                description='British-Swedish pharmaceutical company',
                website='https://www.astrazeneca.com',
                country='United Kingdom'
            ),
            'merck': Manufacturer.objects.create(
                name='Merck',
                description='American multinational pharmaceutical company',
                website='https://www.merck.com',
                country='United States'
            ),
            'roche': Manufacturer.objects.create(
                name='Roche',
                description='Swiss multinational healthcare company',
                website='https://www.roche.com',
                country='Switzerland'
            ),
            'gsk': Manufacturer.objects.create(
                name='GlaxoSmithKline',
                description='British multinational pharmaceutical company',
                website='https://www.gsk.com',
                country='United Kingdom'
            ),
            'bayer': Manufacturer.objects.create(
                name='Bayer',
                description='German multinational pharmaceutical company',
                website='https://www.bayer.com',
                country='Germany'
            ),
            'sanofi': Manufacturer.objects.create(
                name='Sanofi',
                description='French multinational pharmaceutical company',
                website='https://www.sanofi.com',
                country='France'
            ),
            'johnson': Manufacturer.objects.create(
                name='Johnson & Johnson',
                description='American multinational corporation',
                website='https://www.jnj.com',
                country='United States'
            ),
            'abbott': Manufacturer.objects.create(
                name='Abbott',
                description='American multinational healthcare company',
                website='https://www.abbott.com',
                country='United States'
            ),
            'bms': Manufacturer.objects.create(
                name='Bristol Myers Squibb',
                description='American pharmaceutical company',
                website='https://www.bms.com',
                country='United States'
            ),
            'teva': Manufacturer.objects.create(
                name='Teva',
                description='Israeli multinational pharmaceutical company',
                website='https://www.tevapharm.com',
                country='Israel'
            ),
            'baxter': Manufacturer.objects.create(
                name='Baxter',
                description='American multinational healthcare company',
                website='https://www.baxter.com',
                country='United States'
            ),
            'eli': Manufacturer.objects.create(
                name='Eli Lilly',
                description='American pharmaceutical company',
                website='https://www.lilly.com',
                country='United States'
            ),
            'amgen': Manufacturer.objects.create(
                name='Amgen',
                description='American multinational biopharmaceutical company',
                website='https://www.amgen.com',
                country='United States'
            ),
            'biogen': Manufacturer.objects.create(
                name='Biogen',
                description='American multinational biotechnology company',
                website='https://www.biogen.com',
                country='United States'
            ),
            'celgene': Manufacturer.objects.create(
                name='Celgene',
                description='American biotechnology company',
                website='https://www.celgene.com',
                country='United States'
            ),
            'regeneron': Manufacturer.objects.create(
                name='Regeneron',
                description='American biotechnology company',
                website='https://www.regeneron.com',
                country='United States'
            ),
            'cipla': Manufacturer.objects.create(
                name='Cipla',
                description='Indian multinational pharmaceutical company',
                website='https://www.cipla.com',
                country='India'
            ),
            'sunpharma': Manufacturer.objects.create(
                name='Sun Pharmaceutical',
                description='Indian multinational pharmaceutical company',
                website='https://www.sunpharma.com',
                country='India'
            ),
            'drreddys': Manufacturer.objects.create(
                name='Dr. Reddy\'s Laboratories',
                description='Indian multinational pharmaceutical company',
                website='https://www.drreddys.com',
                country='India'
            ),
            'lupin': Manufacturer.objects.create(
                name='Lupin',
                description='Indian multinational pharmaceutical company',
                website='https://www.lupin.com',
                country='India'
            ),
            'aurobindopharma': Manufacturer.objects.create(
                name='Aurobindo Pharma',
                description='Indian multinational pharmaceutical company',
                website='https://www.aurobindo.com',
                country='India'
            ),
            'glenmark': Manufacturer.objects.create(
                name='Glenmark',
                description='Indian multinational pharmaceutical company',
                website='https://www.glenmarkpharma.com',
                country='India'
            ),
            'torrent': Manufacturer.objects.create(
                name='Torrent Pharmaceuticals',
                description='Indian multinational pharmaceutical company',
                website='https://www.torrentpharma.com',
                country='India'
            ),
            'cadila': Manufacturer.objects.create(
                name='Cadila Healthcare',
                description='Indian multinational pharmaceutical company',
                website='https://www.cadilahealthcare.com',
                country='India'
            ),
            'alkem': Manufacturer.objects.create(
                name='Alkem Laboratories',
                description='Indian multinational pharmaceutical company',
                website='https://www.alkemlabs.com',
                country='India'
            ),
            'intas': Manufacturer.objects.create(
                name='Intas Pharmaceuticals',
                description='Indian multinational pharmaceutical company',
                website='https://www.intaspharma.com',
                country='India'
            ),
            'zydus': Manufacturer.objects.create(
                name='Zydus Cadila',
                description='Indian multinational pharmaceutical company',
                website='https://www.zyduscadila.com',
                country='India'
            ),
            'cipla': Manufacturer.objects.create(
                name='Cipla',
                description='Indian multinational pharmaceutical company',
                website='https://www.cipla.com',
                country='India'
            )
        }

        # Create medicines
        medicines = {
            'lisinopril': Medicine.objects.create(
                name='Lisinopril',
                generic_name='Lisinopril',
                form='tablet',
                strength='10mg',
                description='ACE inhibitor used to treat high blood pressure and heart failure',
                composition='Lisinopril dihydrate',
                manufacturer=manufacturers['pfizer'],
                storage_instructions='Store at room temperature between 15-30°C',
                side_effects='Dry cough, dizziness, headache',
                precautions='Not recommended during pregnancy',
                price=25.99,
                requires_prescription=True
            ),
            'metoprolol': Medicine.objects.create(
                name='Metoprolol',
                generic_name='Metoprolol Tartrate',
                form='tablet',
                strength='25mg',
                description='Beta blocker used to treat high blood pressure and angina',
                composition='Metoprolol tartrate',
                manufacturer=manufacturers['astrazeneca'],
                storage_instructions='Store at room temperature below 30°C',
                side_effects='Fatigue, dizziness, depression',
                precautions='Do not stop taking suddenly',
                price=19.99,
                requires_prescription=True
            ),
            'amlodipine': Medicine.objects.create(
                name='Amlodipine',
                generic_name='Amlodipine Besylate',
                form='tablet',
                strength='5mg',
                description='Calcium channel blocker used to treat high blood pressure',
                composition='Amlodipine besylate',
                manufacturer=manufacturers['novartis'],
                storage_instructions='Store at room temperature between 15-30°C',
                side_effects='Edema, dizziness, flushing',
                precautions='May cause gum enlargement',
                price=15.99,
                requires_prescription=True
            ),
            'losartan': Medicine.objects.create(
                name='Losartan',
                generic_name='Losartan Potassium',
                form='tablet',
                strength='50mg',
                description='Angiotensin II receptor blocker used to treat high blood pressure',
                composition='Losartan potassium',
                manufacturer=manufacturers['pfizer'],
                storage_instructions='Store at room temperature below 30°C',
                side_effects='Dizziness, headache, diarrhea',
                precautions='Not recommended during pregnancy',
                price=22.99,
                requires_prescription=True
            ),
            'atenolol': Medicine.objects.create(
                name='Atenolol',
                generic_name='Atenolol',
                form='tablet',
                strength='50mg',
                description='Beta blocker used to treat high blood pressure and angina',
                composition='Atenolol',
                manufacturer=manufacturers['astrazeneca'],
                storage_instructions='Store at room temperature below 30°C',
                side_effects='Fatigue, dizziness, depression',
                precautions='Do not stop taking suddenly',
                price=18.99,
                requires_prescription=True
            ),
            'hydrochlorothiazide': Medicine.objects.create(
                name='Hydrochlorothiazide',
                generic_name='Hydrochlorothiazide',
                form='tablet',
                strength='25mg',
                description='Diuretic used to treat high blood pressure and edema',
                composition='Hydrochlorothiazide',
                manufacturer=manufacturers['novartis'],
                storage_instructions='Store at room temperature between 15-30°C',
                side_effects='Dizziness, headache, nausea',
                precautions='May cause dehydration',
                price=12.99,
                requires_prescription=True
            ),
            'carvedilol': Medicine.objects.create(
                name='Carvedilol',
                generic_name='Carvedilol',
                form='tablet',
                strength='25mg',
                description='Beta blocker used to treat high blood pressure and heart failure',
                composition='Carvedilol',
                manufacturer=manufacturers['pfizer'],
                storage_instructions='Store at room temperature below 30°C',
                side_effects='Fatigue, dizziness, depression',
                precautions='Do not stop taking suddenly',
                price=21.99,
                requires_prescription=True
            ),
            'valsartan': Medicine.objects.create(
                name='Valsartan',
                generic_name='Valsartan',
                form='tablet',
                strength='80mg',
                description='Angiotensin II receptor blocker used to treat high blood pressure',
                composition='Valsartan',
                manufacturer=manufacturers['astrazeneca'],
                storage_instructions='Store at room temperature below 30°C',
                side_effects='Dizziness, headache, diarrhea',
                precautions='Not recommended during pregnancy',
                price=19.99,
                requires_prescription=True
            ),
            'ramipril': Medicine.objects.create(
                name='Ramipril',
                generic_name='Ramipril',
                form='tablet',
                strength='5mg',
                description='ACE inhibitor used to treat high blood pressure and heart failure',
                composition='Ramipril',
                manufacturer=manufacturers['sanofi'],
                storage_instructions='Store at room temperature between 15-30°C',
                side_effects='Dry cough, dizziness, headache',
                precautions='Not recommended during pregnancy',
                price=24.99,
                requires_prescription=True
            ),
            'digoxin': Medicine.objects.create(
                name='Digoxin',
                generic_name='Digoxin',
                form='tablet',
                strength='0.125mg',
                description='Cardiac glycoside used to treat heart failure and atrial fibrillation',
                composition='Digoxin',
                manufacturer=manufacturers['gsk'],
                storage_instructions='Store at room temperature below 25°C',
                side_effects='Nausea, vomiting, irregular heartbeat',
                precautions='Narrow therapeutic window, requires monitoring',
                price=16.99,
                requires_prescription=True
            ),
            'spironolactone': Medicine.objects.create(
                name='Spironolactone',
                generic_name='Spironolactone',
                form='tablet',
                strength='25mg',
                description='Potassium-sparing diuretic used in heart failure and hypertension',
                composition='Spironolactone',
                manufacturer=manufacturers['pfizer'],
                storage_instructions='Store at room temperature below 30°C',
                side_effects='High potassium, breast tenderness',
                precautions='Monitor potassium levels regularly',
                price=20.99,
                requires_prescription=True
            ),
            'clopidogrel': Medicine.objects.create(
                name='Clopidogrel',
                generic_name='Clopidogrel Bisulfate',
                form='tablet',
                strength='75mg',
                description='Antiplatelet agent used to prevent blood clots in cardiovascular diseases',
                composition='Clopidogrel bisulfate',
                manufacturer=manufacturers['sanofi'],
                storage_instructions='Store at room temperature between 15-30°C',
                side_effects='Bleeding, bruising, rash',
                precautions='Monitor for signs of bleeding',
                price=28.99,
                requires_prescription=True
            ),
            'atorvastatin': Medicine.objects.create(
                name='Atorvastatin',
                generic_name='Atorvastatin Calcium',
                form='tablet',
                strength='20mg',
                description='Statin used to lower cholesterol and reduce risk of cardiovascular disease',
                composition='Atorvastatin calcium',
                manufacturer=manufacturers['pfizer'],
                storage_instructions='Store at room temperature below 30°C',
                side_effects='Muscle pain, liver enzyme changes',
                precautions='Monitor liver function tests',
                price=30.99,
                requires_prescription=True
            ),
            'rosuvastatin': Medicine.objects.create(
                name='Rosuvastatin',
                generic_name='Rosuvastatin Calcium',
                form='tablet',
                strength='10mg',
                description='Statin used to lower cholesterol and reduce risk of cardiovascular disease',
                composition='Rosuvastatin calcium',
                manufacturer=manufacturers['astrazeneca'],
                storage_instructions='Store at room temperature below 30°C',
                side_effects='Muscle pain, liver enzyme changes',
                precautions='Monitor liver function tests',
                price=32.99,
                requires_prescription=True
            ),
            'warfarin': Medicine.objects.create(
                name='Warfarin',
                generic_name='Warfarin Sodium',
                form='tablet',
                strength='5mg',
                description='Anticoagulant used to prevent blood clots in cardiovascular diseases',
                composition='Warfarin sodium',
                manufacturer=manufacturers['bayer'],
                storage_instructions='Store at room temperature below 30°C',
                side_effects='Bleeding, bruising, nausea',
                precautions='Monitor INR regularly',
                price=25.99,
                requires_prescription=True
            ),
            'nitroglycerin': Medicine.objects.create(
                name='Nitroglycerin',
                generic_name='Nitroglycerin',
                form='tablet',
                strength='0.4mg',
                description='Vasodilator used to treat angina',
                composition='Nitroglycerin',
                manufacturer=manufacturers['pfizer'],
                storage_instructions='Store at room temperature below 30°C',
                side_effects='Headache, dizziness, flushing',
                precautions='Do not use with PDE5 inhibitors',
                price=22.99,
                requires_prescription=True
            )
        }

        # Create brands
        brands = [
            Brand.objects.create(
                name='Prinivil',
                medicine=medicines['lisinopril'],
                manufacturer=manufacturers['pfizer'],
                is_generic=False,
                price=45.99
            ),
            Brand.objects.create(
                name='Zestril',
                medicine=medicines['lisinopril'],
                manufacturer=manufacturers['astrazeneca'],
                is_generic=False,
                price=42.99
            ),
            Brand.objects.create(
                name='Lopressor',
                medicine=medicines['metoprolol'],
                manufacturer=manufacturers['novartis'],
                is_generic=False,
                price=35.99
            ),
            Brand.objects.create(
                name='Norvasc',
                medicine=medicines['amlodipine'],
                manufacturer=manufacturers['pfizer'],
                is_generic=False,
                price=29.99
            ),
            Brand.objects.create(
                name='Cozaar',
                medicine=medicines['losartan'],
                manufacturer=manufacturers['astrazeneca'],
                is_generic=False,
                price=32.99
            ),
            Brand.objects.create(
                name='Tenormin',
                medicine=medicines['atenolol'],
                manufacturer=manufacturers['novartis'],
                is_generic=False,
                price=28.99
            ),
            Brand.objects.create(
                name='Hyzaar',
                medicine=medicines['losartan'],
                manufacturer=manufacturers['pfizer'],
                is_generic=False,
                price=35.99
            ),
            Brand.objects.create(
                name='Coreg',
                medicine=medicines['carvedilol'],
                manufacturer=manufacturers['astrazeneca'],
                is_generic=False,
                price=31.99
            ),
            Brand.objects.create(
                name='Diovan',
                medicine=medicines['valsartan'],
                manufacturer=manufacturers['novartis'],
                is_generic=False,
                price=27.99
            ),
            Brand.objects.create(
                name='Altace',
                medicine=medicines['ramipril'],
                manufacturer=manufacturers['sanofi'],
                is_generic=False,
                price=39.99
            ),
            Brand.objects.create(
                name='Lanoxin',
                medicine=medicines['digoxin'],
                manufacturer=manufacturers['gsk'],
                is_generic=False,
                price=33.99
            ),
            Brand.objects.create(
                name='Aldactone',
                medicine=medicines['spironolactone'],
                manufacturer=manufacturers['pfizer'],
                is_generic=False,
                price=37.99
            ),
            Brand.objects.create(
                name='Plavix',
                medicine=medicines['clopidogrel'],
                manufacturer=manufacturers['sanofi'],
                is_generic=False,
                price=45.99
            ),
            Brand.objects.create(
                name='Lipitor',
                medicine=medicines['atorvastatin'],
                manufacturer=manufacturers['pfizer'],
                is_generic=False,
                price=49.99
            ),
            Brand.objects.create(
                name='Crestor',
                medicine=medicines['rosuvastatin'],
                manufacturer=manufacturers['astrazeneca'],
                is_generic=False,
                price=52.99
            ),
            Brand.objects.create(
                name='Coumadin',
                medicine=medicines['warfarin'],
                manufacturer=manufacturers['bayer'],
                is_generic=False,
                price=45.99
            ),
            Brand.objects.create(
                name='Nitrostat',
                medicine=medicines['nitroglycerin'],
                manufacturer=manufacturers['pfizer'],
                is_generic=False,
                price=42.99
            ),
            Brand.objects.create(
                name='Amlong',
                medicine=medicines['amlodipine'],
                manufacturer=manufacturers['sunpharma'],
                is_generic=False,
                price=22.99
            ),
            Brand.objects.create(
                name='Losar',
                medicine=medicines['losartan'],
                manufacturer=manufacturers['drreddys'],
                is_generic=False,
                price=27.99
            ),
            Brand.objects.create(
                name='Aten',
                medicine=medicines['atenolol'],
                manufacturer=manufacturers['cipla'],
                is_generic=False,
                price=20.99
            ),
            Brand.objects.create(
                name='Cardivas',
                medicine=medicines['carvedilol'],
                manufacturer=manufacturers['sunpharma'],
                is_generic=False,
                price=24.99
            ),
            Brand.objects.create(
                name='Valzaar',
                medicine=medicines['valsartan'],
                manufacturer=manufacturers['torrent'],
                is_generic=False,
                price=29.99
            ),
            Brand.objects.create(
                name='Ramistar',
                medicine=medicines['ramipril'],
                manufacturer=manufacturers['cipla'],
                is_generic=False,
                price=26.99
            ),
            Brand.objects.create(
                name='Digene',
                medicine=medicines['digoxin'],
                manufacturer=manufacturers['abbott'],
                is_generic=False,
                price=19.99
            ),
            Brand.objects.create(
                name='Aldactone',
                medicine=medicines['spironolactone'],
                manufacturer=manufacturers['cipla'],
                is_generic=False,
                price=23.99
            ),
            Brand.objects.create(
                name='Clopilet',
                medicine=medicines['clopidogrel'],
                manufacturer=manufacturers['sunpharma'],
                is_generic=False,
                price=32.99
            ),
            Brand.objects.create(
                name='Storvas',
                medicine=medicines['atorvastatin'],
                manufacturer=manufacturers['sunpharma'],
                is_generic=False,
                price=34.99
            ),
            Brand.objects.create(
                name='Rozavel',
                medicine=medicines['rosuvastatin'],
                manufacturer=manufacturers['cipla'],
                is_generic=False,
                price=37.99
            ),
            Brand.objects.create(
                name='Acitrom',
                medicine=medicines['warfarin'],
                manufacturer=manufacturers['cipla'],
                is_generic=False,
                price=28.99
            ),
            Brand.objects.create(
                name='Angispan',
                medicine=medicines['nitroglycerin'],
                manufacturer=manufacturers['sunpharma'],
                is_generic=False,
                price=30.99
            ),
            Brand.objects.create(
                name='Atorlip',
                medicine=medicines['atorvastatin'],
                manufacturer=manufacturers['cipla'],
                is_generic=True,
                price=18.99
            ),
            Brand.objects.create(
                name='Amlozaar',
                medicine=medicines['amlodipine'],
                manufacturer=manufacturers['zydus'],
                is_generic=True,
                price=15.99
            ),
            Brand.objects.create(
                name='Telsar',
                medicine=medicines['losartan'],
                manufacturer=manufacturers['glenmark'],
                is_generic=True,
                price=16.99
            ),
            Brand.objects.create(
                name='Ramitor',
                medicine=medicines['ramipril'],
                manufacturer=manufacturers['torrent'],
                is_generic=True,
                price=17.99
            ),
            Brand.objects.create(
                name='Cardace',
                medicine=medicines['ramipril'],
                manufacturer=manufacturers['lupin'],
                is_generic=True,
                price=19.99
            ),
            Brand.objects.create(
                name='Starpress',
                medicine=medicines['metoprolol'],
                manufacturer=manufacturers['sunpharma'],
                is_generic=True,
                price=14.99
            )

        ]

        self.stdout.write(self.style.SUCCESS('Successfully loaded cardiovascular medicines data'))
