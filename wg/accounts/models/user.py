from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from rest_framework.authtoken.models import Token

from wg.accounts.managers.user import UserManager
from wg.accounts.models import Profile


class User(AbstractBaseUser, PermissionsMixin):
    date_joined = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=150, unique=True)
    email_confirmed = models.BooleanField(default=False)
    username = models.CharField(max_length=100, unique=True,
                                null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_short_name(self):
        return

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_token(instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
