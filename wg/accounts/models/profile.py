from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _

GENDERS = (
    (None, 'Gender'),
    ('f', _('Female')),
    ('m', _('Male'))
)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='profile')

    country = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=150, blank=True)
    gender = models.CharField(max_length=1, choices=GENDERS,
                              blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

