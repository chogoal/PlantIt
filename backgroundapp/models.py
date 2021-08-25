from django.db import models

# Create your models here.
from django.views.generic import ListView


class Background(models.Model):
    # image = models.ImageField()
    image = models.ImageField(upload_to='background/', null=False)
    price = models.IntegerField(default=15)
