from django.shortcuts import render
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
        data={
            "data": "data successful"
        }
        group_object = self.get_object(self.kwargs['pk'])
        members=request.data.get('members',[])
        if len(members)>0:
            for member_id in members:
                print(member_id)
                user1=User.objects.get(id=member_id)
                group_object.members.add(user1)
                group_object.save()
        return Response(data, status=status.HTTP_201_CREATED)
        
    def get(self, request, *args, **kwargs):
        user=request.user
        request.data['created_by'] = str(user.id)
        data={
            "data": "data successful"
        }
        group_object = self.get_object(self.kwargs['pk'])
        serializer = GroupAddMemberSerializer(group_object,data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

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
        





    
     
