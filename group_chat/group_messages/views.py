from django.shortcuts import render
from .models import Message
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from .serializers import MessageSerializer,MessageLikeSerializer
from rest_framework.generics import GenericAPIView
from group.models import Group
from django.contrib.auth import get_user_model
User = get_user_model()


class MessageListCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user=request.user
        group_id=request.GET.get("group_id", None)
        if group_id is None or group_id == "":
            raise ValidationError("Please provide group Id")
        try:
            g=Group.objects.get(id=group_id)
        except Exception as ex:
            raise Exception("Group with the id {} does not exits".format(group_id))
        request.data['messaged_by'] = str(user.id)
        request.data['group'] = str(group_id)

        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():

            s=serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

class MessageLikeAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        return Message.objects.get(pk=pk)

    def patch(self, request, *args, **kwargs):
        user=request.user
        request.data['liked_by'] = str(user.id)
        message = self.get_object(self.kwargs['pk'])

        serializer = MessageLikeSerializer(message,data=request.data,partial=True)
        if serializer.is_valid():

            s=serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    