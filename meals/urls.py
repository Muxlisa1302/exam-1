from django.urls import path
from . import views

urlpatterns = [
    path('', views.meal_list, name='meal_list'),
]
