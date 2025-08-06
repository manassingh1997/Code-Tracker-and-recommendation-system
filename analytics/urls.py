from django.urls import path
from .views import HeatmapView, TopicDistributionView, DailyGoalProgressView

urlpatterns = [
    path('heatmap/', HeatmapView.as_view(), name='heatmap'),
    path('topics/', TopicDistributionView.as_view(), name='topic-distribution'),
    path('daily-progress/', DailyGoalProgressView.as_view(), name='daily-goal-progress'),
]