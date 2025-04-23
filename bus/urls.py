from django.urls import path
from .api import BusRouteAPIView

urlpatterns = [
    path("buses/search/", BusRouteAPIView.as_view(), name="bus-search"),
]
