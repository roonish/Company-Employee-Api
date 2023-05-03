# Generated by Django 4.2 on 2023-05-03 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Employee",
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
                ("name", models.CharField(max_length=50)),
                ("email", models.CharField(max_length=50)),
                ("address", models.CharField(max_length=50)),
                ("phone", models.IntegerField()),
                ("bio", models.TextField()),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("Intern", "Intern"),
                            ("Junior", "Junior"),
                            ("Senior", "Senior"),
                            ("Lead", "Lead"),
                        ],
                        max_length=100,
                    ),
                ),
                ("joined_date", models.DateTimeField()),
                ("isFullTime", models.BooleanField(default=False)),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.company"
                    ),
                ),
            ],
        ),
    ]