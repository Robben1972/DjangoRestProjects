# booking/urls.py
from django.urls import path
from .views import (
    HotelListCreateView, HotelDetailView,
    RoomListCreateView, RoomDetailView,
    ReservationCreateView, ReservationDetailView
)

urlpatterns = [
    path('hotels/', HotelListCreateView.as_view(), name='hotel-list-create'),
    path('hotels/<int:pk>/', HotelDetailView.as_view(), name='hotel-detail'),
    path('hotels/<int:hotel_id>/rooms/', RoomListCreateView.as_view(), name='room-list-create'),
    path('rooms/<int:pk>/', RoomDetailView.as_view(), name='room-detail'),
    path('reservations/', ReservationCreateView.as_view(), name='reservation-create'),
    path('reservations/<int:pk>/', ReservationDetailView.as_view(), name='reservation-detail'),
]
