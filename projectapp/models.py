from django.db import models

# Create your models here.


class Project(models.Model):
    PROJECT_LIST = [
        ('정보', '정보게시판'),
        ('자랑', '자랑게시판'),
        ('챌린지', '챌린지'),
    ]

    name = models.CharField(max_length=20, choices=PROJECT_LIST, null=False, unique=True)
    description = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.name}'
