# Generated by Django 5.0.4 on 2024-05-16 16:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcoApp', '0012_remove_booking_performance_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='Performance_Type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='EcoApp.event'),
        ),
    ]