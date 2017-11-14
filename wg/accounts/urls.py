from django.conf.urls import url
from wg.accounts import views

urlpatterns = [
    url(r'^$', views.UserDetail.as_view(), name='user-detail'),

    url(r'^login/$',
        views.LoginView.as_view(),
        name='login'),
    url(r'^reset_password/$',
        views.PasswordReset.as_view(),
        name='password_reset'),


    url(r'^accounts/$',
        views.UserList.as_view(),
        name='user-list'),
]