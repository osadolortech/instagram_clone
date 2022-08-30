from rest_framework.parsers import MultiPartParser, FormParser
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework import viewsets
from instagramapi.permision import CustomPermission

# Create your views here.

class ProfieView(viewsets.ModelViewSet):
    permission_classes = [CustomPermission]
    queryset = Profile.objects.select_related("user")
    serializer_class = ProfileSerializer
    parser_classes = [MultiPartParser,FormParser]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)