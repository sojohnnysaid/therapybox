# Generated by Django 3.1.4 on 2021-01-12 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('therapybox', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='therapyboxtemplate',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=6),
            preserve_default=False,
        ),
    ]
