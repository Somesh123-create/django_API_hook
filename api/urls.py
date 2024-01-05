from django.urls import path
from .views import TriggerPlaybookAPIView

urlpatterns = [
    path('playbook-trigger/', TriggerPlaybookAPIView.as_view(), name='trigger_playbook'),
]
