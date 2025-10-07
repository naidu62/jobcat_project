# jobs/api_views.py
from rest_framework import viewsets
from .models import JobNotification
from .serializers import JobNotificationSerializer


class JobNotificationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Read-only API for job notifications.
      • GET /api/jobs/       → list
      • GET /api/jobs/<id>/  → detail
    """
    queryset = JobNotification.objects.all().order_by('-start_date', '-created_at')
    serializer_class = JobNotificationSerializer