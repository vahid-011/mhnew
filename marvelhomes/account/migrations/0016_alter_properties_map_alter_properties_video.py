# Generated by Django 5.0.6 on 2024-06-12 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_properties_map_properties_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='properties',
            name='map',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='properties',
            name='video',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
