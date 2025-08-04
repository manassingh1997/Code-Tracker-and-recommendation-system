from rest_framework import serializers
from .models import CodingLog
# Create your serializers here.
class CodingLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodingLog
        fields = '__all__'
        read_only_fields = ['user']

    