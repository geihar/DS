from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.MovieListView.as_view()),
    path('review/', views.ReviewCreateView.as_view()),
    path('rating/', views.AddStarRating.as_view()),
    path('actors/', views.ActorListView.as_view()),
    path('actors/<int:pk>', views.ActorDetailView.as_view()),
    path('movies/<int:pk>/', views.MovieDetailView.as_view()),
]


