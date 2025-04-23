from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .models import Booking, BookedSeat
from bus.models import Bus, BusRoute
from core.models import User
from .models import Booking
from .serializers import BookingSerializer, BookedSeatSerializer
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db import models


class CreateBookingView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        user = request.user
        bus_route_id = request.data.get('bus_route')

        if not bus_route_id:
            return Response({"error": "Bus route ID is required."}, status=400)
        try:
            bus_route = BusRoute.objects.get(uuid=bus_route_id)
        except BusRoute.DoesNotExist:
            return Response({"error": f"No route found with ID {bus_route_id}."}, status=404)

        
        
        
        booking = Booking.objects.create(user=user, bus_route=bus_route, status=Booking.Status.CONFIRMED)
        serializer = BookingSerializer(booking)
        
        return Response({"message": "Booking created successfully.", "data": serializer.data}, status=201)
         


class BookingListView(ListAPIView):
    serializer_class = BookingSerializer

    def get_queryset(self):
        queryset = Booking.objects.select_related('user', 'bus_route', 'bus_route__bus').all()
        bus_name = self.request.query_params.get('bus_name')
        date = self.request.query_params.get('date')
        customer_name = self.request.query_params.get('customer_name')
        bus_route = self.request.query_params.get('bus_route')

        if bus_name:
            queryset = queryset.filter(
                Q(bus_route__bus__bus_number__icontains=bus_name) | 
                Q(bus_route__bus__bus_name__icontains=bus_name)
            )
        if date:
            queryset = queryset.filter(bus_route__date=date)
        if customer_name:
            queryset = queryset.filter(Q(user__first_name__icontains=customer_name) | Q(user__last_name__icontains=customer_name))
        if bus_route:
            try:
                queryset = queryset.filter(bus_route__uuid=bus_route)
            except:
                return queryset.none()
            
        return queryset

class CancelBookingView(APIView):
    def delete(self, request, uuid):
        try:
            booking = Booking.objects.get(uuid=uuid)
        except Booking.DoesNotExist:
            return Response({"error": "Booking not found."}, status=404)
        booking.status = Booking.Status.CANCELLED
        booking.save()
        booking.seats.update(is_cancelled=True)

        serializer = BookingSerializer(booking)


        return Response({"message": "Booking cancelled successfully.", "data":serializer.data}, status=200)
    

# class BookSeatView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         user = request.user
#         # bus_number = request.data.get('bus_number')
#         # booking_date = request.data.get('booking_date')
#         seat_number = request.data.get('seat_number')
#         # phone = request.data.get("phone")
#         booking = request.data.get('booking_id')


#         if not booking:
#             return Response({"error": "Booking Id is required."}, status=400)
        
#         # if not isinstance(seat_numbers, list):
#         #     return Response({"error": "Seat number must be a list."}, status=400)
#         if not seat_number:
#             return Response({"error": "Seat numbers are required."}, status=400)
        
#         try:
#             booking_id = Booking.objects.get(uuid=booking)
#         except Booking.DoesNotExist:
#             return Response({"error": "Booking not found."}, status=404)
        
#         # if not bus.routes.filter(date=booking_date).exists():
#         #     return Response({"error": f"No route available for bus {bus_number} on {booking_date}."}, status=400)

        
#         # booking = Booking.objects.create(user=user, bus=bus, status =Booking.Status.CONFIRMED)
#         # bookedSeat = BookedSeat.objects.create(
#         #     booking=booking_id,
#         #     seat_number=seat_number,
#         #     )
#         # booked_seats = []
#         # errors = []
#         # for seat_number in seat_numbers:
#         #     seat_data = {
#         #         'booking': str(booking.uuid),
#         #         'seat_number': seat_number,
#         #         'booking_date': booking_date,
#         #     }
#         serializer = BookedSeatSerializer(data={
#     'booking': str(booking_id.uuid),  
#     'seat_number': seat_number,
#     })
        
#         if serializer.is_valid():
#             booked_seat = serializer.save()

#             route = booking_id.bus.routes

