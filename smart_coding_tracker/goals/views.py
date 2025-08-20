from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Goal
from .serializers import GoalSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  
from datetime import date
from logs.models import CodingLog
# Create your views here.

class GoalViewSet(viewsets.ModelViewSet):
    serializer_class = GoalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class GoalStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        today = date.today()

        try:
            goal = Goal.objects.filter(user=user).latest('created_on')
        except Goal.DoesNotExist:
            return Response({"detail": "Goal not set."}, status=400)
        
        if goal.period == 'daily':
            count = CodingLog.objects.filter(user=user, date=today).count()
        elif goal.period == 'weekly':
            from datetime import timedelta
            start_of_week = today - timedelta(days=today.weekday())
            count = CodingLog.objects.filter(user=user, date__gte=start_of_week, date__lte=today).count()
        else:
            count = 0

        goal_completed = count >= goal.target_count
        return Response({
            "goal_completed": goal_completed,
            "count": count,
            "target": goal.target_count
        })
