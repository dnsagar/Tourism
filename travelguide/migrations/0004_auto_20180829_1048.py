# Generated by Django 2.0.7 on 2018-08-29 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelguide', '0003_place_prating'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='himage1',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hotel',
            name='himage2',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hotel',
            name='himage3',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]