from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# when a user is saved, a signel and data are sent to the profile's page
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:  # means that 'if the user is created'
        Profile.objects.create(user=instance)


def saveprofile(sender, instance, **kwargs):
    instance.Profile.save()
