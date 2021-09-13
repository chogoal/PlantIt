from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Challenge(models.Model):
    writer = models.OneToOneField(User, on_delete=models.CASCADE, related_name='challenge', null=True, blank=True)
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='challenge/', null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    success = models.BooleanField(default=False)  # 챌린지 성공 유무