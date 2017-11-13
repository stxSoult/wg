from django.conf.urls import url
from wg.albums.views import AlbumList, AlbumDetail

urlpatterns = [
    url(r'^albums/$',
        AlbumList.as_view(),
        name='album-list'),


    url(r'^albums/(?P<pk>[0-9]+)/$',
        AlbumDetail.as_view(),
        name='album-detail')
]
