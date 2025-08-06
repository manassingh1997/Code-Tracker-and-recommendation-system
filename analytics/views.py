from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from logs.models import CodingLog
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
    permisison_classes = [IsAuthenticated]

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
