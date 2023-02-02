from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from core.models import User
from core.serializers import UserRegisterSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()
