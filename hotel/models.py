# booking/models.py
from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    rating = models.FloatField()

    def __str__(self):
        return self.name


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='rooms', on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=50)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f'Room {self.room_number} at {self.hotel.name}'


class Reservation(models.Model):
    room = models.ForeignKey(Room, related_name='reservations', on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=255)
    check_in_date = models.DateField()
    check_out_date = models.DateField()

    def __str__(self):
        return f'Reservation for {self.guest_name} in room {self.room.room_number}'
