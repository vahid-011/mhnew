# Generated by Django 5.0.6 on 2024-06-11 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_properties_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='properties',
            name='company',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
