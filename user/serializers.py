
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.db import transaction
from .models import Profile
from .models import User
from instagramapi.serialzers import InstaPost


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class CustomUser(ModelSerializer):
    user_profile = ProfileSerializer(read_only=True)
    post = InstaPost()
    class Meta:
        model = User
        fields = [
            "id","name","username","user_profile","post"
        ]
        read_only_fileds = ("id","name","post")
        
    # def create(self, validated_data):
    #     users_data = validated_data.pop('user_profile')
    #     users = User.objects.create(**validated_data)
    #     for user_data in users_data:
    #         Profile.objects.create(users=users, **user_data)
    #     return users

    # def update(self, instance, validated_data):
    #     users_data = validated_data.pop('user_profile')
    #     item = instance.user_profile
    #     for user_data in users_data:
    #         setattr(item,user_data)
    #     item.save()
    #     return instance


class CustomRegisterSerializer(RegisterSerializer):
    name = serializers.CharField(max_length=125)

    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.name = self.data.get('name')
        user.save()
        return user

