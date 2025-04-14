from rest_framework.test import APITestCase
from rest_framework import status

class SentimentAnalysisViewTest(APITestCase):
    def test_sentiment_analysis(self):
        # Replace with your actual token
        token = '392ae2e2158dcb213dff94752a9ee536c7b1f788'
        url = 'http://127.0.0.1:8000/api/v1/sentiment/analysis/'
        headers = {
            'Authorization': f'Bearer {token}'
        }
        
        # Send the GET request with query parameters
        response = self.client.get(url, {'department': 'hr_department', 'period': '30d'}, **headers)
        
        # Check if the response is successful (status code 200)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # You can add more assertions based on your expected response
