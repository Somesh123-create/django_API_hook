from django.urls import path
from .views import home

app_name = "hooks"


urlpatterns = [
    path('', home, name='home'),
]
