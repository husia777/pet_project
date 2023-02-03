from django.urls import path, include

from core.views import UserCreateAPIView

urlpatterns = [
    path('auth/sign-up/', UserCreateAPIView.as_view())
]

