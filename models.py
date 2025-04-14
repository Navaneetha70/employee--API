from django.db import models
import uuid

class EmployeeSentimentScore(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employeeId = models.UUIDField()
    totalMentions = models.IntegerField(default=0)
    emailCountAnalyzed = models.IntegerField(default=0)
    positiveMentions = models.IntegerField(default=0)
    neutralMentions = models.IntegerField(default=0)
    negativeMentions = models.IntegerField(default=0)
    managementComplaints = models.IntegerField(default=0)
    payComplaints = models.IntegerField(default=0)
    harassmentConcerns = models.IntegerField(default=0)
    positiveScore = models.FloatField(default=0.0)
    negativeScore = models.FloatField(default=0.0)
    overallSentimentScore = models.FloatField(default=0.0)
    trendScore = models.FloatField(default=0.0)
    analysisDate = models.DateTimeField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    remark = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.id)
