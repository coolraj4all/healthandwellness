# Generated by Django 5.1.5 on 2025-02-16 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "medical_records",
            "0002_patienthealthdetails_patientmedicinedetails_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="patienthealthdetails",
            name="blood_pressure",
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name="patienthealthdetails",
            name="cns",
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name="patienthealthdetails",
            name="cvs",
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name="patienthealthdetails",
            name="follow_up_date",
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name="patienthealthdetails",
            name="heart_rate",
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name="patienthealthdetails",
            name="p_a",
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name="patienthealthdetails",
            name="rr",
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name="patienthealthdetails",
            name="rs",
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name="patienthealthdetails",
            name="sleep_hours",
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3),
        ),
        migrations.AlterField(
            model_name="patienthealthdetails",
            name="spo2",
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name="patienthealthdetails",
            name="temperature",
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4),
        ),
    ]
