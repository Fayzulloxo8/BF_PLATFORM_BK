from .models import *
from rest_framework import serializers

from rest_framework import serializers
from .models import Movie, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # Kategoriya nomini chiqaradi

    class Meta:
        model = Movie
        fields = '__all__'
