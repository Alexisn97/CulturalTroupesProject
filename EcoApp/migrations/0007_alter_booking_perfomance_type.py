# Generated by Django 5.0.4 on 2024-05-16 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcoApp', '0006_booking_perfomance_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='Perfomance_Type',
            field=models.CharField(max_length=50),
        ),
    ]