#             return Response({
#                 "message": "Seats booked successfully.",
#                 "data": serializer.data,
#                 "route_info": {
#                     "source": route.source,
#                     "destination": route.destination,
#                     "date": route.date
#                 }
#             }, status=201)

#         else:
#             return Response(serializer.errors, status=400) 

# class CancelSeatView(APIView):
#     def patch(self, request):
#         bus_number = request.data.get('bus_number')
#         boooking_date = request.data.get('booking_date')
#         seat_number = request.data.get('seat_number')
#         phone = request.data.get('phone')

#         if not bus_number or not boooking_date or not seat_number:
#             return Response({"error": "Bus number, booking date and seat number are required."}, status=400)
        
#         try:
#             user = User.objects.get(phone=phone)
#         except User.DoesNotExist:
#             return Response({"error": "User not found."}, status=404)
        
#         try:
#             bus = Bus.objects.get(bus_number=bus_number)
#             booking = Booking.objects.get(bus=bus, user=user, status=Booking.Status.CONFIRMED)
#         except (Bus.DoesNotExist, Booking.DoesNotExist):    
#             return Response({"error": "Bus or Booking not found."}, status=404)
        
        
#         try:
#             seat = BookedSeat.objects.get(booking=booking, seat_number=seat_number, booking_date=boooking_date)
#         except BookedSeat.DoesNotExist:
#             return Response({"error": "Seat not found."}, status=404)
#         seat.is_cancelled = True
#         seat.save()

#         return Response({"message": "Seat cancelled successfully."}, status=200)

class BookSeatView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, uuid):
        user = request.user
        seat_number = request.data.get('seat_number')
        booking = Booking.objects.get(uuid=uuid)

        # if not booking:
        #     return Response({"error": "Booking Id is required."}, status=400)

        if not seat_number:
            return Response({"error": "Seat number is required."}, status=400)

        # try:
        #     booking_id = Booking.objects.get(uuid=uuid)
        # except Booking.DoesNotExist:
        #     return Response({"error": "Booking not found."}, status=404)

        serializer = BookedSeatSerializer(data={
            'booking': str(booking.uuid),  
            'seat_number': seat_number,
        })

        if serializer.is_valid():
            # booked_seat = serializer.save()
            # route = booking.bus_route 

            return Response({
                "message": "Seats booked successfully.",
                "data": serializer.data,
                # "route_info": {
                #     "source": route.source,
                #     "destination": route.destination,
                #     "date": route.date
                # }
            }, status=201)

        return Response(serializer.errors, status=400)


class CancelSeatView(APIView):

    def delete(self, request, uuid):
        seat_number = request.data.get('seat_number')
        booking = Booking.objects.get(uuid=uuid)

        if not seat_number:
            return Response({"error": "Seat number is required."}, status=400)
        try:
            seat = BookedSeat.objects.filter(booking__uuid=booking.uuid, seat_number=seat_number).first() 
        except BookedSeat.DoesNotExist:
            return Response({"error": "Seat not found."}, status=404)
        
        if seat.is_cancelled:
            return Response({"message": "Seat is already cancelled."}, status=200)

        seat.is_cancelled = True
        seat.save()

        serializer = BookedSeatSerializer(seat)
        
        return Response({
                "message": "Seat cancelled successfully.",
                "data": serializer.data,
            }, status=200)


        

class AvailableSeatsView(APIView):
    def get(self, request,uuid):
        # bus_route = request.query_params.get('bus_route')
        # if not bus_route:
        #     return Response({"error": "Bus route is required."}, status=400)
        
        try:
            route = BusRoute.objects.get(uuid=uuid)
        except BusRoute.DoesNotExist:
            return Response({"error": "Bus route not found."}, status=404)

        bus = route.bus 

        booked_seats_count = BookedSeat.objects.filter(
            booking__bus_route=route,
            is_cancelled=False
        ).count()

        available_seats = bus.capacity - booked_seats_count 
       



        return Response({
            "bus_route": str(route),
            "available_seats": available_seats,
            "total_seats": bus.capacity,
           
        }, status=200)
