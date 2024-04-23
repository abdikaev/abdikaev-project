from django.urls import path
from .views import movie_details_view, movie_page_view, delete_movie_page_view, basket_page_view  # Добавлено новое представление

urlpatterns = [
    path('', movie_page_view, name='movie_page'),  # Страница списка фильмов
    path('movies/', movie_page_view, name='movies'),  # Также страница списка фильмов
    path('movies/<int:pk>/', movie_details_view, name='movie_detail'),  # Страница деталей фильма
    path('movies/<int:pk>/delete/', delete_movie_page_view, name='delete_movie_page'),  # Страница удаления фильма
    path('basket/', basket_page_view, name='basket'),  # Новая страница корзины
]
