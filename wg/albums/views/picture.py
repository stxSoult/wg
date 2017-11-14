from rest_framework.generics import CreateAPIView
from wg.albums.serializers import PictureSerializer


class UploadPicture(CreateAPIView):
    serializer_class = PictureSerializer
