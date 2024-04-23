from django.shortcuts import render, redirect
from .models import Movie
from .forms import CreateMovieForm

def index_page(request):
    if request.method == 'GET':
        form = CreateMovieForm()
        movies = Movie.objects.all()
        return render(request, 'movie/index.html', {'movies': movies, 'form': form})
    elif request.method == 'POST':
        form = CreateMovieForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            producer = form.cleaned_data['producer']
            duration = form.cleaned_data['duration']
            movie = Movie.objects.create(title=title, description=description, producer=producer, duration=duration)
            return redirect('movie_detail', pk=movie.pk)  # Redirect to the movie detail page
        else:
            movies = Movie.objects.all()
            return render(request, 'movie/index.html', {'movies': movies, 'form': form})

def movies_details(request, pk):
    movie = Movie.objects.get(id=pk)
    return render(request, 'movie/movie-detail.html', {'movie': movie})

def delete_movie(request, pk):
    try:
        movie = Movie.objects.get(id=pk)
        movie.delete()
        return redirect('index')  # Redirect to the index page after deleting the movie
    except Movie.DoesNotExist:
        error = 'Movie not found'
        form = CreateMovieForm()
        movies = Movie.objects.all()
        return render(request, 'movie/index.html', {'movies': movies, 'form': form, 'error': error})
