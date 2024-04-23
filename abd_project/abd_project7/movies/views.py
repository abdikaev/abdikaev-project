from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Max
from .models import Movie
from .forms import MovieForm

sizes = [4, 8, 12, 24, 36]


def movies_page_view(request):
    size = request.GET.get('size', 10)
    page = request.GET.get('page', 1)
    order_by = request.GET.get('order_by', 'title')
    title = request.GET.get('title', '')
    min_duration = request.GET.get('min_duration', 0)
    max_duration = Movie.objects.aggregate(max_duration=Max('duration'))['max_duration']
    movies = Movie.objects.filter(title__icontains=title, duration__gte=min_duration, duration__lte=max_duration).order_by(order_by)
    filters = {
        'title': title,
        'min_duration': min_duration,
        'max_duration': max_duration
    }
    paginator = Paginator(movies, size)
    page_obj = paginator.get_page(page)
    return render(request, 'movies/movies.html', {'page_obj': page_obj, 'paginator': paginator, 'sizes': sizes, 'order_by': order_by, 'filters': filters})


def index_page_view(request):
    form = MovieForm()
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies_page')
    return render(request, 'movies/index.html', {'form': form})


def edit_movies_page_view(request, pk):
    movie = get_object_or_404(Movie, id=pk)
    form = MovieForm(request.POST or None, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('movie_details_page', pk=pk)
    return render(request, 'movies/edit-movie.html', {'movie': movie, 'form': form})


def movie_details_page_view(request, pk):
    movie = get_object_or_404(Movie, id=pk)
    return render(request, 'movies/movie-details.html', {'movie': movie})


def delete_movies_page_view(request, pk):
    movie = get_object_or_404(Movie, id=pk)
    movie.delete()
    return redirect('movies_page')
