from django.urls import path
from .views import movies_page_view, movie_details_page_view, delete_movies_page_view, edit_movies_page_view, \
    index_page_view

urlpatterns = [
    path('', index_page_view, name='index_page'),
    path('movies/', movies_page_view, name='movies_page'),
    path('movies/<int:pk>/', movie_details_page_view, name='movie_details_page'),
    path('movies/<int:pk>/edit/', edit_movies_page_view, name='edit_movie_page'),
    path('movies/<int:pk>/delete/', delete_movies_page_view, name='delete_movie_page')
]
