# views.py

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .utils import *

def home(request):
    triplist = Trips.objects.all()
    return render(request, 'home.html', {'trips': triplist})

#region trips
def trip_details(request, trip_id):
    trip = Trips.objects.get(id=trip_id)
    participants = GetUsersOnTrip(trip_id)
    isontrip = VerifyUserReservation(request.user.id, trip_id)
    accommodations = Accommodation.objects.filter(trip=trip)
    return render(request, 'trip_details.html', {'trip': trip, 'participants': participants, 'isontrip': isontrip, 'accommodations': accommodations})
def list_trip(request):
    trips = Trips.objects.all()
    return render(request, 'trips.html', {'trips': trips})

def search_trips(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query')
        trips = Trips.objects.filter(destination__icontains=search_query)
    else:
        trips = Trips.objects.all()

    return render(request, 'trips.html', {'trips': trips})

#endregion

#region reservations
def my_reservations(request):
    reservations = GetReservationByIdUSer(request.user.id)
    return render(request, 'reservations.html', {'reservations': reservations})

def add_reservation(request, trip_id):
    if not request.user.is_authenticated:
        messages.error(request, 'You must be logged in to make a reservation')
        return redirect('login')
    else:
        if (VerifyUserReservation(request.user.id, trip_id)):
            messages.error(request, 'Vous avez déjà réservé ce voyage.')
            return redirect('trips')
        else:
            trip = Trips.objects.get(id=trip_id)
            AddReservation(request.user.id, trip, "Details")
            return redirect('reservations')

def delete_reservation(request, reservation_id):
    DeleteReservation(reservation_id)
    return redirect('reservations')
#endregion


