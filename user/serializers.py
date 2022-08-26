
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.db import transaction
from .models import Profile
from .models import User


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class CustomeUser(ModelSerializer):
    user_profile = ProfileSerializer()
    class Meta:
        model = User
        fields = [
            "id","name","username"
        ]
        read_only_fileds = ("id","name")


class CustomRegisterSerializer(RegisterSerializer):
    name = serializers.CharField(max_length=125)

    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.name = self.data.get('name')
        user.save()
        return user

