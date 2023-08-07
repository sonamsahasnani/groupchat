from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.conf import settings  
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token 
from django.contrib.auth.hashers import check_password
from django.contrib.auth.views import LogoutView
from django.contrib.auth import get_user_model
User = get_user_model()


class UserListCreateAPIView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request, format=None):
        email = request.data.get("email")
        password = request.data.get("password")
        username=request.data.get("username")
        data={
            "email": email,
            "username":username
        }
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            s=serializer.save()
            token=Token.objects.create(user=s)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        username=request.data.get("username")
        password = request.data.get("password")
        data={
            "username":username
        }
        try:
            user=User.objects.get(username=username)
            if user.check_password(password):
                t=Token.objects.get_or_create(user=user)
            else:
                data={
                    "data":"Invalid Username or Password provided"
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            raise ValidationError("User does not Exists")
        return Response(data={"meessage":"Successful logged In"}, status=status.HTTP_200_OK)

class UserLogoutAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




