from .models import Booking, BookedSeat
from rest_framework import serializers

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['uuid', 'user', 'bus_route', 'status', 'created_at', 'updated_at']

class BookedSeatSerializer(serializers.ModelSerializer):
    source = serializers.SerializerMethodField()
    destination = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()
    class Meta:
        model = BookedSeat
        fields = ['uuid', 'booking', 'seat_number','source','destination' ,'date','is_cancelled']

    def get_source(self, obj):
        return obj.booking.bus_route.source
    def get_destination(self, obj):
        return obj.booking.bus_route.destination
    def get_date(self, obj):
        return obj.booking.bus_route.date

    def validate(self, data):
        booking_input = data.get('booking')
        seat_number = data.get('seat_number')

        bus = booking_input.bus_route.bus 


        try:
            seat_num_int = int(seat_number)
        except (TypeError, ValueError):
            raise serializers.ValidationError("Seat number must be an integer.")

        if seat_num_int < 1 or seat_num_int > bus.capacity:
            raise serializers.ValidationError(f"Seat number must be between 1 and {bus.capacity}.")

        if BookedSeat.objects.filter(booking__bus_route__bus=bus, seat_number=seat_number).exists():
            raise serializers.ValidationError(f"Seat {seat_number} is already booked for this bus.")

        return data

        