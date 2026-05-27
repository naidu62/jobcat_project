from rest_framework import viewsets
from .models import JobNotification
from .serializers import JobNotificationSerializer


class JobNotificationViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = (
        JobNotification.objects
        .prefetch_related(
            "vacancy_details",
            "extra_fields"
        )
        .order_by("-created_at")
    )

    serializer_class = JobNotificationSerializer