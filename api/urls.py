# api/urls.py
from django.urls import include, path

urlpatterns = [
    path('', include('jobs.api_urls')),   # now /api/jobs/ is available
]