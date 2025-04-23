from django.db import models
from core.mixins import AbstractTrack

# Create your models here.
class Booking(AbstractTrack):
    class Status(models.TextChoices):
        PENDING = 'PENDING'
        CONFIRMED = 'CONFIRMED'
        CANCELLED = 'CANCELLED'
    
    user = models.ForeignKey('core.User', on_delete=models.CASCADE, related_name='bookings')
    bus_route = models.ForeignKey('bus.BusRoute', on_delete=models.CASCADE, related_name='bookings')
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )
    
    def __str__(self):
        return f"Booking {self.uuid} by {self.user.first_name} {self.user.last_name}"
    

class BookedSeat(AbstractTrack):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='seats')
    seat_number = models.CharField(max_length=10)
    is_cancelled = models.BooleanField(default=False)
    # booking_date = models.DateField()

    
    def __str__(self):
        return f"Seat {self.seat_number} for Booking {self.booking.uuid}"