from django.shortcuts import render
from rest_framework import viewsets
from .serialisers import CarSerializer, CategorySerializer
from .models import Car, Category
# Create your views here.
class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer