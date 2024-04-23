from django import forms
from .models import Movie

class CreateMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'producer', 'duration', 'rating']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'producer': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Producer'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Duration'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Rating'}),
        }

