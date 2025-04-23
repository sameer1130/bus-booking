from rest_framework import serializers
from .models import Bus, BusRoute


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
            "created_at",
            "updated_at",
        )