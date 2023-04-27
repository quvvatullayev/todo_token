from django.urls import path
from .views import (
    CreateUser,
    Login_user,
    Create_todo,
)

urlpatterns = [
    path("create_user/", CreateUser.as_view()),
    path('login/', Login_user.as_view()),
    path('create_todo/', Create_todo.as_view()),
]