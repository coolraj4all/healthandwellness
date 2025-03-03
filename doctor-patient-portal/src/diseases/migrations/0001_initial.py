# Generated by Django 5.1.5 on 2025-03-01 11:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DiseaseCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "parent_category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="diseases.diseasecategory",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Disease Categories",
            },
        ),
        migrations.CreateModel(
            name="Disease",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("scientific_name", models.CharField(blank=True, max_length=200)),
                ("description", models.TextField()),
                ("symptoms", models.TextField()),
                ("causes", models.TextField()),
                ("treatment", models.TextField()),
                (
                    "severity_level",
                    models.IntegerField(
                        choices=[
                            (1, "Mild"),
                            (2, "Moderate"),
                            (3, "Severe"),
                            (4, "Critical"),
                        ]
                    ),
                ),
                ("is_contagious", models.BooleanField(default=False)),
                ("incubation_period", models.CharField(blank=True, max_length=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="diseases.diseasecategory",
                    ),
                ),
            ],
        ),
    ]
