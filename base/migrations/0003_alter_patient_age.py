# Generated by Django 4.0.3 on 2022-03-23 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_patient_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.CharField(max_length=3),
        ),
    ]
