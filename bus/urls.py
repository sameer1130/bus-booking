from django.urls import path
from .api import BusRouteViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("busroutes",BusRouteViewSet,basename="busroute")

urlpatterns = router.urls