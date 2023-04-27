from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Task
from .serializer import TaskSerializer, UserSerializer
from rest_framework import status

class CreateUser(APIView):
    def post(self, request:Request):
        username = request.data.get('username')
        if User.objects.filter(username = username):
            return Response({"user":"user already exist"})
        else:
            password = request.data.get('password')
            user = User.objects.create(username=username, password=password)
            token = Token.objects.create(user = user)
            return Response({"token":token.key})
        
class Login_user(APIView):
    def post(self, request:Request):
        username = request.data.get("username")
        password = request.data.get("password")
        if User.objects.filter(username = username):
            user = User.objects.get(username = username)
            token, uniq = Token.objects.get_or_create(user = user)
            return Response({"token":token.key})
        else:
            return Response({"user":"user not found"})

