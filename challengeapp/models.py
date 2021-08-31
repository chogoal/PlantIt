from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Challenge(models.Model):
    writer = models.OneToOneField(User, on_delete=models.CASCADE, related_name='challenge')
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='challenge/', null=True)
    content = models.TextField(null=True)

    success = models.BooleanField(default=False)  # 챌린지 성공 유무