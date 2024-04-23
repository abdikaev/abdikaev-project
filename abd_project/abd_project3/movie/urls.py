from django.urls import path
from .views import index_page, movies_details, delete_movie

urlpatterns = [
    path('', index_page, name='index'),
    path('movies/', index_page, name='movies_post'),
    path('<int:pk>/delete/', delete_movie, name='delete_movie'),
    path('<int:pk>/', movies_details, name='movie_detail'),
]
