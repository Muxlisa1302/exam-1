from django.shortcuts import render
from .models import TaxiRide


def taxi_rides(request):
    rides = TaxiRide.objects.all()
    return render(request, 'taxi/rides.html', {'taxi_rides': rides})

