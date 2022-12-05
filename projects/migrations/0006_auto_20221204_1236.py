# Generated by Django 3.2.16 on 2022-12-04 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_rename_langauage_summary_project_language_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image1_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='image2_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='image3_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]