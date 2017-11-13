from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from wg.shortcuts.models import DateModel


class UserAlbum(DateModel):
    name = models.CharField(max_length=250)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='pictures')
    pictures = models.ManyToManyField('Picture',
                                      related_name='album')

    class Meta:
        unique_together = ('name', 'user')
