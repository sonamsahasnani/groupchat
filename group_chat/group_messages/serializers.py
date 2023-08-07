from .models import Message
from group.models import Group
from rest_framework import serializers
from django.contrib.auth import get_user_model
from user.serializers import UserSerializer
User = get_user_model()

# from django.db import models

class MessageSerializer(serializers.ModelSerializer):
    # created_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    description = serializers.CharField()
    messaged_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    group = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all())


    class Meta:
        model = Message
        fields = ('__all__')

    def create(self,validated_data):
        print(validated_data)
        instance=Message.objects.create(**validated_data)
        return instance

class MessageLikeSerializer(serializers.ModelSerializer):
    liked_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())


    class Meta:
        model = Message
        fields = ('__all__')

    def update(self,instance,validated_data):
        instance.is_liked = True
        instance.liked_by=validated_data.get('liked_by')
        return instance


    