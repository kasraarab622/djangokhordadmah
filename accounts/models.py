from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    picture = models.ImageField(upload_to="profile_picture")

    def __str__(self):
        return f'{self.bio}'