from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer

from core.models import User


class SignUpSerializer(serializers.ModelSerializer):

    def is_valid(self, raise_exception=False):
        self._password_repeat = self.initial_data.pop('password_repeat')
        return super().is_valid(raise_exception=raise_exception)

    def validate(self, data):
        if data.get('password') != self._password_repeat:
            raise serializers.ValidationError({'password_repeat': ['Пароли не совпадают']})
        return data

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(user.password)
        user.save()
        return user

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']


