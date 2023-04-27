from django.urls import path
from .views import (
    CreateUser,
    Login_user,
)

urlpatterns = [
    path("create_user/", CreateUser.as_view()),
    path('login/', Login_user.as_view()),
]