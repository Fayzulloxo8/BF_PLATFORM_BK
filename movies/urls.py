from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import MovieListCreateView, CategoryListCreateView

urlpatterns = [
    path('movies/', MovieListCreateView.as_view(), name='movie-list'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
]
