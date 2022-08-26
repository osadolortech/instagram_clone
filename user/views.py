from rest_framework.parsers import MultiPartParser, FormParser
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework import viewsets

# Create your views here.

class ProfieView(viewsets.ModelViewSet):
    queryset = Profile.objects.select_related("user")
    serializer_class = ProfileSerializer
    parser_classes = [MultiPartParser,FormParser]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)