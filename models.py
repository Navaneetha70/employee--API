# models.py

import uuid
from django.db import models

class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Additional fields for the Employee model can be added here

class EmployeeSentimentScore(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    total_mentions = models.IntegerField()
    email_count_analyzed = models.IntegerField()
    positive_mentions = models.IntegerField()
    neutral_mentions = models.IntegerField()
    negative_mentions = models.IntegerField()
    management_complaints = models.IntegerField()
    pay_complaints = models.IntegerField()
    harassment_concerns = models.IntegerField()
    positive_score = models.FloatField()
    negative_score = models.FloatField()
    overall_sentiment_score = models.FloatField()
    trend_score = models.FloatField()
    analysis_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    remark = models.TextField()
