from django.urls import path

from core.views import SignUpAPIView, LoginAPIView

urlpatterns = [
    path('signup', SignUpAPIView.as_view()),
    path('login', LoginAPIView.as_view()),

]
