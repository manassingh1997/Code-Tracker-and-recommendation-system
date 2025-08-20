from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from logs.models import CodingLog
from goals.models import Goal
from datetime import date 
from django.db.models.functions import TruncDate
from django.db.models import Count 

# Create your views here.
class HeatmapView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        #Group logs by date and count them
        logs = (
            CodingLog.objects
            .filter(user=user)
            .annotate(log_day=TruncDate('date'))
            .values('log_day')
            .annotate(count=Count('id'))
            .order_by('log_day')
        )

        return Response(logs)
    
class TopicDistributionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        logs = (
            CodingLog.objects
            .filter(user=user)
            .values('topic')
            .values('topic')
            .annotate(count=Count('id'))
            .order_by('-count')
        )

        return Response(logs)
    
class DailyGoalProgressView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        user = request.user
        today = date.today()

        # Get today's logs
        today_logs_count = CodingLog.objects.filter(user=user, date=today).count()

        # Get user goal
        try:
            goal = Goal.objects.get(user=user)
            daily_target = goal.daily_target
        except Goal.DoesNotExist:
            return Response({"detail": "Goal not set."}, status=400)
        

        #Prepare response
        progress = {
            "date": today,
            "problems_solved": today_logs_count,
            "daily_target": daily_target,
            "completed_percentage": round((today_logs_count / daily_target) * 100, 2) if daily_target else 0.0
        }

        return Response(progress)
