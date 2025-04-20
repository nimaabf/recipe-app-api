# Seriaizers for user api app.

from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from django.utils.translation import gettext as _


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 5}
        }

    def create(self, validated_data):
        """Create and return a user with encrypted password."""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instace, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instace, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user

    class AuthTokenSerializer(serializers.Serializer):
        email = serializers.EmailField()
        password = serializers.CharField(
            style={'input-type': 'password'},
            trim_whitespace=False
        )

        def validate(self, attrs):
            email = attrs.get('email')
            password = attrs.get('password')
            user = authenticate(
                request=self.context.get('request'),
                username=email,
                password=password
            )
            if not user:
                msg = _('Unable to auth with this user and password')
                raise serializers.ValidationError(msg, code='authorization')

            attrs['user'] = user
            return attrs
