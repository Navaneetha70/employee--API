from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

# Define the SentimentRecord model (Pydantic schema)
class SentimentRecord(BaseModel):
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
    analysisDate: str

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Employee Sentiment API"}

# Create endpoint for getting employee sentiment scores
@app.get("/employee-sentiment")
def get_employee_sentiment():
    # Here you could fetch data from your database
    return {"message": "Employee Sentiment Scores Data"}

# Create endpoint for adding new sentiment records
@app.post("/employee-sentiment")
def create_sentiment_record(record: SentimentRecord):
    # Here you would typically save the record to the database
    return {"message": "Sentiment record created", "data": record}
