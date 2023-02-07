from rest_framework.generics import CreateAPIView
from .models import User
from .serializers import SignUpSerializer


class SignUpView(CreateAPIView):
    """Create new user"""
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
