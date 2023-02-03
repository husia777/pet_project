from django.urls import path, include

from core.views import UserCreateAPIView

urlpatterns = [
    path('core/signup/', UserCreateAPIView.as_view())
]

