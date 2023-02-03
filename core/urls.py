from django.urls import path

from core.views import UserCreateAPIView, index

urlpatterns = [
    path('index/', index),
    path('signup/', UserCreateAPIView.as_view()),
]

