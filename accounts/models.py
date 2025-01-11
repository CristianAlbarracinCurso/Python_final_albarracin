from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    biography = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    pass