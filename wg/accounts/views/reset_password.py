from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from wg.accounts.serializers import PasswordResetSerializer


class PasswordReset(GenericAPIView):
    serializer_class = PasswordResetSerializer

    def get(self, request, *args, **kwargs):
        return Response(PasswordResetSerializer().data)

    def post(self, request, *args, **kwargs):
        pass
