# Generated by Django 3.2.18 on 2023-07-09 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='resmesdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('gender', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=100)),
                ('specilization', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('college', models.CharField(max_length=100)),
                ('resume', models.CharField(max_length=100)),
            ],
        ),
    ]
