from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from core.models import User
from core.serializers import UserRegisterSerializer

def index(request):
    return HttpResponse('<h1>dspogdf</h1>')
class UserCreateAPIView(CreateAPIView):
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()
