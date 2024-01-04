from django.urls import path
from .views import trigger_playbook

urlpatterns = [
    path('playbook-trigger/', trigger_playbook, name='trigger_playbook'),
]
