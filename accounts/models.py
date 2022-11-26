from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

class CustomUser(AbstractUser): # creating the custom user model
    # add new fields here
    pass 

    def __str__(self):
        return self.username


class Profile(models.Model):
    ''' the model for user profile'''
    # one to one relation one user = one profile
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
