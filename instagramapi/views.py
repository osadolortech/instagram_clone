from rest_framework import viewsets
from .userpermission import CustomPermission
from django.db.models import Q
from .models import ImageModel,Comment,LikePost,InstaPost
from .serialzers import InstapostSerializer,ImageSerializer,LikePostSerilaizer,CommentSerializer
from rest_framework.parsers import MultiPartParser, FormParser
# Create your views here.


class InstaPostViews(viewsets.ModelViewSet):
    permission_classes = [CustomPermission]
    queryset= InstaPost.objects.all()
    serializer_class = InstapostSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

class ImageView(viewsets.ModelViewSet):
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializer
    parser_classes = [MultiPartParser,FormParser]


class CommentView(viewsets.ModelViewSet):
    queryset =Comment.objects.all()
    serializer_class = CommentSerializer

class LikeView(viewsets.ModelViewSet):
    queryset =LikePost.objects.all()
    serializer_class = LikePostSerilaizer

    def perform_create(self, serializer):
        queryset = self.filter_queryset(self.get_queryset())
        subset = queryset.filter(Q(user_id=self.request.data['user']) & Q(post_id=self.request.data['post']))
        if subset.count() > 0:
            subset.first().delete()
            return
        serializer.save()