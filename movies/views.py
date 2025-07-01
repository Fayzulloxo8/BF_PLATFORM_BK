from rest_framework import generics
from .models import Movie,Category
from .serializer import MovieSerializer ,CategorySerializer # agar senga kerakli serializer nomi shu bo‘lsa


class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
