from django.contrib.auth.models import BaseUserManager
from django.db.models import Q


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **kwargs):
        """
        Create and save user with given email and password
        """
        if not email:
            raise ValueError('Email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        defaults = {'is_superuser': False,
                    'is_staff': False}
        extra_fields.update(defaults)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        defaults = {'is_superuser': True,
                    'is_staff': True}
        extra_fields.update(defaults)

        if not extra_fields.get('is_superuser', False):
            raise ValueError('Superuser must have "is_superuser" attribute'
                             'set to "True"')
        return self._create_user(email, password,   **extra_fields)

    def get_by_natural_key(self, username):
        case_insensitive_username_field = '{}__iexact'.format(
            self.model.USERNAME_FIELD)
        return self.get(**{case_insensitive_username_field: username})