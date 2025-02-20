from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    about_me = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(upload_to="users/profile-images/")

    def __str__(self):
        return self.username
