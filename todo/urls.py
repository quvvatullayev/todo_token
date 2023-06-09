from django.urls import path
from .views import (
    CreateUser,
    Login_user,
    Create_todo,
    Updeate_todo,
    Delete_todo,
    Get_todo_by_user,
    Get_todo_by_id,
    Get_todo_status_check,
    Updeate_todo_status,
    Get_todo_status_uncheck,
)

urlpatterns = [
    path("create_user/", CreateUser.as_view()),
    path('login/', Login_user.as_view()),
    path('create_todo/', Create_todo.as_view()),
    path('update_todo/<int:pk>/', Updeate_todo.as_view()),
    path('delete_todo/<int:pk>/', Delete_todo.as_view()),
    path('get_todo_by_user/', Get_todo_by_user.as_view()),
    path('get_todo_by_id/<int:pk>/', Get_todo_by_id.as_view()),
    path('get_todo_status_check/', Get_todo_status_check.as_view()),
    path('update_todo_status/<int:pk>/', Updeate_todo_status.as_view()),
    path('get_todo_status_uncheck/', Get_todo_status_uncheck.as_view()),
    
]