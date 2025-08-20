from rest_framework import serializers
from .models import DSAProblemBank

class DSAProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = DSAProblemBank
        fields = ['id', 'title', 'link', 'topic', 'difficulty']