from rest_framework import serializers
from rest_framework.reverse import reverse
from wg.shortcuts import get_user


class UserRelatedObjectLinkField(serializers.HyperlinkedIdentityField):
    """
    Update reverse kwargs with 'user' for /<username_or_id>/object/<pk>
    """

    def get_url(self, obj, view_name, request, format, **kwargs):
        user = {'user': [x for x in request.path.split('/') if x][0]}
        url_kwargs = {
            'pk': obj.pk,
            'user': get_user(**user).pk
        }
        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)

