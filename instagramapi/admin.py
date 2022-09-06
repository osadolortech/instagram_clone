from django.contrib import admin
from .models import InstaPost,ImageModel,Comment,LikePost
from user.models import User

# Register your models here.

admin.site.register((InstaPost,ImageModel,Comment,LikePost,User))