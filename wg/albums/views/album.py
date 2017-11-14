from django.db import IntegrityError
from django.utils.translation import ugettext as _
from rest_framework import status
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import SAFE_METHODS
from rest_framework.response import Response
# ==
from wg.albums.models import UserAlbum
from wg.albums.serializers import (AlbumSerializer,
                                   AlbumCreateSerializer,
                                   AlbumEditSerializer)
from wg.permissions import IsOwnerOrReadOnly
from wg.albums.serializers import PictureSerializer


class AlbumList(GenericAPIView):
    def get_queryset(self):
        return UserAlbum.objects.filter(user=self.kwargs.get('user'))

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AlbumCreateSerializer
        return AlbumSerializer

    def get(self, request, *args, **kwargs):
        context = {'request': request}

        return Response(
            AlbumSerializer(self.get_queryset(),
                            many=True,
                            context=context).data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            try:
                serializer.save(user=request.user)
            except IntegrityError:
                return Response({'Error': _('Album already exist')})
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class AlbumDetail(RetrieveUpdateDestroyAPIView):
    queryset = UserAlbum.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = AlbumEditSerializer

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return AlbumSerializer
        return AlbumEditSerializer

    def put(self, request, *args, **kwargs):
        try:
            response = self.update(request, *args, **kwargs)
            return response
        except IntegrityError:
            return Response({
                'Error': _(f'Album "{request.data.get("name")}" already exist')
            })
