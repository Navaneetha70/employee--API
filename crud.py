
from sqlalchemy.orm import Session
from models import EmployeeSentimentScore
from datetime import datetime
import uuid

def get_sentiments(db: Session):
    return db.query(EmployeeSentimentScore).all()

def insert_dummy_data(db: Session):
    sentiment = EmployeeSentimentScore(
        employeeId=str(uuid.uuid4()),
        totalMentions=100,
        emailCountAnalyzed=50,
        positiveMentions=40,
        neutralMentions=30,
        negativeMentions=30,
        managementComplaints=5,
        payComplaints=10,
        harassmentConcerns=2,
        positiveScore=40.0,
        negativeScore=-30.0,
        overallSentimentScore=10.0,
        trendScore=2.0,
        analysisDate=datetime.utcnow(),
        remark="Initial dummy entry"
    )
    db.add(sentiment)
    db.commit()
