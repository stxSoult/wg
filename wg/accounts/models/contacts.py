from django.db import models
from django.conf import settings


class AdditionalEmail(models.Model):
    user = models.ManyToManyField(settings.AUTH_USER_MODEL)
    email = models.EmailField(max_length=150, unique=True)
    confirmed = models.BooleanField(default=False)
