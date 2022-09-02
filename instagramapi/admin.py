from django.contrib import admin
from .models import InstaPost,ImageModel,Comment,LikePost

# Register your models here.

admin.site.register((InstaPost,ImageModel,Comment,LikePost))