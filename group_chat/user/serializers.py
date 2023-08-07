from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

# User Serializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
      user = User.objects.create_user(username=validated_data['username'], email=validated_data['email'], password=validated_data['password'])
      user.save()
      return user

# Register Serializer
# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'password')
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#       user = User.objects.create(username=validated_data['username'], email=validated_data['email'])  
#       user.set_password(validated_data['password'])
#       user.save()
#       return user