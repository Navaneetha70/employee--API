from django.db import models
import uuid
from django.db import models

class EmployeeSentimentScore(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee_id = models.UUIDField()  # Assuming employee ID is a UUID
    total_mentions = models.IntegerField()
    employee_id = models.CharField(max_length=100)
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
    remark = models.TextField(null=True, blank=True)
    text = models.TextField() 
    text = models.TextField(default='No data')


    def __str__(self):
        return f"Sentiment analysis for employee {self.employee_id} on {self.analysis_date}"

