# Generated by Django 5.0.6 on 2024-07-04 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("galeria", "0002_fotografia_categoria"),
    ]

    operations = [
        migrations.AddField(
            model_name="fotografia",
            name="publicada",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="fotografia",
            name="categoria",
            field=models.CharField(
                choices=[
                    ("NEBULOSA", "Nebulosa"),
                    ("ESTRELA", "Estrela"),
                    ("GALÁXIA", "Galáxica"),
                    ("PLANETA", "Planeta"),
                    ("SATÉLITE", "Satélite"),
                ],
                default="",
                max_length=100,
            ),
        ),
    ]
