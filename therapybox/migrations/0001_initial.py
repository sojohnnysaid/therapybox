# Generated by Django 3.1.4 on 2021-01-04 01:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TherapyBoxUser',
            fields=[
                ('myabstractuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.myabstractuser')),
                ('facility_name', models.CharField(blank=True, max_length=128)),
                ('company_name', models.CharField(blank=True, max_length=128)),
                ('phone_number', models.CharField(blank=True, max_length=128)),
                ('point_of_contact', models.CharField(blank=True, max_length=128)),
                ('address_line_1', models.CharField(blank=True, max_length=128)),
                ('address_line_2', models.CharField(blank=True, max_length=128)),
                ('suburb', models.CharField(blank=True, max_length=128)),
                ('city', models.CharField(blank=True, max_length=128)),
                ('postcode', models.CharField(blank=True, max_length=128)),
                ('shipping_region', models.CharField(blank=True, choices=[('REGION_1', 'Region 1'), ('REGION_2', 'Region 2')], max_length=40)),
                ('agreed_to_terms_and_conditions', models.BooleanField(blank=True, default=False)),
                ('is_approved', models.BooleanField(blank=True, default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('users.myabstractuser',),
        ),
    ]