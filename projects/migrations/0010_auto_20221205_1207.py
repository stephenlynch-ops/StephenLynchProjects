# Generated by Django 3.2.16 on 2022-12-05 12:07

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_alter_project_image1'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image4',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image4'),
        ),
        migrations.AddField(
            model_name='project',
            name='image4_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='image5',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image5'),
        ),
        migrations.AddField(
            model_name='project',
            name='image5_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='image6',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image6'),
        ),
        migrations.AddField(
            model_name='project',
            name='image6_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]
