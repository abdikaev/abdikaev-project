from django.urls import path
from .views import (
    movie_details_view,
    movies_page_view,
    delete_movie_page_view,
    index_page_view,
    edit_movie_view,
    category_movies_view
)

urlpatterns = [
    path('', index_page_view, name='index_page'),
    path('category/<int:pk>/movies/', category_movies_view,  name='category_movies'),
    path('movies/', movies_page_view, name='movies'),
    path('movies/<int:pk>/', movie_details_view, name='movie_details'),
    path('movies/<int:pk>/edit/', edit_movie_view, name='edit_movie'),
    path('movies/<int:pk>/delete/', delete_movie_page_view, name='delete_movie_page'),
]
