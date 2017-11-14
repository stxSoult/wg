from django.shortcuts import get_object_or_404
from wg.accounts.models import User


def get_user(**kwargs):
    try:
        user = User.objects.get(username__iexact=kwargs.get('user'))
    except User.DoesNotExist:
        user = get_object_or_404(User, pk=kwargs.get('user'))
    return user
