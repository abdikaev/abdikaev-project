from django import forms
from .models import Movie


class CreateMovieForm(forms.Form):
    title = forms.CharField(min_length=1, max_length=255, required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': 'Enter movie title'
                                                          }))
    description = forms.CharField(min_length=0, max_length=3000, required=False,
                                  widget=forms.TextInput(attrs={'class': 'form-control',
                                                                'placeholder': 'Enter description'
                                                                }))
    producer = forms.CharField(min_length=1, max_length=255, required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Enter movie producer'
                                                             }))
    duration = forms.IntegerField(min_value=1, required=True,
                                  widget=forms.TextInput(attrs={'class': 'form-control',
                                                                'placeholder': 'Enter duration'
                                                                }))


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        # fields = ['title', 'duration', 'producer', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter movie title'}),
            'duration': forms.TextInput(
                attrs={
                    'type': 'number',
                    'class': 'form-control',
                    'placeholder': 'Enter duration'
                }
            ),

            'producer': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter producer'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description'}),
            'category': forms.Select(attrs={'class': 'form-select'})
        }
