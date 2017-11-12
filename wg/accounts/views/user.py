from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from wg.accounts.models import User
from wg.accounts.serializers import (UserSerializer,
                                     UserCreateSerializer,
                                     UserEditSerializer)



class UserList(ListCreateAPIView):
    queryset = User.objects.order_by('-date_joined')
    # serializer_class = UserSerializer
    permission_classes = ()
    authentication_classes = ()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserCreateSerializer
        return UserSerializer

    def put(self, request, *args, **kwargs):
        users = User.objects.get_order_from_data(**request.data)
        return Response(UserSerializer(users).data)


    def post(self, request, *args, **kwargs):
        self.serializer_class = UserCreateSerializer
        return super(UserList, self).post(request, *args, **kwargs)

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()


class UserDetail(APIView):
    permission_classes = ()

    @staticmethod
    def get(request, pk):
        user = get_object_or_404(User, pk=pk)
        context = {'request': request}
        return Response(UserSerializer(user, context=context).data)

    @staticmethod
    def post(request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserEditSerializer(user, data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        pass