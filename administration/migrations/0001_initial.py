# Generated by Django 3.1.4 on 2021-01-11 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_submitted', models.DateField(auto_now_add=True)),
                ('product_id_list', models.CharField(max_length=40)),
                ('status', models.CharField(blank=True, choices=[('1', 'New'), ('2', 'Labels generated'), ('3', 'Shipped'), ('4', 'Arrived at facility'), ('5', 'Closed items returned')], default=1, max_length=40)),
            ],
            options={
                'ordering': ['status'],
            },
        ),
    ]
