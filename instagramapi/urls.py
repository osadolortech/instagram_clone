from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ImageView,LikeView,CommentView,InstaPostViews

router = DefaultRouter()
router.register("instapost", InstaPostViews)
router.register("image", ImageView)
router.register("Like", LikeView)
router.register("comment", CommentView)

urlpatterns = [
    path("",include(router.urls))
]