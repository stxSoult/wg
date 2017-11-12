from rest_framework import serializers

from wg.accounts.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'picture', 'country')

    def __init__(self, exclude=None, **kwargs):
        super().__init__(**kwargs)

        if exclude:
            assert isinstance(exclude, (list, tuple)), 'list or tuple'

            fields = tuple((field for field in self.Meta.fields if
                      not field in exclude))
            self.Meta.fields = fields

        else:
            self.user = serializers.HyperlinkedIdentityField(
                view_name='accounts:user-detail',
                lookup_field='pk',
            )
