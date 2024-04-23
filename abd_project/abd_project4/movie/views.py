from django.shortcuts import render, redirect
from .models import Movie, BasketItem
from .forms import CreateMovieForm
from django.contrib import messages


def movie_page_view(request):
    if request.method == 'GET':
        form = CreateMovieForm()
        movies = Movie.objects.all()
        return render(request, 'movie/index.html', {'movies': movies, 'form': form})
    elif request.method == 'POST':
        form = CreateMovieForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            rating = form.cleaned_data.get('rating')
            movie = Movie(title=title, description=description, rating=rating)
            movie.save()
            messages.success(request, 'Movie created successfully.')
            return redirect('/movies')
    else:
        return redirect('/movies')

def movie_details_view(request, pk):
    try:
        movie = Movie.objects.get(id=pk)
        return render(request, 'movie/movie-details.html', {'movie': movie})
    except Movie.DoesNotExist:
        error = 'Movie not found'
        messages.error(request, error)
        return redirect('/movies')


def delete_movie_page_view(request, pk):
    try:
        movie = Movie.objects.get(id=pk)
        movie.delete()
        messages.success(request, 'Movie deleted successfully.')
        return redirect('/movies')
    except Movie.DoesNotExist:
        error = 'Movie not found'
        messages.error(request, error)
        return redirect('/movies')


def basket_page_view(request):
    if request.user.is_authenticated:
        basket_items = BasketItem.objects.filter(owner=request.user)
        return render(request, 'movie/basket.html', {'basket_items': basket_items})
    else:
        return redirect('/auth/login')


def add_movie_to_basket_view(request, pk):
    if request.user.is_authenticated:
        movie = Movie.objects.get(pk=pk)
        basket_item = BasketItem(movie=movie, owner=request.user)
        basket_item.save()
        messages.success(request, 'Movie added to basket successfully.')
        return redirect('/basket/')
    else:
        return redirect('/auth/login/')


def delete_from_basket_view(request, pk):
    if request.user.is_authenticated:
        try:
            basket_item = BasketItem.objects.get(pk=pk)
            if request.user == basket_item.owner:
                basket_item.delete()
                messages.success(request, 'Item removed from basket successfully.')
            else:
                messages.error(request, 'You are not authorized to delete this item.')
        except BasketItem.DoesNotExist:
            messages.error(request, 'Basket item not found.')
    else:
        messages.error(request, 'Please login to delete items from your basket.')
    return redirect('/basket/')
