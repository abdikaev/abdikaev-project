from django import forms

class CreateMovieForm(forms.Form):
    title = forms.CharField(min_length=1, max_length=255, required=True)
    description = forms.CharField(min_length=1, max_length=3000, required=False)
    producer = forms.DateField(required=True)
    duration = forms.IntegerField(required=True)
