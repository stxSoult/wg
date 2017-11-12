from django.conf.urls import url, include
from django.contrib import admin

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('accounts:user-list', request=request, format=format),
    })


urlpatterns = [
    url(r'^$', api_root),
    url(r'^', include('wg.accounts.urls', namespace='accounts')),



    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework'))

]
