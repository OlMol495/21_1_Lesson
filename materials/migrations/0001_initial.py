# Generated by Django 5.0.1 on 2024-01-10 15:23

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Material",
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
                ("title", models.CharField(max_length=150, verbose_name="Заголовок")),
                ("body", models.TextField(verbose_name="Текст")),
            ],
            options={
                "verbose_name": "Материал",
                "verbose_name_plural": "Материалы",
            },
        ),
    ]
