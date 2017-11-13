from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import SAFE_METHODS
from django.shortcuts import get_object_or_404
# ==
from wg.utils.permissions import IsOwnerOrReadOnly
from wg.accounts.models import User
from wg.accounts.serializers import (UserSerializer,
                                     UserCreateSerializer,
                                     UserEditSerializer)


class UserList(ListCreateAPIView):
    queryset = User.objects.order_by('-date_joined')
    permission_classes = ()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserCreateSerializer
        return UserSerializer

    def post(self, request, *args, **kwargs):
        self.serializer_class = UserCreateSerializer
        return super(UserList, self).post(request, *args, **kwargs)

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()


class UserDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = User.objects.all().order_by('-date_joined')

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return UserSerializer
        return UserEditSerializer

    def delete(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs.get('pk'))
        user.is_active = False
        user.save()
        context = {'request': request}
        return Response(UserSerializer(user, context=context).data,
                        status=status.HTTP_200_OK)
