from django.urls import path

from core.views import UserCreateAPIView

urlpatterns = [
    path('core/signup/', UserCreateAPIView.as_view()),
]

