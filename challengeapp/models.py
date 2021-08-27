from django.db import models

# Create your models here.


class Challenge(models.Model):
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='challengeapp/', null=True)
    content = models.TextField(null=True)

    success = models.BooleanField(default=False)  # 챌린지 성공 유무