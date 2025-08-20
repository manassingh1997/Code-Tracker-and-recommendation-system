from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import CodingLog
from .serializers import CodingLogSerializer
# Create your views here.

class CodinglogViewSet(viewsets.ModelViewSet):
    serializer_class = CodingLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CodingLog.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

