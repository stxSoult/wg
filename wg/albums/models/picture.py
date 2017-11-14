from django.db import models

from wg.models import DateModel


class Picture(DateModel):
    comment = models.CharField(max_length=2000, blank=True)
    image = models.ImageField(upload_to='pictures/')

