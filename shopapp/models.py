from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from backgroundapp.models import Background


class Purchasing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='shop', null=False)
    background = models.ForeignKey(Background, on_delete=models.CASCADE,
                                   related_name='shop', null=False)
