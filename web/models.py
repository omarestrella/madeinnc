from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
