# Generated by Django 4.2.1 on 2023-06-26 01:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rendez_vous',
            name='date_fin',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 26, 4, 5, 28, 131027)),
        ),
        migrations.AddField(
            model_name='rendez_vous',
            name='duree',
            field=models.IntegerField(default=1),
        ),
    ]