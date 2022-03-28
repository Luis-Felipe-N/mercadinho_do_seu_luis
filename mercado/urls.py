from django.urls import path
from .views import HomeView


urlpatterns = [
    path('', HomeView.HomeView.as_view(), name='home')
]
