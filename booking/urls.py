from django.urls import path
from .api import BookingListView,CancelBookingView, BookSeatView, CancelSeatView,CreateBookingView

urlpatterns = [
    path("bookings/", BookingListView.as_view(), name="booking-list"),
    path("bookings/<uuid:uuid>/cancel/", CancelBookingView.as_view(), name="cancel-booking"),
    path("bookings/<uuid:uuid>/book-seat/", BookSeatView.as_view(), name="book-seat"),
    # path('bookings/cancel-seat/<uuid:pk>/', CancelSeatView.as_view(), name='cancel-seat'),
    path('bookings/<uuid:uuid>/cancel-seat/', CancelSeatView.as_view(), name='cancel-seat'),
    # path('bookings/<uuid:uuid>/available-seats/', AvailableSeatsView.as_view(), name='available-seats'),
    path('bookings/create/', CreateBookingView.as_view(), name='create-booking'),
]