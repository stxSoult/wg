from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='profile')
    picture = models.ImageField(upload_to='pictures/profile',
                                blank=True, null=True)

    country = models.CharField(max_length=100)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
