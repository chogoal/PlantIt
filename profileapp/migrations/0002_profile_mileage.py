# Generated by Django 3.2.6 on 2021-08-27 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='mileage',
            field=models.IntegerField(default=100),
        ),
    ]
