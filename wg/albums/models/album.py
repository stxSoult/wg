from django.conf import settings
from django.db import models

from wg.models import DateModel


class UserAlbum(DateModel):
    name = models.CharField(max_length=250)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='pictures')
    pictures = models.ManyToManyField('Picture',
                                      related_name='albums')

    class Meta:
        unique_together = ('name', 'user')

    def __str__(self):
        return self.name
