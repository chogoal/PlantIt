# Generated by Django 3.2.6 on 2021-08-25 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(null=True, upload_to='challengeapp/')),
                ('content', models.TextField(null=True)),
                ('success', models.BooleanField(default=False)),
            ],
        ),
    ]