# Generated by Django 3.0.3 on 2020-02-26 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relocation', '0006_adresse_typeadresse'),
    ]

    operations = [
        migrations.AddField(
            model_name='demenagement',
            name='option_supplementaires',
            field=models.ManyToManyField(through='relocation.DemenagementOptionsSupplementaire', to='relocation.OptionSupplementaire'),
        ),
    ]
