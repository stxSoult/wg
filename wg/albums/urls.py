from django.conf.urls import url
from wg.albums.views import AlbumList, AlbumDetail, UploadPicture

urlpatterns = [

    url(r'upload_picture/$',
        UploadPicture.as_view(),
        name='upload_picture'),

    url(r'^(?P<user>[0-9a-zA-Z]+)/albums/$',
        AlbumList.as_view(),
        name='album-list'),

    url(r'^(?P<user>[0-9a-zA-Z]+)/albums/(?P<pk>[0-9]+)/$',
        AlbumDetail.as_view(),
        name='album-detail')

]
