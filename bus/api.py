from rest_framework.views import APIView
from .models import BusRoute
from .serializers import BusRouteSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets


# class BusRouteAPIView(APIView):
#     def get(self, request):
#         source = request.query_params.get('source')
#         destination = request.query_params.get('destination')
#         if not source or not destination:
#             return Response({"error": "Source and destination are required."}, status=400)
        
#         bus_routes = BusRoute.objects.filter(source=source, destination=destination)
#         if not bus_routes.exists():
#             return Response({"error": "No bus routes found."}, status=404)
        
#         serializer = BusRouteSerializer(bus_routes, many=True)
#         return Response(serializer.data, status=200)
    


class BusRouteViewSet(viewsets.ViewSet):
    def list(self, request):
        source = request.query_params.get('source')
        destination = request.query_params.get('destination')
        if not source or not destination:
            return Response({"error":"Source and Destination are required"}, status=400)
        bus_routes = BusRoute.objects.filter(source=source, destination=destination)
        if not bus_routes.exists():
            return Response({"error":"No bus route found"}, status=400)
        serializer = BusRouteSerializer(bus_routes, many = True)
        return Response(serializer.data, status= 200)
    
    @action(detail= True, methods=['GET'])
    def available_seats(self, request, pk=None):
        bus_route = BusRoute.objects.get(uuid=pk)
        serializer = BusRouteSerializer(bus_route)
        return Response({"available_seats":serializer.data.get("available_seats")})

    