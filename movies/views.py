from django.shortcuts import render
from rest_framework.generics import GenericAPIView

from movies.serializers import MovieSerializer
from .models import Movie


# Create your views here.

class MovieAPIView(GenericAPIView):
    queryset = Movie
    serializer_class = MovieSerializer
