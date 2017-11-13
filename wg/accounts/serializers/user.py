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
        fields = ('url', 'id', 'is_active', 'date_joined', 'email',
                  'first_name', 'last_name', 'profile')


class UserCreateSerializer(serializers.ModelSerializer):
    url = user_detail
    password = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('url', 'email', 'first_name', 'last_name', 'password')


class UserEditSerializer(serializers.ModelSerializer):
    url = user_detail
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('url', 'id', 'first_name', 'last_name',
                  'profile')

    def update(self, instance, validated_data):
        profile_data = validated_data.get('profile', {})

        instance.first_name = validated_data.get('first_name',
                                                 instance.first_name)
        instance.last_name = validated_data.get('last_name',
                                                instance.last_name)

        instance.save()

        profile = instance.profile
        profile.country = profile_data.get('country', profile.country)
        profile.city = profile_data.get('city', profile.city)
        profile.gender = profile_data.get('gender', profile.gender)
        profile.birthday = profile_data.get('birthday', profile.birthday)
        profile.save()
        return instance


class UserLoginSerializer(UserSerializer):
    token = serializers.SerializerMethodField()

    @staticmethod
    def get_token(user):
        """
        Get or create token
        """

        token, created = Token.objects.get_or_create(user=user)
        return token.key

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'profile', 'token')
