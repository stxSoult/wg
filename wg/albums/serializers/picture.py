from rest_framework.serializers import (ModelSerializer,)

from wg.albums.models import UserAlbum, Picture


class PictureSerializer(ModelSerializer):

    class Meta:
        model = Picture
        fields = ('image', 'comment', 'albums')

    def get_fields(self):
        fields = super(PictureSerializer, self).get_fields()
        user = self.context['request'].user

        fields['albums'].child_relation.queryset = UserAlbum.objects.filter(
            user=user
        )
        return fields
