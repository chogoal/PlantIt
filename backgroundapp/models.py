from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.views.generic import ListView


class Background(models.Model):
    # image = models.ImageField()
    image = models.ImageField(upload_to='background/', null=False)
    price = models.IntegerField(default=15)
    state = models.CharField(max_length=10, default='unsold')

#
# class Purchasing(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE,
#                              related_name='shop', null=False)
#     background = models.ForeignKey(Background, on_delete=models.CASCADE,
#                                    related_name='shop', null=False)
#
#     class Meta:
#         unique_together = ['user', 'background']
