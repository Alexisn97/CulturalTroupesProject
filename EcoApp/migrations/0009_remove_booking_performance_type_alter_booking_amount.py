# Generated by Django 5.0.4 on 2024-05-16 14:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcoApp', '0008_remove_booking_perfomance_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='Performance_Type',
        ),
        migrations.AlterField(
            model_name='booking',
            name='Amount',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EcoApp.event'),
        ),
    ]
