from django.shortcuts import render
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from rest_framework import generics, permissions
from .serializers import GroupSerializer,GroupAddMemberSerializer
from rest_framework.generics import GenericAPIView
from .models import Group
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.

class GroupCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user=request.user
        request.data['created_by'] = str(user.id)
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            s=serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)

class GroupAddMembersAPIView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'user_id'

    def get_object(self, pk):
        return Group.objects.get(pk=pk)

    def patch(self, request, *args, **kwargs):
        user=request.user
        request.data['created_by'] = str(user.id)
        group_object = self.get_object(self.kwargs['pk'])
        serializer = GroupAddMemberSerializer(group_object,data=request.data)
        if serializer.is_valid():
            s=serializer.save()
            data={
                "group_members": s.members.all().values_list('username',flat=True)
            }
            return Response(data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request, *args, **kwargs):
        user=request.user
        request.data['created_by'] = str(user.id)
        group_object = self.get_object(self.kwargs['pk'])
        data={
                "group_members": group_object.members.all().values_list('username',flat=True)
            }
        return Response(data, status=status.HTTP_200_OK)

class GroupSearchMembersAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user=request.user
        print(self.kwargs['pk'])
        print(request.data)
        users=Group.objects.filter(id=self.kwargs['pk'],members__username__icontains=request.data.get("name")).values_list('members__username',flat=True)
        data={
                "members": users
            }
        return Response(data, status=status.HTTP_200_OK)
        





    
     
