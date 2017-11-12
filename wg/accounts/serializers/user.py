from rest_framework import serializers
from wg.accounts.models import User
from rest_framework.authtoken.models import Token
from wg.accounts.serializers import ProfileSerializer

user_detail = serializers.HyperlinkedIdentityField(
    view_name='accounts:user-detail',
    lookup_field='pk'
)


class UserSerializer(serializers.ModelSerializer):
    url = user_detail
    profile = ProfileSerializer(exclude=['user'])
    class Meta:
        model = User
        fields = ('url', 'id', 'date_joined', 'email', 'first_name',
                  'last_name', 'profile')


class UserCreateSerializer(serializers.ModelSerializer):
    url = user_detail
    password = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('url', 'email', 'first_name', 'last_name', 'password')


class UserEditSerializer(serializers.ModelSerializer):
    url = user_detail

    class Meta:
        model = User
        fields = ('url', 'id', 'email', 'first_name', 'last_name', 'profile', 'token')


class UserLoginSerializer(UserSerializer):
    token = serializers.SerializerMethodField()

    @staticmethod
    def get_token(user):
        """
        Get or create token
        """

        token, created = Token.objects.get_or_create()
        return token.key

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'profile', 'token')
