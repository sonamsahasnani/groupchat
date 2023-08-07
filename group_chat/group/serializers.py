from .models import Group
from rest_framework import serializers
from django.contrib.auth import get_user_model
from user.serializers import UserSerializer
User = get_user_model()

# from django.db import models

class UserAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', )

    def to_representation(self, instance):
        print("UserAdd to_representation")
        rep = super().to_representation(instance)
        # rep["genre"] = GenreSerializer(instance.genre.all(), many=True).data
        print("rep")
        print(rep)
        return rep


class GroupSerializer(serializers.ModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Group
        fields = ('name','created_by')
    

class GroupAddMemberSerializer(serializers.ModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    members = UserAddSerializer(many=True)

    class Meta:
        model = Group
        fields = ('created_by','name','members')

    def get(self, instance, validated_data):
        print("get")
        print(validated_data)
        return instance

    # def to_representation(self, value):
    #     print("to_representation")
    #     print(value)
    #     return value
    #     # return [{
    #     #     'id': value.id,
    #     #     # 'name': obj.name,
    #     # }]


    def to_internal_value(self, data):
        print("to_internal_value")
        print(data['members'])
        u=User.objects.filter(id__in=data['members'])
        print(u)
        return u


    def update(self, instance, validated_data):
        print("update")
        print("validated_data")
        print(validated_data)
        data = validated_data.get('members')
        print("data")
        print(data)
        # print(pk)
        # poll = get_object_or_404(User, pk=pk)
        # data = UserSerializer(poll).data
        # print(data)
        # print("**update Function**")
        return instance