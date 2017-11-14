from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    response = {}
    if request.user.is_authenticated():
        user_links = {
            'current_user': reverse('user-detail',
                                    request=request,
                                    kwargs={'user': request.user.pk}),
            'current_user_albums': reverse('albums:album-list',
                                           request=request,
                                           kwargs={'user': request.user.pk}),
        }
        response.update(user_links)
    else:
        response.update({'login': reverse('rest_framework:login',
                                          request=request) + '?next=/'})

    response.update({
        'users': reverse('accounts:user-list', request=request, format=format),

    })
    return Response(response)


urlpatterns = [
      url(r'^$', api_root),
      url(r'^', include('wg.accounts.urls', namespace='accounts')),
      url(r'^', include('wg.albums.urls', namespace='albums')),

      url(r'^admin/', admin.site.urls),
      url(r'^api-auth/',
          include('rest_framework.urls',
                  namespace='rest_framework')),

      url(r'^(?P<user>[0-9a-zA-Z]+)/', include('wg.accounts.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
