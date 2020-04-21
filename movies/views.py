from django.shortcuts import render
from django.views.generic.base import View

from .models import Movie


class MovieViews(View):
    def get(self, request):
        movie = Movie.objects.all()
        return render(request, 'movies/movies.html', {'movie_list': movie})


class MovieDetailView(View):

    def get(self, request, slug):
        movie = Movie.objects.get(url=slug)
        return render(request, 'movies/moviesingle.html', {'movie_list': movie})