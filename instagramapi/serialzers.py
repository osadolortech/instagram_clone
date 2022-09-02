from rest_framework import serializers
from .models import InstaPost,Comment,ImageModel,LikePost


class ImageSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    class Meta:
        model = ImageModel
        fields = "__all__"



class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    class Meta:
        model = Comment
        fields = "__all__"


class LikePostSerilaizer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    class Meta:
        model = LikePost
        fields="__all__"


class InstapostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    post_image = ImageSerializer(many=True,read_only=True)
    like_post= LikePostSerilaizer(many=True, read_only=True)
    post_comment = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = InstaPost
        fields = [
            "id","user","post_image","caption","created_at","like_post","post_comment","num_of_like","num_of_comment"
        ]