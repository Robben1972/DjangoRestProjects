# booking/views.py
from rest_framework import generics
from .models import Hotel, Room, Reservation
from .serializers import HotelSerializer, RoomSerializer, ReservationSerializer


class HotelListCreateView(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class HotelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class RoomListCreateView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get_queryset(self):
        return Room.objects.filter(hotel_id=self.kwargs['hotel_id'])

    def perform_create(self, serializer):
        hotel = generics.get_object_or_404(Hotel, id=self.kwargs['hotel_id'])
        serializer.save(hotel=hotel)


class RoomDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class ReservationCreateView(generics.CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class ReservationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
