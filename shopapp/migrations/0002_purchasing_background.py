# Generated by Django 3.2.6 on 2021-08-27 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backgroundapp', '0005_delete_background_dot'),
        ('shopapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasing',
            name='background',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='shop', to='backgroundapp.background'),
            preserve_default=False,
        ),
    ]