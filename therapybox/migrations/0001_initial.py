# Generated by Django 3.1.4 on 2021-01-04 13:11

import cloudinary.models
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
        migrations.CreateModel(
            name='TherapyBoxTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=128)),
                ('image_1', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('image_2', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('image_3', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('image_4', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('tags', models.CharField(max_length=128)),
                ('length', models.CharField(help_text='Approx mm', max_length=128)),
                ('height', models.CharField(help_text='Approx mm', max_length=128)),
                ('depth', models.CharField(help_text='Approx mm', max_length=128)),
                ('weight', models.CharField(help_text='Approx kg', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='TherapyBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, choices=[('STORAGE', 'Storage')], max_length=40)),
                ('status', models.CharField(blank=True, choices=[('AVAILABLE', 'Available'), ('REGION_2', 'Region 2')], max_length=40)),
                ('condition', models.CharField(blank=True, choices=[('GOOD', 'Good'), ('BROKEN', 'Broken'), ('MISSING', 'Missing'), ('UNDER_DEVELOPMENT', 'Under development'), ('WAITING_FOR_PART', 'Waiting for a part')], max_length=40)),
                ('due_back', models.DateField(blank=True, null=True)),
                ('notes', models.TextField()),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='therapybox.therapyboxtemplate')),
            ],
            options={
                'ordering': ['due_back'],
            },
        ),
    ]
