from django.contrib.auth import login, authenticate
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .models import User
from .serializers import SignUpSerializer, LoginSerializer


class SignUpAPIView(CreateAPIView):
    """Create new user"""
    queryset = User.objects.all()
    serializer_class = SignUpSerializer


class LoginAPIView(CreateAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        # login
        if user:
            login(request, user)
            return Response(status=status.HTTP_200_OK)

        return Response(data={'password': ['Invalid password']}, status=status.HTTP_400_BAD_REQUEST)
