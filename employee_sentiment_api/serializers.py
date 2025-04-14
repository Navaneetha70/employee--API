from rest_framework import serializers
from .models import EmployeeSentimentScore

class EmployeeSentimentScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeSentimentScore
        fields = '__all__'
