# urls.py

from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    #trips

    path('trips/', list_trip, name='trips'),
    path('trip_details/<int:trip_id>/', trip_details, name='trip_details'),
    path('search_trips/', search_trips, name='search_trips'),

    #reservations
    path('reservations/', my_reservations, name='reservations'),
    path('add_reservation/<int:trip_id>/', add_reservation, name='add_reservation'),
    path('delete_reservation/<int:reservation_id>/', delete_reservation, name='delete_reservation'),

]
