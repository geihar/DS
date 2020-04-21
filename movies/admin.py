from django.contrib import admin
from .models import Category, Actor, RatingStars, Rating, Movie, MoviesShots, Genre, Reviews

admin.site.register(Category)
admin.site.register(Actor)
admin.site.register(RatingStars)
admin.site.register(Movie)
admin.site.register(MoviesShots)
admin.site.register(Rating)
admin.site.register(Genre)
admin.site.register(Reviews)
