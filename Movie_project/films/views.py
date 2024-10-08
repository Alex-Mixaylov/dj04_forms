from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie
from .forms import MovieForm


def index(request):
    return render(request, 'films/index.html')


def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('films')
        else:
            print("Форма не прошла валидацию.")
            print(form.errors)  # Вывод ошибок формы в консоль терминала
    else:
        form = MovieForm()

    return render(request, 'films/forms.html', {'form': form})


def view_movies(request):
    movies = Movie.objects.all()
    return render(request, 'films/films.html', {'movies': movies})

