# Generated by Django 2.0.7 on 2018-08-29 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelguide', '0006_hotel_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='pcity',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]