from django.db import models

# Create your models here.


class UserProfile(models.Model):
    full_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    github = models.URLField(null=True)
    linkedin = models.URLField(null=True)
