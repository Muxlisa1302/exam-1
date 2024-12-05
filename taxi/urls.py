from django.urls import path
from . import views

urlpatterns = [
    path('', views.taxi_rides, name='taxi_rides'),
]
