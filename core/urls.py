from django.urls import path, include

from core.views import UserCreateAPIView

urlpatterns = [
    path('signup/', UserCreateAPIView.as_view())
]

