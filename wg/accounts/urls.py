from django.conf.urls import url
from wg.accounts import views
urlpatterns = [
    url(r'^login/$', views.LoginView.as_view(), name='login'),



    url(r'^accounts/$',
        views.UserList.as_view(),
        name='user-list'),
    url(r'^accounts/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name='user-detail')
]