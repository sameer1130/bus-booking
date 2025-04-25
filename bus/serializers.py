from rest_framework import serializers
from .models import Bus, BusRoute
from booking.models import BookedSeat


class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = (
            "uuid",
            "bus_number",
            "bus_name",
            "capacity",
            "bus_type",
            "created_at",
            "updated_at",
        )

class BusRouteSerializer(serializers.ModelSerializer):
    # available_seats = serializers.SerializerMethodField()


    class Meta:
        model = BusRoute
        fields = (
            "uuid",
            "bus",
            "source",
            "destination",
            "departure_time",
            "arrival_time",
            "price",
            "date",
            "available_seats",
            "total_seats",
            "created_at",
            "updated_at",
        )

    # def get_available_seats(self, obj):
    #     total_capacity = obj.bus.capacity

    #     booked_seat_count = BookedSeat.objects.filter(
    #         booking__bus_route=obj,
    #         is_cancelled= False
    #     ).count()
    #     return total_capacity - booked_seat_count


class AvailableSeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusRoute
        fields = ['source', 'destination', 'date', 'total_seats', 'available_seats']


