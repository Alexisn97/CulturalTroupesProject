# Generated by Django 5.0.4 on 2024-05-16 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcoApp', '0004_rename_amount_booking_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='Amount',
            field=models.IntegerField(default=0),
        ),
    ]
