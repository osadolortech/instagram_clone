from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import ProfieView

router = DefaultRouter()
router.register('profile', ProfieView)

urlpatterns = [
    path("",include(router.urls))
]