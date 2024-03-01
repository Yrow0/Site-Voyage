from datetime import datetime, timedelta
from app_voyage.models import Trips, Accommodation, Reservation
from django.contrib.auth.models import User


# Créer des voyages simulés
def create_simulated_trips():
    Trips.objects.create(
        destination="New York",
        departuredate=datetime.now() + timedelta(days=30),
        returndate=datetime.now() + timedelta(days=37),
        price=1000,
        seats=400,
    )

    Trips.objects.create(
        destination="Paris",
        departuredate=datetime.now() + timedelta(days=45),
        returndate=datetime.now() + timedelta(days=52),
        price=500,
        seats=200,
    )

    Trips.objects.create(
        destination="Tokyo",
        departuredate=datetime.now() + timedelta(days=60),
        returndate=datetime.now() + timedelta(days=67),
        price=2000,
        seats=500,
    )


# Créer des logements simulés pour chaque voyage
def create_simulated_accommodations():
    for trip in Trips.objects.all():
        Accommodation.objects.create(
            trip=trip,
            address="123 Main Street, City",
            startdate=trip.departuredate,
            enddate=trip.returndate,
            hotelname="Hotel ABC",
            phonenumber="123-456-7890",
            details="Breakfast included"
        )


def GetReservationByIdUSer(id) -> list[Reservation]:
    return Reservation.objects.filter(user_id=id)
# Appel des fonctions pour créer les données simulées

def AddReservation(id, trip, details):
    Reservation.objects.create(
        user_id=id,
        trip=trip,
        details=details
    )
    trip.seats -= 1
    trip.save()


def GetUserById(id):
    return User.objects.get(id=id)

def GetUsersOnTrip(trip_id):
    users = []
    reservations = Reservation.objects.filter(trip_id=trip_id)
    for reservation in reservations:
        users.append(GetUserById(reservation.user_id))
    return users

def DeleteReservation(id):
    Reservation.objects.filter(id=id).delete()

def VerifyUserReservation(id, trip_id):
    return Reservation.objects.filter(user_id=id, trip_id=trip_id).exists()
