# Generated by Django 5.0.6 on 2024-06-12 05:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_alter_properties_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertydetails',
            name='property',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='detail', to='account.properties'),
        ),
    ]