from rest_framework import serializers
from .models import Car, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name',]

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['category', 'name', 'price']