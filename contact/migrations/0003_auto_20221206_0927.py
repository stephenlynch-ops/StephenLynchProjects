# Generated by Django 3.2.16 on 2022-12-06 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20221205_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='user_image',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='user_name',
        ),
    ]