from django.shortcuts import render
from rest_framework import generics
from .serializers import UserCreateSerializer  
from .models import User

# Create your views here.
class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
