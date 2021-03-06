from django.urls import path
from . import views

urlpatterns = [
    path('', views.MovieViews.as_view(), name='main_page'),
    path('filter/', views.FilterMoviesView.as_view(), name='filter'),
    path('search/', views.Search.as_view(), name='search'),
    path('category/<slug:slug>/', views.CategoryFilter.as_view(), name='category'),
    path('star_filter', views.SearchStar.as_view(), name='star_filter'),
    path("add-rating/", views.AddStarRating.as_view(), name='add_rating'),
    path('json-filter/', views.JsonFilterMoviesView.as_view(), name='json_filter'),
    path('<slug:slug>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('review/<int:pk>/', views.AddReview.as_view(), name='add_review'),
    path('actor/<str:slug>/', views.ActorView.as_view(), name='actor_detail'),
]