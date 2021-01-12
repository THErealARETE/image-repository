from django.urls import path, include

from .views import ImageViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('image' , ImageViewSet)

urlpatterns = router.urls


