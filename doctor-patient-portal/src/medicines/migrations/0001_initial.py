# Generated by Django 5.1.5 on 2025-03-01 11:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("diseases", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Manufacturer",
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
                ("description", models.TextField(blank=True)),
                ("website", models.URLField(blank=True)),
                ("country", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Medicine",
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
                ("generic_name", models.CharField(max_length=200)),
                (
                    "form",
                    models.CharField(
                        choices=[
                            ("tablet", "Tablet"),
                            ("capsule", "Capsule"),
                            ("liquid", "Liquid"),
                            ("injection", "Injection"),
                            ("topical", "Topical"),
                            ("inhaler", "Inhaler"),
                            ("drops", "Drops"),
                        ],
                        max_length=20,
                    ),
                ),
                ("strength", models.CharField(max_length=50)),
                ("description", models.TextField()),
                ("composition", models.TextField()),
                ("storage_instructions", models.TextField(blank=True)),
                ("side_effects", models.TextField(blank=True)),
                ("precautions", models.TextField(blank=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("requires_prescription", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "manufacturer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="medicines.manufacturer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MedicineRecommendation",
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
                (
                    "recommendation_type",
                    models.CharField(
                        choices=[
                            ("FIRST_LINE", "First Line Treatment"),
                            ("SECOND_LINE", "Second Line Treatment"),
                            ("ALTERNATIVE", "Alternative Treatment"),
                        ],
                        max_length=50,
                    ),
                ),
                ("special_instructions", models.TextField(blank=True)),
                ("contraindications", models.TextField(blank=True)),
                (
                    "effectiveness_rating",
                    models.IntegerField(
                        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
                    ),
                ),
                (
                    "evidence_level",
                    models.CharField(
                        choices=[
                            ("HIGH", "High Quality Evidence"),
                            ("MODERATE", "Moderate Quality Evidence"),
                            ("LOW", "Low Quality Evidence"),
                        ],
                        max_length=50,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "disease",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="diseases.disease",
                    ),
                ),
                (
                    "medicine_recommendations",
                    models.ManyToManyField(
                        related_name="alternative_recommendations",
                        to="medicines.medicine",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Brand",
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
                ("is_generic", models.BooleanField(default=False)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "manufacturer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="medicines.manufacturer",
                    ),
                ),
                (
                    "medicine",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="brands",
                        to="medicines.medicine",
                    ),
                ),
            ],
            options={
                "unique_together": {("name", "manufacturer")},
            },
        ),
    ]
