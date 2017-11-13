from django.db import models
from django.conf import settings


class Picture(models.Model):
    name = models.CharField(max_length=250, blank=True)
    image = models.ImageField(upload_to='pictures/')
