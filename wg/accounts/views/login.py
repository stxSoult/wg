from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import reverse
from django.contrib.auth import authenticate

from wg.accounts.models import User
from wg.accounts.serializers import UserLoginSerializer


class LoginView(APIView):
    permission_classes = ()

    def get(self, request, *args, **kwargs):
        return redirect(reverse('accounts:user-list'))

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if not user:
            return Response({'ERROR': 'NET TAKOGO'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserLoginSerializer(user)
        return Response(serializer.data)