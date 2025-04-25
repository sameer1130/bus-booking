from django_filters import rest_framework as filters
from django.db.models import Q
from .models import Booking

class BookingFilters(filters.FilterSet):
    bus = filters.CharFilter(method="filter_bus")
    customer_name = filters.CharFilter(method="filter_customer_name")
    date = filters.CharFilter(field_name="bus_route__date")
    bus_route = filters.CharFilter(field_name="bus_route__uuid")

    def filter_bus(self, queryset, name, value):
        return queryset.filter(
            Q(bus_route__bus__bus_name__iexact=value) |
            Q(bus_route__bus__bus_number__iexact=value)
        )
    
    def filter_customer_name(self, queryset, name, value):
        return queryset.filter(
            Q(user__first_name__iexact=value) |
            Q(user__last_name__iexact=value)
        )