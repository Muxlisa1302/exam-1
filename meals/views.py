from django.shortcuts import render
from .models import Meal


def meal_list(request):
    meals = Meal.objects.all()
    return render(request, 'meals/list.html', {'meals': meals})

