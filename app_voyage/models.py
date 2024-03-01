from django.db import models

class Trips(models.Model):
    departuredate = models.DateTimeField('date of departure')
    returndate = models.DateTimeField('date of return')
    destination = models.CharField(max_length=200)
    transporttype = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seats = models.IntegerField()


class Reservation(models.Model):
    trip = models.ForeignKey(Trips, on_delete=models.CASCADE)
    details = models.CharField(max_length=200)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

class Accommodation(models.Model):
    trip = models.ForeignKey(Trips, on_delete=models.CASCADE)
    hotelname = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=200)
    startdate = models.DateTimeField('date of arrival')
    enddate = models.DateTimeField('date of departure')
    details = models.CharField(max_length=200)



