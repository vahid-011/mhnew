# Generated by Django 5.0.6 on 2024-06-11 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_paymentdetails_propertydetails_properties'),
    ]

    operations = [
        migrations.AlterField(
            model_name='properties',
            name='description',
            field=models.CharField(max_length=800),
        ),
        migrations.AlterField(
            model_name='properties',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
