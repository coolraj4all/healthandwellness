# Generated by Django 5.1.5 on 2025-03-01 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("medical_records", "0005_alter_patienthealthdetails_heart_rate_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="patienthealthdetails",
            name="provisional_diagnosis",
            field=models.TextField(blank=True, null=True),
        ),
    ]
