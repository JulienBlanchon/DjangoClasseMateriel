# Generated by Django 5.0.6 on 2024-05-27 14:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prets', '0003_accessoire_emprunt_lieu_emprunt_objectif_utilisation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessoire',
            name='materiel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prets.materiel'),
        ),
    ]