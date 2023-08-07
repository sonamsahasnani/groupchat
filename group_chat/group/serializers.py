from .models import Group
from rest_framework import serializers
from django.contrib.auth import get_user_model
from user.serializers import UserSerializer
User = get_user_model()

# from django.db import models

class UserAddSerializer(serializers.ModelSerializer):
    ingredients = serializers.ListField(write_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', )

class GroupSerializer(serializers.ModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Group
        fields = ('name','created_by')
    

class GroupAddMemberSerializer(serializers.ModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    members = serializers.ListField(write_only=True)

    class Meta:
        model = Group
        fields = ('created_by','name','members')

    def get(self, instance, validated_data):
        print("instance")
        print(instance)
        return instance

    def update(self, instance, validated_data):
        member_ids = validated_data.get('members')
        for member_id in member_ids:
            user=User.objects.get(id=member_id)
            instance.members.add(user)
            instance.save()
        return instance