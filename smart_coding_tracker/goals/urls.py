from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GoalViewSet, GoalStatusView

router = DefaultRouter()
router.register(r'', GoalViewSet, basename='goal')

urlpatterns = [
    path('status/', GoalStatusView.as_view(), name='goal-status'),    
    path('', include(router.urls)),
]