from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    occupation = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.username
