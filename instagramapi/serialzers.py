from rest_framework import serializers
from .models import InstaPost,Comment,ImageModel,LikePost


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        models = ImageModel
        fields = "__all__"

class InstapostSrilaizers(serializers.ModelSerializer):
    post_image = ImageSerializer(many=True,read_only=True)
    class Meta:
        models = InstaPost
        fields = [
            "id","post_image","caption","created_at"
        ]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        models = Comment
        fields = "__all__"


class LikePostSerilaizer(serializers.ModelSerializer):
    class Meta:
        models = LikePost
        fields="__all__"