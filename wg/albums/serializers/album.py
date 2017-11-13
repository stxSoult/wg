from django.utils.translation import ugettext as _
from rest_framework import serializers
from wg.albums.models import UserAlbum


class AlbumSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='albums:album-detail',
                                               lookup_field='pk')
    user = serializers.StringRelatedField()

    class Meta:
        model = UserAlbum
        fields = ('url', 'name', 'user')


class AlbumCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAlbum
        fields = ('name',)


class AlbumEditSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAlbum
        fields = ('name',)
