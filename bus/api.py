from rest_framework.views import APIView
from .models import BusRoute
from .serializers import BusRouteSerializer
from rest_framework.response import Response


class BusRouteAPIView(APIView):
    def get(self, request):
        source = request.query_params.get('source')
        destination = request.query_params.get('destination')
        if not source or not destination:
            return Response({"error": "Source and destination are required."}, status=400)
        
        bus_routes = BusRoute.objects.filter(source=source, destination=destination)
        if not bus_routes.exists():
            return Response({"error": "No bus routes found."}, status=404)
        
        serializer = BusRouteSerializer(bus_routes, many=True)
        return Response(serializer.data, status=200)


    