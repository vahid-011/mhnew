# Generated by Django 5.0.6 on 2024-06-13 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0018_alter_properties_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='properties',
            name='map',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='properties',
            name='video',
            field=models.URLField(null=True),
        ),
    ]