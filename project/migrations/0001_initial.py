# Generated by Django 4.1.1 on 2022-11-09 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.basemodel')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            bases=('core.basemodel',),
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.basemodel')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Image')),
                ('social_networks', models.JSONField(verbose_name='Social networks')),
            ],
            bases=('core.basemodel',),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.basemodel')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('logo', models.ImageField(upload_to='', verbose_name='Logo')),
                ('initial_date', models.DateField(verbose_name='Initial date')),
                ('latitud', models.FloatField(verbose_name='Latitud')),
                ('longitude', models.FloatField(verbose_name='Longitude')),
                ('address', models.CharField(max_length=100, verbose_name='Address')),
                ('phone', models.CharField(max_length=100, verbose_name='Phone')),
                ('brochure', models.FileField(upload_to='', verbose_name='Brochure')),
                ('social_networks', models.JSONField(verbose_name='Social networks')),
                ('levels', models.SmallIntegerField(default=1, verbose_name='Niveles')),
                ('colony_field', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='location.colony')),
                ('developer_field', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='project.developer')),
            ],
            bases=('core.basemodel',),
        ),
    ]
