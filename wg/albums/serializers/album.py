from rest_framework import serializers
from django.shortcuts import reverse
from wg.albums.models import UserAlbum
from wg.serializers import UserRelatedObjectLinkField
from wg.albums.serializers import PictureSerializer


class AlbumSerializer(serializers.ModelSerializer):
    url = UserRelatedObjectLinkField(view_name='albums:album-detail')
    pictures = PictureSerializer(many=True)

    class Meta:
        model = UserAlbum
        fields = ('url', 'id', 'name', 'pictures')


class AlbumCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAlbum
        fields = ('name',)


class AlbumEditSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(method_name='get_owner')
    pictures = PictureSerializer(many=True, read_only=True)

    class Meta:
        model = UserAlbum
        fields = ('user', 'name', 'pictures')

    def get_owner(self, album):
        request = self.context.get('request')
        return request.build_absolute_uri(
            reverse('user-detail',
                    kwargs={'user': album.user.username or album.user.pk}))
