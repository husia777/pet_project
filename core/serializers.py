from rest_framework import serializers

from core.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password_repeat']

    def is_valid(self, *, raise_exception=False):
        if self.initial_data.pop('password') == self.initial_data.pop('password_repeat'):
            return super().is_valid(raise_exception=True)
        raise serializers.ValidationError("Пароли не совпадают")

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data["last_name"],
            email=validated_data['email'],
            password=validated_data['password']
        )
        user.save()
        return user
