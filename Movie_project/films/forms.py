from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    release_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date', 'class': 'form-control'}
        )
    )

    class Meta:
        model = Movie
        fields = ['title', 'description', 'release_date', 'review']
