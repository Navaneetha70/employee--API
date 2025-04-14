from rest_framework.views import APIView
from rest_framework.response import Response
from .models import EmployeeSentimentScore
from .serializers import EmployeeSentimentScoreSerializer
from rest_framework import status
from datetime import datetime, timedelta
from rest_framework.permissions import IsAuthenticated
from textblob import TextBlob  # ← Import TextBlob
from collections import defaultdict

class SentimentAnalysisView(APIView):
    permission_classes = [IsAuthenticated]  # or [AllowAny] if you prefer

    def get(self, request):
        # Get query parameters
        department_id = request.query_params.get('department')
        start_time = request.query_params.get('startTime')
        end_time = request.query_params.get('endTime')
        period = request.query_params.get('period', '30d')  # Default to 30 days

        # Parse date filters
        if start_time:
            start_time = datetime.strptime(start_time, '%Y-%m-%d')
        if end_time:
            end_time = datetime.strptime(end_time, '%Y-%m-%d')

        # Get relevant records
        sentiment_data = EmployeeSentimentScore.objects.filter(employee_id__startswith=department_id)
        if start_time:
            sentiment_data = sentiment_data.filter(analysis_date__gte=start_time)
        if end_time:
            sentiment_data = sentiment_data.filter(analysis_date__lte=end_time)

        # Limit data based on period
        if period == '30d':
            sentiment_data = sentiment_data.filter(analysis_date__gte=datetime.now() - timedelta(days=30))
            period_type = 'daily'
        elif period == '60d':
            sentiment_data = sentiment_data.filter(analysis_date__gte=datetime.now() - timedelta(days=60))
            period_type = 'weekly'
        elif period == '90d':
            sentiment_data = sentiment_data.filter(analysis_date__gte=datetime.now() - timedelta(days=90))
            period_type = 'monthly'

        # Aggregate sentiment using TextBlob
        aggregated_by_date = defaultdict(lambda: {'positive': 0, 'neutral': 0, 'negative': 0, 'total': 0})
        
        for record in sentiment_data:
            date_key = record.analysis_date.strftime('%d-%m-%Y')
            text = record.text  # Make sure your model has this field
            
            blob = TextBlob(text)
            polarity = blob.sentiment.polarity

            if polarity > 0:
                aggregated_by_date[date_key]['positive'] += 1
            elif polarity < 0:
                aggregated_by_date[date_key]['negative'] += 1
            else:
                aggregated_by_date[date_key]['neutral'] += 1
            
            aggregated_by_date[date_key]['total'] += 1

        # Format aggregated data
        aggregated_data = []
        for date, counts in aggregated_by_date.items():
            total = counts['total']
            aggregated_data.append({
                'label': date,
                'positivePercentage': (counts['positive'] / total) * 100 if total else 0,
                'neutralPercentage': (counts['neutral'] / total) * 100 if total else 0,
                'negativePercentage': (counts['negative'] / total) * 100 if total else 0,
            })

        # Compute overall average
        def avg_percent(key):
            return sum(d[key] for d in aggregated_data) / len(aggregated_data) if aggregated_data else 0

        response_data = {
            'status': 'success',
            'data': {
                'currentPeriod': {
                    'year': datetime.now().year,
                    'month': datetime.now().month,
                    'yearLabel': datetime.now().strftime('%B %Y'),
                    'positivePercentage': avg_percent('positivePercentage'),
                    'neutralPercentage': avg_percent('neutralPercentage'),
                    'negativePercentage': avg_percent('negativePercentage'),
                },
                'periodType': period_type,
                'periodLabel': f'Last {period}',
                'aggregatedData': aggregated_data
            }
        }

        return Response(response_data, status=status.HTTP_200_OK)
