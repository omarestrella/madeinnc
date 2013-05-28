from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=255, unique=True)
    url = models.URLField(max_length=255, unique=True)
    description = models.TextField()
    authorized = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
