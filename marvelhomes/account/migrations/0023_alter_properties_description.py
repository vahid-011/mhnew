# Generated by Django 5.0.6 on 2024-06-14 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0022_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='properties',
            name='description',
            field=models.TextField(max_length=30000),
        ),
    ]
