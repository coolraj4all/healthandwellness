# Generated by Django 5.1.5 on 2025-02-01 10:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PatientMedicalHistory",
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
                ("condition_name", models.CharField(max_length=200)),
                ("diagnosis_date", models.DateField()),
                ("current_status", models.CharField(max_length=100)),
                ("treatment", models.TextField()),
                ("notes", models.TextField(blank=True)),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="medical_histories",
                        to="accounts.patient",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PatientMedication",
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
                ("dosage", models.CharField(max_length=100)),
                (
                    "frequency",
                    models.CharField(
                        choices=[
                            ("ONCE", "Once daily"),
                            ("TWICE", "Twice daily"),
                            ("THRICE", "Thrice daily"),
                            ("FOUR", "Four times daily"),
                            ("AS_NEEDED", "As needed"),
                            ("OTHER", "Other"),
                        ],
                        max_length=10,
                    ),
                ),
                ("start_date", models.DateField()),
                ("end_date", models.DateField(blank=True, null=True)),
                ("prescribing_doctor", models.CharField(max_length=200)),
                ("reason", models.TextField()),
                ("side_effects", models.TextField(blank=True)),
                ("notes", models.TextField(blank=True)),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="medications",
                        to="accounts.patient",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PatientSurgicalHistory",
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
                ("surgery_name", models.CharField(max_length=200)),
                ("surgery_date", models.DateField()),
                ("hospital", models.CharField(max_length=200)),
                ("surgeon", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("complications", models.TextField(blank=True)),
                ("recovery_notes", models.TextField(blank=True)),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="surgical_histories",
                        to="accounts.patient",
                    ),
                ),
            ],
        ),
    ]
