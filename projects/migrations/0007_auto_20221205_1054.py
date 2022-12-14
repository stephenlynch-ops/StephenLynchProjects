# Generated by Django 3.2.16 on 2022-12-05 10:54

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20221204_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image1',
            field=cloudinary.models.CloudinaryField(blank=True, default='placeholder', max_length=255, null=True, verbose_name='image1'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image2',
            field=cloudinary.models.CloudinaryField(blank=True, default='placeholder', max_length=255, null=True, verbose_name='image2'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image3',
            field=cloudinary.models.CloudinaryField(blank=True, default='placeholder', max_length=255, null=True, verbose_name='image3'),
        ),
    ]
