# Generated by Django 3.1.4 on 2021-01-05 00:43

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('therapybox', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='therapyboxtemplate',
            name='image_2',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='therapyboxtemplate',
            name='image_3',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image'),
        ),
    ]