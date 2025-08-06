from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from logs.models import CodingLog
from .models import DSAProblemBank
from .serializers import DSAProblemSerializer
from collections import Counter
# Create your views here.

class RecommendationView(APIView):
    permission_clasees = [IsAuthenticated]

    def get(self, request):
        user = request.user

        logs = CodingLog.objects.filter(user=user)

        # Count topic frequency
        topic_counts = Counter(log.topic for log in logs)
        weak_topics = [topic for topic, count in topic_counts.items() if count <= 2]

        # Get links of attempted problems
        attempted_links = logs.values_list('problem_link', flat=True)

        # Recommendations from bank: unseen & weak topic
        recommendations = DSAProblemBank.objects.exclude(link__in=attempted_links)

        if weak_topics:
            recommendations = recommendations.filter(topic__in=weak_topics)

        serialized = DSAProblemSerializer(recommendations[:5], many = True)
        return Response(serialized.data)