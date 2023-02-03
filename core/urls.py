from django.urls import path, include

from core.views import UserCreateAPIView

urlpatterns = [
    path('core/sign-up/', UserCreateAPIView.as_view())
]

