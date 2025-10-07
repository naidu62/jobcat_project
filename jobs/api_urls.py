# jobs/api_urls.py
from rest_framework.routers import DefaultRouter
from .api_views import JobNotificationViewSet

router = DefaultRouter()
router.register(r'jobs', JobNotificationViewSet, basename='jobs')

urlpatterns = router.urls
