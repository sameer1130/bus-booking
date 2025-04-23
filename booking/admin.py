from django.contrib import admin
from .models import Booking, BookedSeat

# Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'user', 'bus_route', 'status', 'created_at', 'updated_at')
    list_filter = ('status',)
    search_fields = ('user__username', 'bus__bus_number')
    ordering = ('-created_at',)


@admin.register(BookedSeat)
class BookedSeatAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'booking', 'seat_number', 'is_cancelled')
    list_filter = ('is_cancelled',)
    search_fields = ('booking__user__username', 'seat_number')
    # ordering = ('-booking_date',)
