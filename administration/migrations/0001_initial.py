# Generated by Django 3.1.4 on 2021-01-11 01:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_submitted', models.DateTimeField(auto_now=True)),
                ('product_id_list', models.CharField(max_length=40)),
                ('status', models.CharField(blank=True, choices=[('NEW', 'New'), ('LABELS_GENERATED', 'Labels generated'), ('SHIPPED', 'Shipped'), ('ARRIVED_AT_FACILITY', 'Arrived at facility'), ('CLOSED_ITEMS_RETURNED', 'Closed items returned')], default='NEW', max_length=40)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
