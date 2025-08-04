from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CodinglogViewSet

router = DefaultRouter()
router.register(r'',CodinglogViewSet, basename='codinglog')

urlpatterns = [
    path('', include(router.urls)),
]