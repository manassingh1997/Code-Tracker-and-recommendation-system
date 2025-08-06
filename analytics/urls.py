from django.urls import path
from .views import HeatmapView, TopicDistributionView

urlpatterns = [
    path('heatmap/', HeatmapView.as_view(), name='heatmap'),
    path('topics/', TopicDistributionView.as_view(), name='topic-distribution'),
]