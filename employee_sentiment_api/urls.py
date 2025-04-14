
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from .views import SentimentAnalysisView

urlpatterns = [
    path('admin/', admin.site.urls),  # Only this line for admin
    path('api/sentiment/', SentimentAnalysisView.as_view(), name='sentiment-analysis')
]





