from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from .models import Profile
# overwriting the user creation and user saving to create a new profile when a new user is created


# create a profile when a user is created
@receiver(post_save, sender=get_user_model())
def create_user_profile(sender, instance, created, **kwargs): 
    if created:
        Profile.objects.create(user = instance)


# saves the profile when the user is saved
@receiver(post_save, sender=get_user_model())
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()