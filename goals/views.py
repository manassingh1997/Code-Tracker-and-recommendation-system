from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Goal
from .serializers import GoalSerializer
# Create your views here.

class GoalViewSet(viewsets.ModelViewSet):
    serializer_class = GoalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
