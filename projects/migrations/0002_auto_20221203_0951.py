# Generated by Django 3.2.16 on 2022-12-03 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link_to_repo',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='link_to_site',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
