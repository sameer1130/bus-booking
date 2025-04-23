from django.contrib import admin
from .models import Bus, BusRoute

# Register your models here.
@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ('uuid','bus_number', 'bus_name','capacity', 'created_at','bus_type', 'updated_at')
    search_fields = ('bus_number',)
    ordering = ('-created_at',)

@admin.register(BusRoute)
class BusRouteAdmin(admin.ModelAdmin):
    list_display = ('uuid','bus', 'source', 'destination', 'departure_time', 'arrival_time', 'price', 'date','created_at','updated_at')
    search_fields = ('bus__bus_number', 'source', 'destination')
    ordering = ('-created_at',)