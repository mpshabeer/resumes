# Generated by Django 3.2.18 on 2023-07-09 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resmesdetails',
            name='phone',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='resmesdetails',
            name='year',
            field=models.IntegerField(max_length=100),
        ),
    ]
