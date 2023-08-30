from django.db import models
from django.contrib.auth.models import AbstractUser, User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='users/', null=True, blank=True)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    objects = models.Manager()
    def __str__(self):
        return f"{self.user.username}'s profile"