from django.shortcuts import render, redirect
from .models import Movie, Category
from .forms import CreateMovieForm, MovieForm
from django.contrib import messages


def index_page_view(request):
    categories = Category.objects.all()
    return render(request, 'movie/index.html', {'categories': categories})


def movies_page_view(request):
    categories = Category.objects.all()
    if request.method == 'GET':
        form = MovieForm()
        movies = Movie.objects.all()
        return render(request, 'movie/movies.html', {'movies': movies, 'form': form, 'categories': categories})
    elif request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            producer = form.cleaned_data.get('producer')
            duration = form.cleaned_data.get('duration')
            category_id = form.cleaned_data.get('category')
            movie = Movie(
                title=title,
                description=description,
                producer=producer,
                duration=duration,
                category_id=category_id
            )
            movie.save()
        movies = Movie.objects.all()
        return render(request, 'movie/movies.html', {'movies': movies, 'form': form, 'categories': categories})


def movie_details_view(request, pk):
    movie = Movie.objects.get(id=pk)
    return render(request, 'movie/movie-detail.html', {'movie': movie})


def category_movies_view(request, pk):
    category = Category.objects.get(id=pk)
    movies = Movie.objects.filter(category_id=pk)
    if request.method == 'GET':
        form = CreateMovieForm()
        return render(request, 'movie/category-movies.html', {'category': category, 'movies': movies, 'form': form})
    elif request.method == 'POST':
        form = CreateMovieForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            producer = form.cleaned_data.get('producer')
            duration = form.cleaned_data.get('duration')
            movie = Movie(title=title, description=description, producer=producer, duration=duration, category_id=pk)
            movie.save()
        movies = Movie.objects.filter(category_id=pk)
        return render(request, 'movie/category-movies.html', {'category': category, 'movies': movies, 'form': form})


def edit_movie_view(request, pk):
    movie = Movie.objects.get(id=pk)
    if request.method == 'GET':
        form = MovieForm(initial={'title': movie.title, 'description': movie.description,
                                  'producer': movie.producer, 'duration': movie.duration})
        return render(request, 'movie/edit-movie.html', {'movie': movie, 'form': form})
    elif request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie.title = form.cleaned_data.get('title')
            movie.description = form.cleaned_data.get('description')
            movie.producer = form.cleaned_data.get('producer')
            movie.duration = form.cleaned_data.get('duration')
            movie.save()
            return redirect('movie_details', pk=pk)


def delete_movie_page_view(request, pk):
    try:
        movie = Movie.objects.get(id=pk)
        movie.delete()
        return redirect('movies')
    except Movie.DoesNotExist:
        messages.error(request, 'Movie not found.')
        return redirect('movies')
