# Generated by Django 5.0.4 on 2024-05-16 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcoApp', '0010_booking_performance_type_alter_booking_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='Performance_Type',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
