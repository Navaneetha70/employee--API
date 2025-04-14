
from pydantic import BaseModel
from datetime import datetime

class EmployeeSentimentScoreSchema(BaseModel):
    id: str
    employeeId: str
    totalMentions: int
    emailCountAnalyzed: int
    positiveMentions: int
    neutralMentions: int
    negativeMentions: int
    managementComplaints: int
    payComplaints: int
    harassmentConcerns: int
    positiveScore: float
    negativeScore: float
    overallSentimentScore: float
    trendScore: float
    analysisDate: datetime
    createdAt: datetime
    updatedAt: datetime
    remark: str

    class Config:
        orm_mode = True
