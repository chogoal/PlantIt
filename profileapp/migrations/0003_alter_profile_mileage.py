# Generated by Django 3.2.6 on 2021-08-27 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0002_profile_mileage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mileage',
            field=models.IntegerField(default=100, null=True),
        ),
    ]
