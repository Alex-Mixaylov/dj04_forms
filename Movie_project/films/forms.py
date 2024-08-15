from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    release_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date', 'class': 'form-control', 'format': '%d.%m.%Y'}
        ),
        input_formats=['%d.%m.%Y']
    )

    class Meta:
        model = Movie
        fields = ['title', 'poster', 'description', 'release_date', 'review']
        widgets = {
            'poster': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'review': forms.Textarea(attrs={'class': 'form-control'}),
        }
