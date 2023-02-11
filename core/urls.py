from django.urls import path, include

from core.views import SignUpAPIView, LoginAPIView, UserRetrieveUpdateView, PasswordUpdateView

urlpatterns = [
    path('signup', SignUpAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('profile', UserRetrieveUpdateView.as_view()),
    path('update_password', PasswordUpdateView.as_view()),

]
